---
name: tillganglighetsredogorelse
description: 'Skriver, uppdaterar och kontrollerar svenska tillgänglighetsredogörelser enligt DOS-lagen (2018:1937) med Diggs officiella mallar, samt information om tjänstens tillgänglighet enligt tillgänglighetslagen (2023:254) med PTS vägledning – båda med EN 301 549/WCAG som teknisk grund och maskinell kravkontroll. Skillen författar utifrån ett granskningsunderlag; den utför inte själva tillgänglighetstestningen. Används när en offentlig aktör behöver en tillgänglighetsredogörelse för en webbplats, e-tjänst eller app, eller när en leverantör av konsumenttjänster – e-handel, banktjänster, elektronisk kommunikation, passagerartransport, e-böcker eller tv-tjänster – behöver tillgänglighetsinformation. Triggas på tillgänglighetsredogörelse, DOS-lagen, tillgänglighetslagen, LPTT, 2023:254, EN 301 549, följsamhetsgrad, oskäligt betungande anpassning, oproportionerligt stor börda, användningssituationer, tillgänglighetsinformation.'
---

# Tillgänglighetsredogörelse och tillgänglighetsinformation – utkast, uppdatering och kontroll

Du författar, uppdaterar och kontrollerar svenska tillgänglighetsdokument enligt två lagar: tillgänglighetsredogörelser enligt DOS-lagen (2018:1937), DIGG:s föreskrifter MDFFS 2019:2 och Diggs officiella Word-mallar, och information om tjänstens tillgänglighet enligt lagen (2023:254) om vissa produkters och tjänsters tillgänglighet (tillgänglighetslagen) med PTS vägledning som förebild. Standardläget är utkast ur ett underlag; resultaten verifieras alltid maskinellt.

## Grundregler

- **Hitta aldrig på underlag.** Datum, följsamhetsgrad, brister, kontaktuppgifter och metod måste komma från användarens underlag – granskningsrapport, checklista eller svar. Saknas en uppgift: fråga efter den. Skriv aldrig ”helt förenlig” utan ett underlag som säger det, och hitta aldrig på ett bedömningsdatum.
- **Utkast är utkast.** Redovisa alltid att publicering kräver mänskligt sign-off av aktören. Skillen ger ingen juridisk rådgivning: citera kraven, men låt aktörens jurist avgöra gränsfrågor om undantagen – 12 § och 9 § i DOS-lagen, 7 § i tillgänglighetslagen.
- **Kategorisera bristerna rätt.** Bristande förenlighet, undantag (12 § DOS-lagen respektive 7 § tillgänglighetslagen) och innehåll utanför lagen (9 § respektive 5 §) är olika saker med olika rättsverkningar – använd mallens underavsnitt och låt underlaget avgöra vilket som gäller.
- **Bevara mallens struktur.** Rubriklydelse, -nivåer och avsnittsordning följer mallen – Diggs Word-mallar under DOS-lagen, PTS vägledning under tillgänglighetslagen – och ska behållas exakt. Platshållarkonventionerna är `{}` obligatoriskt, `[]` frivilligt, `<>` faktadata – i det färdiga dokumentet finns ingen av dem kvar.
- **Verifiera maskinellt.** Efter varje utkast och uppdatering körs `scripts/kontrollera.py` – det är kravkontrollen, inte kosmetika. Skriptet är syntaktiskt: det bevisar inte att innehållet stämmer, bara att de obligatoriska delarna finns.

## Skillen testar inte tillgänglighet

Att granska en webbplats eller app mot EN 301 549 är ett separat arbete: automatiska verktyg (axe, Lighthouse m.fl.) hittar bara en del av bristerna och manuell testning med skärmläsare och tangentbord krävs för en ingående granskning. Sådana resultat är **inmatning** till den här skillen. Får du en URL och en förfrågan om att ”ta reda på” tillgängligheten: säg att skillen inte testar, och be om ett underlag i stället. Undantag: en användare kan be om vägledning om hur en granskning går till – då svarar du kort utifrån `references/krav-och-kallor.md`.

## Avgör vilket regelverk som gäller

Två lagar kan vara aktuella, med olika tillämpningsområden – avgör vilken som gäller innan du väljer mall:

