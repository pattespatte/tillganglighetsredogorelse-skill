#!/usr/bin/env python3
"""Kontrollera att ett tillgänglighetsdokument uppfyller lagkrav och mallens regler.

Används av skillen tillganglighetsredogorelse i läget kontrollera (och efter
utkast/uppdatering):

    python3 kontrollera.py REDOGÖRELSE.md [--app] [--lptt]

Två lägen: DOS-lagen (standard, samt --app för mobilapplikationer) med grund i
MDFFS 2019:2 §6 och Diggs vägledning och Word-mallar, och tillgänglighetslagen
(2023:254) med --lptt och grund i 25 § lagen, 24 § förordningen (2023:676) och
PTS vägledning. Kontrollerna är syntaktiska – de konstaterar att obligatoriska
delar finns och att mallens platshållare är utbytta, inte att innehållet är sant.

Varje kontroll rapporteras som OK, FEL eller VARNING. FEL ger exit 1 och raden
"BRISTER", VARNING påverkar inte exit-koden. Utdata är kompakt: en rad per
kontroll, aldrig dokumentinnehåll.
"""

import re
import sys
from pathlib import Path

# Mallens instruktionsfraser som ska vara borta i en färdig redogörelse.
KVARLEVOR = [
    "VILLKORLIGT", "ÅÅÅÅ",
    "[Om helt:", "[Om delvis", "[Om inte:", "[Om helt]",
    "[Välj ett alternativ", "[Kvar endast om", "[Annars: behåll",
    "[Helt tillgänglig:", "[Svarstiden är normalt", "[Metod,",
    "[Granskningsmetod]", "[Granskningsrapport", "[ring ",
    "[Webbplatsen publicerades", "[Appen publicerades",
]

# Obligatoriska H2-fragment (variantneutrala mellan webbplats och app).
OBLIGATORISKA_RUBRIKER = [
    "Hur tillgänglig är",
    "Vad kan du göra om du inte kan använda",
    "Rapportera brister",
    "Tillsyn",
    "Teknisk information om",
    "Innehåll som inte är tillgängligt",
    "Hur vi testat",
]

# LPTT-läget: mallens instruktionsfraser som ska vara borta i en färdig information.
LPTT_KVARLEVOR = [
    "VILLKORLIGT", "ÅÅÅÅ",
    "[Om tjänsten följer standarden:", "[Om tjänsten inte följer standarden:",
    "[Om inga kända brister:", "[Om kända brister:",
    "[Inga kända brister:", "[Kvar endast om", "[Annars:",
    "[Om du upptäcker", "[ring ", "[använd vårt", "[Vi arbetar",
    "[Om tjänsten även finns som app", "[För tjänster under PTS",
]

# LPTT-läget: obligatoriska H2-fragment enligt references/mall-lptt.md.
LPTT_OBLIGATORISKA_RUBRIKER = [
    "Om tjänsten",
    "Hur tillgänglig är",
    "som kan vara svåra att använda",
    "Hur vi kontrollerar",
    "Kontakta oss",
    "Tillsyn",
]

# Tillsynsmyndigheter enligt förordningen (2023:676).
TILLSYNSMYNDIGHETER = [
    "PTS", "Post- och telestyrelsen",
    "Mediemyndigheten",
    "Konsumentverket",
    "Transportstyrelsen",
    "Myndigheten för tillgängliga medier",
]

DATUM = r"\d{4}-\d{2}-\d{2}"
EPOST = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
LANK = r"\]\(\s*https?://"
KRITERIUM = re.compile(r"(WCAG\s*)?\b\d+\.\d+(?:\.\d+)?\b|EN 301 549|klausul", re.I)


def las(p):
    return Path(p).read_text(encoding="utf-8")


class Rubrik:
    def __init__(self, niva, titel, start, slut):
        self.niva, self.titel = niva, titel
        self.start, self.slut = start, slut

    def text(self, rader):
        return "\n".join(rader[self.start:self.slut])


