# tillganglighetsredogorelse – tillgänglighetsredogörelser för AI-agenter

tillganglighetsredogorelse är en agent skill som skriver, uppdaterar och kontrollerar svenska tillgänglighetsredogörelser enligt lagen om tillgänglighet till digital offentlig service (DOS-lagen). Den vänder sig till dig som arbetar på en myndighet eller annan offentlig aktör som ska publicera en redogörelse för en webbplats, e-tjänst eller app – utifrån ett granskningsunderlag, med kraven maskinellt verifierade.

## Vad skillen gör

| Läge | Vad du får |
|---|---|
| Utkast | En färdig redogörelse enligt Diggs mall, från ditt underlag eller en granskningsrapport |
| Uppdatera | Befintlig redogörelse uppdaterad – nya brister, nya datum, ändrad följsamhet |
| Kontrollera | Kravkontroll av en färdig redogörelse: vad som saknas, bryter mot eller luktar illa |

Tre saker skiljer tillganglighetsredogorelse från en vanlig prompt:

1. **Kraven kontrolleras maskinellt.** Efter varje utkast kör ett skript en syntaktisk kontroll mot MDFFS 2019:2 §6 och Diggs vägledning: obligatoriska rubriker, följsamhetsgrad med exakt ord (helt, delvis eller inte), datumformat och datumordning, formulärlänk, anmälningslänk till Digg, inga kvarvarande platshållare. En redogörelse som inte klarar kontrollen lämns inte ut.
2. **Svenskt regelverk, svensk mall.** Strukturen följer Diggs officiella Word-mallar för webbplats och app – rubriklydelse, avsnittsordning, de tre bristkategorierna (bristande förenlighet, oskäligt betungande anpassning 12 §, innehåll utanför lagen 9 §) och Diggs tio användningssituationer. Kraven är spårbara till lag, föreskrift och vägledning i `references/krav-och-kallor.md`.
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
- ”Kontrollera redogorelsen i doc/tillganglighet.md mot lagkraven”
- ”Gör en tillgänglighetsredogörelse för vår app” (skillen använder då appmallen)

Skillen frågar efter det underlag som saknas – följsamhetsgrad, brister, datum, kontaktvägar – i en enda konsoliderad frågerunda, och föreslår ett avslutande klarspråkspass (t.ex. med [klarsprak-skill](https://github.com/pattespatte/klarsprak-skill)).

## Vad som finns i repot

```
SKILL.md                          Skillens instruktioner
scripts/kontrollera.py            Maskinell kravkontroll (python 3, enbart standardbiblioteket)
references/mall-webbplats.md      Mall för webbplatser och e-tjänster, efter Diggs Word-mall
references/mall-app.md            Mall för mobilapplikationer, efter Diggs Word-mall
references/krav-och-kallor.md     Kravmappning: mallavsnitt ↔ MDFFS 2019:2 §6 ↔ Digg-vägledning
references/wcag-till-situation.md WCAG/EN 301 549/axe-fynd → användningssituation → bristtext
```

Kontrollskriptet kan köras fristående:

    python3 scripts/kontrollera.py tillganglighetsredogorelse.md [--app]

## Källor

- [Digg – Skapa en tillgänglighetsredogörelse](https://www.digg.se/kunskap-och-stod/digital-tillganglighet/skapa-en-tillganglighetsredogorelse) med officiella Word-mallar
- [MDFFS 2019:2, konsoliderad version](https://www.digg.se/om-oss/forfattningssamling/foreskrifter-om-tillganglighet-till-digital-offentlig-service-mdffs-20192/konsoliderad-version)
- [DOS-lagen (2018:1937)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20181937-om-tillganglighet-till-digital_sfs-2018-1937/)
- [Anmäl bristande tillgänglighet till Digg](https://www.digg.se/tdosanmalan)

## Licens

[MIT](LICENSE) © pattespatte