- **Offentlig aktör** (myndighet, kommun, region m.fl.) med webbplats, e-tjänst eller app → **DOS-lagen (2018:1937)**. Använd `references/mall-webbplats.md` eller `references/mall-app.md` och kontrollera utan flagga eller med `--app`.
- **Tjänst mot konsumenter** inom något av områdena i 4 § tillgänglighetslagen (2023:254) – e-handel, banktjänster, elektronisk kommunikation, passagerartransport, e-böcker eller åtkomst till audiovisuella medietjänster → **tillgänglighetslagen**, oavsett om aktören är offentlig eller privat. Använd `references/mall-lptt.md` och kontrollera med `--lptt`. Dokumentet kallas information om tjänstens tillgänglighet – lagen kräver ingen redogörelse enligt Diggs mall.
- **Mikroföretag** (färre än tio anställda och högst 2 miljoner euro i årsomsättning eller balansomslutning): tjänster undantas från tillgänglighetslagens krav (10 §). Påpeka det om det är aktuellt – men avgör inte själv om undantaget gäller.
- **Fysiska produkter** (3 §) omfattas av tillgänglighetslagen men följer ett annat flöde: teknisk bedömning, EU-försäkran om överensstämmelse och CE-märkning (11–12 §§). Säg att skillen inte stödjer det och hänvisa till PTS vägledning.
- En aktör kan omfattas av båda lagarna för olika tjänster – skriv ett dokument per tjänst, enligt respektive lag. Detaljerna står i `references/krav-och-kallor.md`; gränsfall avgör aktörens jurist.

## Välj läge

| Läge | När användaren vill | Din uppgift |
|---|---|---|
| **Utkast** | En ny redogörelse | Underlag → mall → färdigt utkast + kravkontroll |
| **Uppdatera** | Ändra en befintlig redogörelse | Ändra bara det aktuella, bevara resten |
| **Kontrollera** | Granska en färdig redogörelse | Kör skriptet, tolka, komplettera |

Är läget oklart – fråga. Under DOS-lagen: tjänsten är en app om användaren säger app eller mobil applikation – använd då `references/mall-app.md` och flaggan `--app`; annars `references/mall-webbplats.md`. En redogörelse per teknisk lösning – skriv aldrig en gemensam för webbplats och app. Under tillgänglighetslagen gäller `references/mall-lptt.md` för hela tjänsten – en webbutik och dess app är en tjänst med en information.

## Underlaget

Innan utkast: kontrollera att du har följande. Kommer det inte fram av filer eller konversationen – ställ **en konsoliderad frågerunda**, aldrig många små:

1. Aktörens namn, tjänstens namn och adress (URL) – enligt tillgänglighetslagen även vilket tjänsteområde tjänsten tillhör, eftersom det styr tillsynsmyndigheten.
2. Följsamhetsgrad enligt DOS-lagen – helt, delvis eller inte – och grundlagen för bedömningen. Eller, enligt tillgänglighetslagen, hur kraven uppfylls: följs standarden EN 301 549, eller beskrivs det på annat sätt?
3. Kända brister: vad, var i tjänsten, vilka användare som påverkas, WCAG/EN 301 549-kriterium om det är känt.
4. Undantag: innehåll som 12 § åberopas för (med bedömning) och innehåll under 9 § (DOS-lagen) – eller 7 §-undantag enligt tillgänglighetslagen, med vilka krav det gäller och besked om att myndigheten underrättats (8 §).
5. Utvärderingsmetod och datum för senaste ingående granskning; datum för senaste översyn. Enligt tillgänglighetslagen är datumen god praxis, inte krav.
6. Kontaktvägar: formulärlänk (krav enligt Digg under DOS-lagen – e-post och telefon räcker inte), e-post, telefon, eventuellt svarstid.
7. Eventuellt tillgängliga alternativ till otillgängligt innehåll och måldatum för åtgärder.

En granskningsrapport räcker som underlag för punkt 2–4: översätt fynden till användningssituationer med `references/wcag-till-situation.md`. Rapporten anger ofta regelnamn (axe) eller EN 301 549-klausuler i stället för kriteriumnummer – tabellen täcker båda.

## Läge: utkast

Tempo: två Read (underlag + mall), ett Write, ett Bash – sedan svaret. Läs referensfiler utöver mallen bara när behovet uppstår: `references/krav-och-kallor.md` när du måste motivera eller kontrollera ett krav, `references/wcag-till-situation.md` när du översätter granskningsfynd.