def rubriker(rader):
    """Alla rubriker med (#-nivå) och sina avsnitt (till nästa rubrik)."""
    funna = []
    for i, rad in enumerate(rader):
        m = re.match(r"^(#{1,6})\s+(.*)$", rad)
        if m:
            funna.append(Rubrik(len(m.group(1)), m.group(2).strip(), i + 1, len(rader)))
    for j, r in enumerate(funna):
        r.slut = funna[j + 1].start if j + 1 < len(funna) else len(rader)
    return funna


def hitta(rub, fragment, rader, max_niva=6):
    for r in rub:
        if r.niva <= max_niva and fragment.lower() in r.titel.lower():
            return r
    return None


def listpunkter(text):
    return [rad[2:].strip() for rad in text.splitlines() if rad.lstrip().startswith("- ")]


def kontrollera_lptt(text, rader, rub, namn):
    """Läge för lagen (2023:254): information om tjänstens tillgänglighet."""
    fel, varningar, rapport = 0, 0, []

    def ok(meddelande):
        rapport.append(f"  [OK]      {meddelande}")

    def fel_rad(meddelande):
        nonlocal fel
        fel += 1
        rapport.append(f"  [FEL]     {meddelande}")

    def varning(meddelande):
        nonlocal varningar
        varningar += 1
        rapport.append(f"  [VARNING] {meddelande}")

    print(f"Kontroll av {namn} (tjänst, 2023:254):")

    # 1. Kvarvarande platshållare och mallinstruktioner
    fynd = [k for k in LPTT_KVARLEVOR if k in text]
    fynd += re.findall(r"\{[^{}\n]{1,120}\}", text)
    fynd += [m for m in re.findall(r"<[^<>\n]{1,120}>", text)
             if re.search(r"ÅÅÅÅ|länk|formulär|dag|månad|år|telefonnummer", m, re.I)]
    if fynd:
        fel_rad(f"Platshållare kvar: {', '.join(dict.fromkeys(fynd[:6]))}"
                + (" m.m." if len(fynd) > 6 else ""))
    else:
        ok("Inga platshållare kvar")

    # 2. Rubriker
    h1 = [r for r in rub if r.niva == 1]
    if not h1:
        fel_rad("H1-rubrik saknas")
    saknade = [f for f in LPTT_OBLIGATORISKA_RUBRIKER if hitta(rub, f, rader, max_niva=2) is None]
    if saknade:
        fel_rad(f"Obligatoriska rubriker saknas: {', '.join(saknade)}")
    else:
        ok("Alla obligatoriska rubriker finns")

    # 3. Bristförteckningen och dess användningssituationer
    situationsrubriker = [r for r in rub
                          if r.niva == 3 and r.titel.lower().startswith("problem vid")]
    if situationsrubriker:
        tomma = [r.titel for r in situationsrubriker if not listpunkter(r.text(rader))]
        if tomma:
            fel_rad(f"Användningssituationer utan bristpunkter: {', '.join(tomma)}")
        else:
            punkter = [p for r in situationsrubriker for p in listpunkter(r.text(rader))]
            utan = [p for p in punkter if not KRITERIUM.search(p)]
            ok(f"Bristförteckning: {len(situationsrubriker)} situationer, {len(punkter)} punkter")
            if utan:
                varning(f"{len(utan)} bristpunkt" + ("" if len(utan) == 1 else "er")
                        + " utan hänvisning till WCAG/EN 301 549-kriterium")
    elif re.search(r"känner inte till", text, re.I):
        ok("Inga kända brister (meningen ”känner inte till” finns)")
    else:
        fel_rad("Varken användningssituationer (”Problem vid användning …”) eller mening om inga kända brister finns")

    # 4. 7 §-undantaget: vilka krav och motivering (VILLKORLIGT avsnitt)
    undantag = hitta(rub, "Undantag", rader, max_niva=2)
    if undantag is not None:
        avsnitt = undantag.text(rader)
        if not listpunkter(avsnitt):
            fel_rad("7 §-avsnittet saknar förteckning över vilka krav undantaget gäller")
        elif "Motivering" not in avsnitt:
            fel_rad("7 §-avsnittet saknar motivering (raden ”Motivering: …”)")
        else:
            ok("7 §-avsnitt med kravförteckning och motivering")

    # 5. Kontaktavsnittet (minst en väg – e-post är den som går att se maskinellt)
    kontakt = hitta(rub, "Kontakta oss", rader)
    if kontakt is not None and not re.search(EPOST, kontakt.text(rader)):
        varning("Ingen e-postadress i kontaktavsnittet – kontrollera att minst en kontaktväg finns")

    # 6. Tillsynsavsnittet: rätt myndighet varierar, bara en påminnelse
    tillsyn = hitta(rub, "Tillsyn", rader, max_niva=2)
    if tillsyn is not None:
        avsnitt = tillsyn.text(rader)
        if not any(m.lower() in avsnitt.lower() for m in TILLSYNSMYNDIGHETER):
            varning("Tillsynsavsnittet nämner ingen känd tillsynsmyndighet "
                    "(PTS, Mediemyndigheten, Konsumentverket, Transportstyrelsen, "
                    "Myndigheten för tillgängliga medier) – kontrollera vilken som gäller tjänsteområdet")
        else:
            ok("Tillsynsavsnitt med myndighet")

    # 7. Datum: god praxis enligt PTS vägledning, inte lagkrav
    def datum_efter(markare):
        for rad in rader:
            if markare in rad:
                m = re.search(DATUM, rad)
                return m.group(0) if m else f"OGILTIG ({rad.strip()[:60]})"
        return None

    kontroll = datum_efter("Senaste kontrollen gjordes den")
    uppdaterad = datum_efter("Informationen uppdaterades senast den")
    if kontroll is None:
        varning("Datum för senaste kontroll saknas (”Senaste kontrollen gjordes den …”) – god praxis, inte krav")
    elif not re.fullmatch(DATUM, kontroll):
        fel_rad(f"Kontrolldatum inte i ÅÅÅÅ-MM-DD: {kontroll}")
    else:
        ok(f"Senaste kontroll: {kontroll}")
    if uppdaterad is None:
        varning("Senast uppdaterad saknas (”Informationen uppdaterades senast den …”) – god praxis, inte krav")
    elif not re.fullmatch(DATUM, uppdaterad):
        fel_rad(f"Senast uppdaterad inte i ÅÅÅÅ-MM-DD: {uppdaterad}")
    elif kontroll and re.fullmatch(DATUM, kontroll) and kontroll > uppdaterad:
        fel_rad(f"Kontrolldatum ({kontroll}) ligger efter senast uppdaterad ({uppdaterad})")
    else:
        ok(f"Senast uppdaterad: {uppdaterad}")

    print("\n".join(rapport))
    varningstext = f"{varningar} varning" + ("ar" if varningar != 1 else "")
    if fel:
        print(f"BRISTER – {fel} fel, {varningstext}; rätta och kör igen")
        return 1
    print(f"KLAR – 0 fel, {varningstext}")
    return 0


