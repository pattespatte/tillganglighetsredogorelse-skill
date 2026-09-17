# tillganglighetsredogorelse – tillgänglighetsredogörelser för AI-agenter

[![skills.sh](https://skills.sh/b/pattespatte/tillganglighetsredogorelse-skill)](https://skills.sh/pattespatte/tillganglighetsredogorelse-skill)

tillganglighetsredogorelse är en agent skill som skriver, uppdaterar och kontrollerar svenska tillgänglighetsdokument enligt två lagar: tillgänglighetsredogörelser enligt lagen om tillgänglighet till digital offentlig service (DOS-lagen) för myndigheter och andra offentliga aktörer, och information om tjänstens tillgänglighet enligt lagen (2023:254) om vissa produkters och tjänsters tillgänglighet för leverantörer av konsumenttjänster – e-handel, banktjänster, elektronisk kommunikation, passagerartransport, e-böcker och tv-tjänster. Den vänder sig till dig som ska publicera ett sådant dokument för en webbplats, e-tjänst eller app – utifrån ett granskningsunderlag, med kraven maskinellt verifierade.

## Vad skillen gör

| Läge | Vad du får |
|---|---|
| Utkast | En färdig redogörelse enligt Diggs mall, eller tillgänglighetsinformation enligt PTS vägledning, från ditt underlag eller en granskningsrapport |
| Uppdatera | Befintligt dokument uppdaterat – nya brister, nya datum, ändrad följsamhet |
| Kontrollera | Kontroll av ett färdigt dokument: vad som saknas eller kan göras mer tillgängligt |

Tre saker skiljer tillganglighetsredogorelse från en vanlig prompt:

1. **Kraven kontrolleras maskinellt.** Efter varje utkast kör ett skript en syntaktisk kontroll: obligatoriska rubriker, datumformat och datumordning och inga kvarvarande platshållare – och enligt DOS-lagen dessutom följsamhetsgrad med exakt ord (helt, delvis eller inte), formulärlänk och anmälningslänk till Digg. Enligt tillgänglighetslagen kontrolleras i stället att 7 §-undantag redovisas med krav och motivering. Ett dokument som inte klarar kontrollen godkänns inte.
2. **Svenskt regelverk, svensk mall.** Enligt DOS-lagen följer strukturen Diggs officiella Word-mallar för webbplats och app – rubriklydelse, avsnittsordning, de tre bristkategorierna (bristande förenlighet, oskäligt betungande anpassning 12 §, innehåll utanför lagen 9 §) och Diggs tio användningssituationer. Enligt tillgänglighetslagen (2023:254), som saknar föreskriven mall, följer informationen PTS vägledning om innehållet i 25 §. Kraven är spårbara till lagar, föreskrifter och vägledningar i `references/krav-och-kallor.md`.
3. **Skillen testar inte tillgänglighet.** Granskningsunderlaget – automatiska verktyg, manuell testning, konsult – är inmatning, inte något skillen alstrar. Därmed hittar den inte på fakta: datum, brister och följsamhetsgrad kommer alltid från ditt underlag, och utkastet kräver mänskligt sign-off före publicering.

Granskningsrapporter med WCAG-kriterier, EN 301 549-klausuler eller axe-regelnamn översätts till användarvänliga bristtexter per användningssituation via en mappningstabell i `references/wcag-till-situation.md`.

## Installation

Skillen följer Agent Skills-standarden (en katalog med en `SKILL.md`) och fungerar i agenter som stödjer den, till exempel Claude Code, Cursor, Codex och ZCode. Det enda kravet är python 3 – skriptet använder ingenting utom standardbiblioteket.

Alla agenter via [skills](https://skills.sh)-CLI:

    npx skills add pattespatte/tillganglighetsredogorelse-skill

Claude Code, klonad:

    git clone https://github.com/pattespatte/tillganglighetsredogorelse-skill.git ~/.claude/skills/tillganglighetsredogorelse

ZCode, klonad:

    git clone https://github.com/pattespatte/tillganglighetsredogorelse-skill.git ~/.agents/skills/tillganglighetsredogorelse

## Användning

Be agenten använda skillen, till exempel:

- ”Skapa en tillgänglighetsredogörelse för webbplatsen X med hjälp av granskningsrapporten rapport.md”
- ”Uppdatera tillganglighetsredogorelse.md – vi har åtgärdat kontrastbristerna och gjort en ny granskning”
- ”Kontrollera redogörelsen i doc/tillganglighet.md mot lagkraven”
- ”Gör en tillgänglighetsredogörelse för vår app” (skillen använder då appmallen)
- ”Skriv tillgänglighetsinformationen för vår e-handel – här är granskningsrapporten” (skillen använder då mallen för tillgänglighetslagen 2023:254)

Skillen avgör först vilken lag som gäller – offentlig aktör ger DOS-lagen, konsumenttjänst inom e-handel, bank, kommunikation, transport, e-böcker eller tv ger tillgänglighetslagen – och frågar sedan efter det underlag som saknas, i en enda konsoliderad frågerunda. Den föreslår ett avslutande klarspråkspass (t.ex. med [klarsprak-skill](https://github.com/pattespatte/klarsprak-skill)).

## Vad som finns i repot

```
SKILL.md                          Skillens instruktioner
scripts/kontrollera.py            Maskinell kravkontroll (python 3, enbart standardbiblioteket)
references/mall-webbplats.md      Mall för webbplatser och e-tjänster, efter Diggs Word-mall
references/mall-app.md            Mall för mobilapplikationer, efter Diggs Word-mall
references/mall-lptt.md           Mall för information om tjänstens tillgänglighet enligt tillgänglighetslagen
references/krav-och-kallor.md     Kravmappning: mallavsnitt ↔ MDFFS 2019:2 §6 ↔ Digg-vägledning, och tillgänglighetslagens krav
references/wcag-till-situation.md WCAG/EN 301 549/axe-fynd → användningssituation → bristtext
```

Kontrollskriptet kan köras fristående:

    python3 scripts/kontrollera.py tillganglighetsredogorelse.md [--app] [--lptt]

## Källor

- [Digg – Skapa en tillgänglighetsredogörelse](https://www.digg.se/kunskap-och-stod/digital-tillganglighet/skapa-en-tillganglighetsredogorelse) med officiella Word-mallar
- [MDFFS 2019:2, konsoliderad version](https://www.digg.se/om-oss/forfattningssamling/foreskrifter-om-tillganglighet-till-digital-offentlig-service-mdffs-20192/konsoliderad-version)
- [DOS-lagen (2018:1937)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20181937-om-tillganglighet-till-digital_sfs-2018-1937/)
- [Anmäl bristande tillgänglighet till Digg](https://www.digg.se/tdosanmalan)
- [PTS – lagen om vissa produkters och tjänsters tillgänglighet](https://pts.se/digital-inkludering/lagen-om-vissa-produkters-och-tjansters-tillganglighet/)
- [PTS – Information om tjänstens tillgänglighet](https://pts.se/digital-inkludering/lagen-om-vissa-produkters-och-tjansters-tillganglighet/information-om-tjanstens-tillganglighet/)
- [Lag (2023:254) om vissa produkters och tjänsters tillgänglighet](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2023254-om-vissa-produkters-och-tjansters_sfs-2023-254/)
- [Förordning (2023:676) om vissa produkters och tjänsters tillgänglighet](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-2023676-om-vissa-produkters-och_sfs-2023-676/)

## Licens

[MIT](LICENSE) © pattespatte