1. Läs underlaget och mallen. Avgör följsamhetsgraden (DOS-lagen) respektive hur kraven uppfylls (tillgänglighetslagen) och vilka VILLKORLIGA avsnitt som ska med.
2. Skriv målfilen i ett enda svep: mallens platshållare ersätts med underlagets värden, frivilliga block som inte gäller raderas, tomma användningssituationer raderas, tillsynsblocket behålls ordagrant under DOS-lagen och fylls med rätt myndighet under tillgänglighetslagen. Målfilen får ett tydligt namn, till exempel `tillganglighetsredogorelse-{tjanst}.md` eller, enligt tillgänglighetslagen, `tillganglighetsinformation-{tjanst}.md`.
3. Kontrollera: `python3 <skillbas>/scripts/kontrollera.py MÅL [--app] [--lptt]` – ingen flagga för DOS-webbplatser, `--app` för DOS-appar, `--lptt` för tillgänglighetslagen. FEL: rätta och kör igen – högst en gång; kvarstår fel redovisar du dem öppet. VARNINGAR: bedöm var och en.
4. Redovisa kort: följsamhetsgrad, antal brister per situation, datum, öppna frågor och påminnelsen om sign-off. Rekommendera ett avslutande klarspråkspass (skillen klarsprak, om den finns) – redogörelsen ska vara skriven för användare, inte för revisorer.

## Läge: uppdatera

1. Läs den befintliga redogörelsen (och eventuellt nytt underlag). Behåll rubriker, ordning och obehöriga texter oförändrade.
2. Ändra bara det aktuella: nya brister in i rätt användningssituation, åtgärdade brister bort, ändrad följsamhet i **båda** avsnitten (”Hur tillgänglig är…” och ”Teknisk information om…”), ny ingående granskning → nytt bedömningsdatum, annars bara nytt uppdateringsdatum. Datumregeln: bedömning är senast, uppdatering är översyn – aldrig tvärtom.
3. Kontrollera med skriptet och redovisa ändringarna som punkter: `avsnitt – vad som ändrades`.

## Läge: kontrollera

1. Kör `python3 <skillbas>/scripts/kontrollera.py FIL [--app] [--lptt]`.
2. Tolka rapporten: förklara varje FEL med vilket krav det bryter mot – MDFFS 2019:2 §6 och Diggs vägledning enligt DOS-lagen, 25 § lagen och PTS vägledning enligt tillgänglighetslagen. Detaljerna står i `references/krav-och-kallor.md`. Bedöm varje VARNING: är den ett verkligt problem eller medvetet val?
3. Komplettera med det skriptet inte ser: är bristbeskrivningarna konkreta och skrivna för användaren? Finns tillgängliga alternativ nämnda där de finns? Är dokumentet lätt att hitta (länkat från startsidan eller sidfot) och nåbart utan inloggning? Åtföljer det tjänsten enligt tillgänglighetslagen (de allmänna villkoren eller motsvarande)? Har appversionen en versionsrad? Går måldatumet att hålla? Avsluta med bedömningen godkänt/ej godkänt för publicering med motivering.

## Tonläge

Klarspråk genomgående: korta meningar, vanliga ord, du-tilltal till användaren, vi om aktören. Bristpunkterna beskriver vad användaren inte kan göra – inte vilken teknik som är problemet. Facktermerna som måste vara kvar (följsamhet, EN 301 549) förklaras vid första användningen.

## Källor

- Digg – Skapa en tillgänglighetsredogörelse: https://www.digg.se/kunskap-och-stod/digital-tillganglighet/skapa-en-tillganglighetsredogorelse
- MDFFS 2019:2, konsoliderad version: https://www.digg.se/om-oss/forfattningssamling/foreskrifter-om-tillganglighet-till-digital-offentlig-service-mdffs-20192/konsoliderad-version
- DOS-lagen (2018:1937): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20181937-om-tillganglighet-till-digital_sfs-2018-1937/
- Digg – anmäl bristande tillgänglighet: https://www.digg.se/tdosanmalan
- Lag (2023:254) om vissa produkters och tjänsters tillgänglighet: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2023254-om-vissa-produkters-och-tjansters_sfs-2023-254/
- PTS – lagen om vissa produkters och tjänsters tillgänglighet: https://pts.se/digital-inkludering/lagen-om-vissa-produkters-och-tjansters-tillganglighet/
- PTS – Information om tjänstens tillgänglighet: https://pts.se/digital-inkludering/lagen-om-vissa-produkters-och-tjansters-tillganglighet/information-om-tjanstens-tillganglighet/