def main():
    argv = sys.argv[1:]
    app = "--app" in argv
    lptt = "--lptt" in argv
    flaggor = [a for a in argv if a.startswith("--")]
    fil = [a for a in argv if not a.startswith("--")]
    if len(fil) != 1 or any(f not in ("--app", "--lptt") for f in flaggor) or (app and lptt):
        print("Användning: kontrollera.py REDOGÖRELSE.md [--app] [--lptt]", file=sys.stderr)
        return 2

    try:
        text = las(fil[0])
    except OSError as e:
        print(f"Kan inte läsa filen: {e}", file=sys.stderr)
        return 2

    rader = text.splitlines()
    rub = rubriker(rader)
    if lptt:
        return kontrollera_lptt(text, rader, rub, fil[0])
    fel, varningar, rapport = 0, 0, []

    def ok(meddelande):
        rapport.append(f"  [OK]      {meddelande}")

    def fel_rad(meddelande):
        nonlocal fel
        fel += 1
        rapport.append(f"  [FEL]     {meddelande}")

    def varning(meddelande):
        nonlocal varningar
        varningar += 1
        rapport.append(f"  [VARNING] {meddelande}")

    print(f"Kontroll av {fil[0]} ({'app' if app else 'webbplats'}):")

    # 1. Kvarvarande platshållare och mallinstruktioner
    fynd = [k for k in KVARLEVOR if k in text]
    fynd += re.findall(r"\{[^{}\n]{1,120}\}", text)
    fynd += [m for m in re.findall(r"<[^<>\n]{1,120}>", text)
             if re.search(r"ÅÅÅÅ|länk|formulär|dag|månad|år|telefonnummer", m, re.I)]
    if fynd:
        fel_rad(f"Platshållare kvar: {', '.join(dict.fromkeys(fynd[:6]))}"
                + (" m.m." if len(fynd) > 6 else ""))
    else:
        ok("Inga platshållare kvar")

    # 2. Följsamhetsgrad med exakt ord
    grad = None
    for ord_ in ("helt", "delvis", "inte"):
        if re.search(rf"är {ord_} förenlig med", text):
            if grad and grad != ord_:
                fel_rad(f"Följsamhetsgrad: flera grader används ({grad} och {ord_})")
            grad = ord_
    if grad is None:
        fel_rad("Följsamhetsgrad saknas – ingen mening i formen ”är helt/delvis/inte förenlig med”")
    else:
        ok(f"Följsamhetsgrad: {grad}")

    # 3. Rubriker
    h1 = [r for r in rub if r.niva == 1]
    if not h1:
        fel_rad("H1-rubrik saknas")
    saknade = [f for f in OBLIGATORISKA_RUBRIKER if hitta(rub, f, rader, max_niva=2) is None]
    if saknade:
        fel_rad(f"Obligatoriska rubriker saknas: {', '.join(saknade)}")
    else:
        ok("Alla obligatoriska rubriker finns")

    # 4. Datum
    def datum_efter(markare):
        for rad in rader:
            if markare in rad:
                m = re.search(DATUM, rad)
                return m.group(0) if m else f"OGILTIG ({rad.strip()[:60]})"
        return None

    bedomning = datum_efter("Senaste bedömningen gjordes den")
    uppdaterad = datum_efter("uppdaterades senast den")
    if bedomning is None:
        fel_rad("Bedömningsdatum saknas (”Senaste bedömningen gjordes den …”)")
    elif not re.fullmatch(DATUM, bedomning):
        fel_rad(f"Bedömningsdatum inte i ÅÅÅÅ-MM-DD: {bedomning}")
    else:
        ok(f"Bedömningsdatum: {bedomning}")
    if uppdaterad is None:
        fel_rad("Senast uppdaterad saknas (”Redogörelsen uppdaterades senast den …”)")
    elif not re.fullmatch(DATUM, uppdaterad):
        fel_rad(f"Senast uppdaterad inte i ÅÅÅÅ-MM-DD: {uppdaterad}")
    elif bedomning and re.fullmatch(DATUM, bedomning) and bedomning > uppdaterad:
        fel_rad(f"Bedömningsdatum ({bedomning}) ligger efter senast uppdaterad ({uppdaterad})")
    else:
        ok(f"Senast uppdaterad: {uppdaterad}")

    # 5. Bristavsnittet och dess tre underavsnitt
    brister = hitta(rub, "Innehåll som inte är tillgängligt", rader)
    frost = hitta(rub, "Bristande förenlighet", rader)
    oskaligt = hitta(rub, "Oskäligt betungande", rader)
    nionde = hitta(rub, "Innehåll som inte omfattas av lagen", rader)

    if grad == "helt":
        if not re.search(r"inget känt innehåll|inga kända brister", text, re.I):
            fel_rad("Följsamheten är helt, men ingen mening om inga kända brister finns")
        if frost or oskaligt:
            fel_rad("Följsamheten är helt, men bristavsnitt/12 §-avsnitt finns kvar")
        if frost is None and oskaligt is None:
            ok("Helt förenlig utan bristförteckning")
    else:
        if frost is None:
            fel_rad("Underavsnittet ”Bristande förenlighet med lagkraven” saknas")
        else:
            situationsrubriker = [r for r in rub
                                  if r.niva == 4 and r.titel.lower().startswith("problem vid")]
            tomma = [r.titel for r in situationsrubriker if not listpunkter(r.text(rader))]
            if not situationsrubriker:
                fel_rad("Ingen H4-rubrik ”Problem vid användning …” under bristförteckningen")
            elif tomma:
                fel_rad(f"Användningssituationer utan bristpunkter: {', '.join(tomma)}")
            else:
                punkter = [p for r in situationsrubriker for p in listpunkter(r.text(rader))]
                utan = [p for p in punkter if not KRITERIUM.search(p)]
                ok(f"Bristförteckning: {len(situationsrubriker)} situationer, {len(punkter)} punkter")
                if utan:
                    varning(f"{len(utan)} bristpunkt" + ("" if len(utan) == 1 else "er")
                            + " utan hänvisning till WCAG/EN 301 549-kriterium")

    # 6. 12 §-undantaget ska redovisa sin bedömning
    if oskaligt is not None:
        avsnitt = oskaligt.text(rader)
        if "Bedömning" not in avsnitt:
            fel_rad("12 §-avsnittet saknar redovisad bedömning (raden ”Bedömning: …”)")
        elif not listpunkter(avsnitt) and "följande innehåll" not in avsnitt:
            fel_rad("12 §-avsnittet saknar förteckning över undantaget innehåll")
        else:
            ok("12 §-avsnitt med redovisad bedömning")

    if nionde is not None:
        avsnitt = nionde.text(rader)
        if not listpunkter(avsnitt) and not re.search(r"[a-zA-ZåäöÅÄÖ]", avsnitt):
            varning("9 §-avsnittet är tomt – ta bort det om inget innehåll undantas")

    # 7. Meddelandefunktionen: formulärlänk + e-post
    for fragment, etikett in (("Vad kan du göra", "Begäran om tillgängliggörande"),
                              ("Rapportera brister", "Rapportera brister")):
        avsnitt = hitta(rub, fragment, rader)
        if avsnitt is None:
            continue  # redan rapporterat som saknad rubrik
        if not re.search(LANK, avsnitt.text(rader)):
            fel_rad(f"{etikett}: ingen formulärlänk i avsnittet")
        else:
            ok(f"{etikett}: formulärlänk finns")
    kontakt = hitta(rub, "Vad kan du göra", rader)
    if kontakt is not None and not re.search(EPOST, kontakt.text(rader)):
        varning("Ingen e-postadress i kontaktavsnittet")

    # 8. Tillsyn och anmälningslänk till Digg
    tillsyn = hitta(rub, "Tillsyn", rader)
    if tillsyn is None:
        pass  # redan rapporterat som saknad rubrik
    else:
        avsnitt = tillsyn.text(rader)
        if "Digg" not in avsnitt:
            fel_rad("Tillsynsblocket nämner inte Digg")
        elif not re.search(r"digg\.se/tdosanmalan", avsnitt):
            fel_rad("Tillsynsblocket saknar länk till digg.se/tdosanmalan")
        else:
            ok("Tillsynsblock med anmälningslänk till Digg")

    # 9. App: versionsrad och datum för offentliggörande
    if app:
        if not re.search(r"version", text, re.I):
            varning("Appredogörelsen anger ingen version")
        off = datum_efter("offentliggjord den")
        if off is not None and not re.fullmatch(DATUM, off):
            fel_rad(f"Offentliggjort datum inte i ÅÅÅÅ-MM-DD: {off}")

    print("\n".join(rapport))
    varningstext = f"{varningar} varning" + ("ar" if varningar != 1 else "")
    if fel:
        print(f"BRISTER – {fel} fel, {varningstext}; rätta och kör igen")
        return 1
    print(f"KLAR – 0 fel, {varningstext}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
