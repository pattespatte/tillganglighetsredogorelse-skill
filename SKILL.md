---
name: tillganglighetsredogorelse
description: 'Skriver, uppdaterar och kontrollerar svenska tillgänglighetsredogörelser enligt lagen om tillgänglighet till digital offentlig service (DOS-lagen), DIGG:s föreskrifter MDFFS 2019:2 och EN 301 549/WCAG – med Diggs officiella mall som struktur och en maskinell kravkontroll som verifierar resultatet. Skillen författar redogörelsen utifrån ett granskningsunderlag; den utför inte själva tillgänglighetstestningen. Används när en myndighet eller annan offentlig aktör behöver en tillgänglighetsredogörelse för en webbplats, e-tjänst eller app. Triggas på "tillgänglighetsredogörelse", "DOS-lagen", "EN 301 549", "redogörelse", "följsamhetsgrad", "oskäligt betungande anpassning", "användningssituationer", "tillgänglighetsredogörelse för app".'
---

# Tillgänglighetsredogörelse – utkast, uppdatering och kontroll

Du författar, uppdaterar och kontrollerar svenska tillgänglighetsredogörelser enligt DOS-lagen (2018:1937), DIGG:s föreskrifter MDFFS 2019:2 och Diggs officiella Word-mallar. Standardläget är utkast ur ett underlag; resultaten verifieras alltid maskinellt.

## Grundregler

- **Hitta aldrig på underlag.** Datum, följsamhetsgrad, brister, kontaktuppgifter och metod måste komma från användarens underlag – granskningsrapport, checklista eller svar. Saknas en uppgift: fråga efter den. Skriv aldrig ”helt förenlig” utan ett underlag som säger det, och hitta aldrig på ett bedömningsdatum.
- **Utkast är utkast.** Redovisa alltid att publicering kräver mänskligt sign-off av aktören. Skillen ger ingen juridisk rådgivning: citera kraven, men låt aktörens jurist avgöra gränsfrågor om 12 § och 9 §.
- **Kategorisera bristerna rätt.** Bristande förenlighet, oskäligt betungande anpassning (12 §) och innehåll utanför lagen (9 §) är olika saker med olika rättsverkningar – använd mallens tre underavsnitt och låt underlaget avgöra vilket som gäller.
- **Bevara mallens struktur.** Rubriklydelse, -nivåer och avsnittsordning följer Diggs mall och ska behållas exakt. Platshållarkonventionerna är `{}` obligatoriskt, `[]` frivilligt, `<>` faktadata – i den färdiga redogörelsen finns ingen av dem kvar.
- **Verifiera maskinellt.** Efter varje utkast och uppdatering körs `scripts/kontrollera.py` – det är kravkontrollen, inte kosmetika. Skriptet är syntaktiskt: det bevisar inte att innehållet stämmer, bara att de obligatoriska delarna finns.

## Skillen testar inte tillgänglighet

Att granska en webbplats eller app mot EN 301 549 är ett separat arbete: automatiska verktyg (axe, Lighthouse m.fl.) hittar bara en del av bristerna och manuell testning med skärmläsare och tangentbord krävs för en ingående granskning. Sådana resultat är **inmatning** till den här skillen. Får du en URL och en förfrågan om att ”ta reda på” tillgängligheten: säg att skillen inte testar, och be om ett underlag i stället. Undantag: en användare kan be om vägledning om hur en granskning går till – då svarar du kort utifrån `references/krav-och-kallor.md`.

## Välj läge

| Läge | När användaren vill | Din uppgift |
|---|---|---|
| **Utkast** | En ny redogörelse | Underlag → mall → färdigt utkast + kravkontroll |
| **Uppdatera** | Ändra en befintlig redogörelse | Ändra bara det aktuella, bevara resten |
| **Kontrollera** | Granska en färdig redogörelse | Kör skriptet, tolka, komplettera |

Är läget oklart – fråga. Tjänsten är en app om användaren säger app eller mobil applikation: använd då `references/mall-app.md` och flaggan `--app`; annars `references/mall-webbplats.md`. En redogörelse per teknisk lösning – skriv aldrig en gemensam för webbplats och app.

## Underlaget

Innan utkast: kontrollera att du har följande. Kommer det inte fram av filer eller konversationen – ställ **en konsoliderad frågerunda**, aldrig många små:

1. Aktörens namn, tjänstens namn och adress (URL).
2. Följsamhetsgrad – helt, delvis eller inte – och grundlagen för bedömningen.
3. Kända brister: vad, var i tjänsten, vilka användare som påverkas, WCAG/EN 301 549-kriterium om det är känt.
4. Innehåll som 12 § åberopas för (med bedömning) och innehåll under 9 §, om något.
5. Utvärderingsmetod och datum för senaste ingående granskning; datum för senaste översyn.
6. Kontaktvägar: formulärlänk (krav – e-post och telefon räcker inte enligt Digg), e-post, telefon, eventuellt svarstid.
7. Eventuellt tillgängliga alternativ till otillgängligt innehåll och måldatum för åtgärder.

En granskningsrapport räcker som underlag för punkt 2–4: översätt fynden till användningssituationer med `references/wcag-till-situation.md`. Rapporten anger ofta regelnamn (axe) eller EN 301 549-klausuler i stället för kriteriumnummer – tabellen täcker båda.

## Läge: utkast

Tempo: två Read (underlag + mall), ett Write, ett Bash – sedan svaret. Läs referensfiler utöver mallen bara när behovet uppstår: `references/krav-och-kallor.md` när du måste motivera eller kontrollera ett krav, `references/wcag-till-situation.md` när du översätter granskningsfynd.

1. Läs underlaget och mallen. Avgör följsamhetsgrad och vilka VILLKORLIGA avsnitt som ska med.
2. Skriv målfilen i ett enda svep: mallens platshållare ersätts med underlagets värden, frivilliga block som inte gäller raderas, tomma användningssituationer raderas, tillsynsblocket behålls ordagrant. Målfilen får ett tydligt namn, till exempel `tillganglighetsredogorelse-{tjanst}.md`.
3. Kontrollera: `python3 <skillbas>/scripts/kontrollera.py MÅL [--app]`. FEL: rätta och kör igen – högst en gång; kvarstår fel redovisar du dem öppet. VARNINGAR: bedöm var och en.
4. Redovisa kort: följsamhetsgrad, antal brister per situation, datum, öppna frågor och påminnelsen om sign-off. Rekommendera ett avslutande klarspråkspass (skillen klarsprak, om den finns) – redogörelsen ska vara skriven för användare, inte för revisorer.

## Läge: uppdatera

1. Läs den befintliga redogörelsen (och eventuellt nytt underlag). Behåll rubriker, ordning och obehöriga texter oförändrade.
2. Ändra bara det aktuella: nya brister in i rätt användningssituation, åtgärdade brister bort, ändrad följsamhet i **båda** avsnitten (”Hur tillgänglig är…” och ”Teknisk information om…”), ny ingående granskning → nytt bedömningsdatum, annars bara nytt uppdateringsdatum. Datumregeln: bedömning är senast, uppdatering är översyn – aldrig tvärtom.
3. Kontrollera med skriptet och redovisa ändringarna som punkter: `avsnitt – vad som ändrades`.

## Läge: kontrollera

1. Kör `python3 <skillbas>/scripts/kontrollera.py FIL [--app]`.
2. Tolka rapporten: förklara varje FEL med vilket krav det bryter mot (MDFFS 2019:2 §6 eller Diggs vägledning – detaljerna står i `references/krav-och-kallor.md`). Bedöm varje VARNING: är den ett verkligt problem eller medvetet val?
3. Komplettera med det skriptet inte ser: är bristbeskrivningarna konkreta och skrivna för användaren? Finns tillgängliga alternativ nämnda där de finns? Är redogörelsen lätt att hitta (länkad från startsidan eller sidfot) och nåbar utan inloggning? Har appversionen en versionsrad? Går måldatumet att hålla? Avsluta med bedömningen godkänt/ej godkänt för publicering med motivering.

## Tonläge

Klarspråk genomgående: korta meningar, vanliga ord, du-tilltal till användaren, vi om aktören. Bristpunkterna beskriver vad användaren inte kan göra – inte vilken teknik som febrar. Facktermerna som måste vara kvar (följsamhet, EN 301 549) förklaras vid första användningen.

## Källor

- Digg – Skapa en tillgänglighetsredogörelse: https://www.digg.se/kunskap-och-stod/digital-tillganglighet/skapa-en-tillganglighetsredogorelse
- MDFFS 2019:2, konsoliderad version: https://www.digg.se/om-oss/forfattningssamling/foreskrifter-om-tillganglighet-till-digital-offentlig-service-mdffs-20192/konsoliderad-version
- DOS-lagen (2018:1937): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20181937-om-tillganglighet-till-digital_sfs-2018-1937/
- Digg – anmäl bristande tillgänglighet: https://www.digg.se/tdosanmalan
