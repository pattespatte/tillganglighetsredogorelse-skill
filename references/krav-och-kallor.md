# Krav och källor – tillgänglighetsredogörelse och tillgänglighetsinformation

Referens för skillens lägen utkast och kontrollera: vad lagarna och tillsynsmyndigheterna kräver, var det står och var det hamnar i mallen. Först DOS-lagen för offentliga aktörer, därefter tillgänglighetslagen (2023:254) för konsumentinriktade tjänster – se slutet av filen för vad som skiljer lagarna åt i praktiken.

## Vilken lag gäller?

- **Offentlig aktör** (myndighet, kommun, region m.fl. enligt DOS-lagen) med webbplats, e-tjänst eller app → **DOS-lagen (2018:1937)**.
- **Tjänst som erbjuds till konsumenter** inom något av områdena i 4 § tillgänglighetslagen → **lagen (2023:254)**, oavsett aktörstyp. Det är tjänsten, inte organisationens form, som avgör.
- En och samma aktör kan omfattas av båda lagarna för olika tjänster – skriv då ett dokument per tjänst, enligt respektive lag.
- Tveksfall: låt aktören avgöra – fråga efter vad tjänsten är och vem den vänder sig till.

## DOS-lagen – regelverket i korthet

| Nivå | Författning | Roll |
|---|---|---|
| EU-direktiv | Direktiv (EU) 2016/2102 (Webbtillgänglighetsdirektivet) | Kräver tillgänglighetsredogörelse (art. 7) och modellredogörelse (kommissionens genomförandebeslut (EU) 2018/1524) |
| Lag | Lagen (2018:1937) om tillgänglighet till digital offentlig service (DOS-lagen) | Svensk genomförandelag. §§ 9, 12, 13, 15 är väsentliga här |
| Förordning | Förordning (2018:1938) om tillgänglighet till digital offentlig service | Utfyller lagen |
| Föreskrift | DIGG:s föreskrifter (MDFFS 2019:2) om tillgänglighet till digital offentlig service | Kraven på redogörelsens innehåll står i 6 §. Tekniskt krav: 4–5 §§ |
| Standard | EN 301 549 V3.2.1 (2021-03), bilaga A | Förenlighet med standarden medför presumtion att 4 § är uppfyllt (5 §). Bilaga A bygger på WCAG 2.1 nivå AA |

Tillsynsmyndighet: Myndigheten för digital förvaltning (Digg). Anmälningsfunktion: [digg.se/tdosanmalan](https://www.digg.se/tdosanmalan).

## MDFFS 2019:2, 6 § – kravinnehåll mot mallavsnitt

| 6 § punkt | Krav | Mallavsnitt (webbplats) |
|---|---|---|
| 1 | Namn på offentlig aktör samt den eller de webbplatser och mobila applikationer som redogörelsen avser | H1 + ingress |
| 2 | Redogörelse om tjänsten är helt, delvis eller inte förenlig med kraven i 4 § | ”Teknisk information om webbplatsens tillgänglighet” |
| 3 | Förteckning över innehåll som inte är tillgängligt, skälen, och i förekommande fall tillgängliga alternativ | ”Innehåll som inte är tillgängligt” (tre underavsnitt) |
| 4 | Datum för bedömningen, utvärderingsmetod och datum för senaste uppdateringen | ”Hur vi testat webbplatsen” |
| 5 | Meddelandefunktion (eller länk) för att meddela brister och begära tillgängliggörande | ”Vad kan du göra om du inte kan använda delar av webbplatsen?” och ”Rapportera brister i webbplatsens tillgänglighet” |
| 6 | Information om att brister kan anmälas till Digg, och länk till anmälningsfunktionen | ”Tillsyn” |

Utöver 6 § punkt 3–4 gäller, enligt Diggs vägledning: en **förteckning över tillgängliga alternativ** till otillgängligt innehåll ska med om sådana finns (skriv alternativet i anslutning till bristen), och **motiveringen** till åberopat undantag för oskäligt betungande anpassning ska redovisas (13 § DOS-lagen).

## DOS-lagen – paragrafer som redogörelsen rör

- **9 §** – innehåll som inte omfattas av lagen, till exempel dokument i äldre filformat publicerade före den 23 september 2018, kartor och kartscheman samt innehåll från tredje part som aktören inte kontrollerar. Sådant innehåll hör hemma i mallens tredje underavsnitt.
- **12 §** – undantag för oskäligt betungande anpassning. Bedömningen ska beakta konsekvenserna för personer med funktionsnedsättning samt uppskattade kostnader och fördelar.
- **13 §** – kravet på tillgänglighetsredogörelse (första stycket) och meddelandefunktionen (andra stycket). Meddelandefunktionen ska vara tillgänglig – Digg anger att ett formulär är ett sådant sätt, och att telefonnummer och e-postadresser är bra komplement men inte tillräckliga ensamma.
- **15 §** – rätten att begära tillgängliggörande av innehåll som undantagits; sådana begäranden ska kunna ställas via meddelandefunktionen.

## Digg – vägledning i korthet

- **Följsamhetsgrad:** redogörelsen ska ange om tjänsten som helhet är ”helt”, ”delvis” eller ”inte” förenlig. Undvik vaga formuleringar utan något av orden.
- **Bedömningsdatum:** datumet för den senaste **ingående granskning** som ligger till grund för hela redogörelsen. En ny ingående granskning efter publicering: ange det senare datumet.
- **Senast uppdaterad:** gäller den senaste **översynen**, även utan fullständig utvärdering. Digg rekommenderar översyn av aktualiteten minst en gång om året.
- **Uppdateringsfrekvens:** e-tjänst med produktionssättningar – vid varje produktionssättning. Webbplats med löpande publicering – flera gånger per år vid behov. Statisk webbplats – minst årligen. App – vid förändringar som påverkar tillgängligheten.
- **Placering:** tillgängligt format; länk tydligt på startsidan eller åtkomlig från alla sidor (sidfot). App: på aktörens webbplats eller där appen laddas ner – aldrig enbart i appen.
- **Inlogg:** Digg:s uppfattning är att redogörelsen ska kunna tas del av utan inloggning eller identifiering; en redogörelse bakom inloggning är inte ”lätt åtkomlig”.
- **Separata redogörelser:** en per teknisk lösning (webbplats respektive app) rekommenderas. Samma redogörelse för flera operativsystem är tillåten om det är tydligt vad som gäller vilket system.
- **Hänvisa inte till Diggs granskning** som utvärderingsunderlag – Digg gör begränsade stickprov vid tillsyn; en utvärdering som grund för redogörelsen kräver bredare urval.
- **Skicka inte in** redogörelsen till Digg – den publiceras hos aktören själv.

## Användningssituationer

Förteckna brister utifrån hur de påverkar användaren – inte utifrån tekniska kategorier. Situationerna kommer från Diggs vägledning men används i båda mallarna, även informationen enligt tillgänglighetslagen. De tio situationerna:

1. Användning utan synförmåga
2. Användning med nedsatt syn
3. Användning med nedsatt färgseende
4. Användning utan hörsel
5. Användning med nedsatt hörsel
6. Användning utan röstförmåga
7. Användning med nedsatt finmotorik eller styrka
8. Användning med nedsatt rörlighet
9. Användning vid känslighet för flimmer
10. Användning vid kognitiv nedsättning

## DOS-mallens medvetna avvikelser från Diggs Word-mall

| Avvikelse | Skäl |
|---|---|
| Datum som `ÅÅÅÅ-MM-DD` i stället för Word-mallens ”dag månad år” | Otvetydigt, sorteringsbart och maskinellt kontrollerbart |
| Uttrycklig raden ”Anmäl till Digg: digg.se/tdosanmalan” i tillsynsblocket | Kravet på länk till anmälningsfunktionen är uttryckligt (6 §); synlig textlänk är säkrast |
| Länk till tjänsten direkt under ingressen | Digg saknar den i mallen; den hjälper användaren och saknas ofta i publicerade redogörelser |
| WCAG-kriterium angivet i varje bristpunkt | Gör bristerna spårbara och kontrollerbara; Digg kräver ”detaljerad, fullständig och tydlig” förteckning med skäl |

## Tillgänglighetslagen (2023:254) – regelverket i korthet

| Nivå | Författning | Roll |
|---|---|---|
| EU-direktiv | Direktiv (EU) 2019/882 (tillgänglighetsdirektivet) | Kraven på produkter och tjänster; genomfört i Sverige från 2025-06-28 |
| Lag | Lagen (2023:254) om vissa produkters och tjänsters tillgänglighet (tillgänglighetslagen, LPTT) | Svensk genomförandelag. Nyckelbestämmelser här: 3–5, 7–10, 24–25 §§ |
| Förordning | Förordning (2023:676) om vissa produkters och tjänsters tillgänglighet | Tillgänglighetskraven i bilaga 1 (produkter) och bilaga 2 (tjänster). Informationens innehåll: 24 §. Tillsynsmyndigheterna utses i förordningen |
| Föreskrifter | PTSFS 2024:6 (tjänster) och PTSFS 2024:5 (produkter) | Post- och telestyrelsens kompletteringar inom dess tillsynsområde. 3–5 §§ PTSFS 2024:6 reglerar informationen, bland annat att den ska åtfölja tjänsten i de allmänna villkoren eller motsvarande |
| Standard | EN 301 549 | Ingen presumtion i DOS-lagens mening. 9 § lagen ger presumtion om överensstämmelse om en harmoniserad standard som hänvisats i EU:s officiella tidning följs; i avvaktan på det rekommenderar PTS att man tar ledning av EN 301 549 |

## Tillgänglighetslagen – tillämpningsområde

Lagen gäller inte aktörstyper utan produkter och tjänster. Tjänster (4 §) som är avsedda för konsumenter inom:

1. elektroniska kommunikationstjänster (undantaget maskin-till-maskin-överföring),
2. tjänster som ger åtkomst till audiovisuella medietjänster,
3. passagerartransport med buss, fartyg, luftfartyg och tåg – webbplatser, appar, e-biljetter, reseinformation och självserviceterminaler (stads-, förorts- och regionaltransporter omfattas bara av kraven på självserviceterminaler),
4. banktjänster för konsumenter,
5. e-böcker,
6. e-handelstjänster.

Produkter (3 §) mot konsumenter: datormaskinvarusystem och operativsystem, betalningsterminaler, kontantautomater, biljett- och incheckningsautomater, interaktiva självserviceterminaler, terminalutrustning för elektronisk kommunikation och för audiovisuella medietjänster, samt läsplattor. **Skillen stödjer inte produktflödet** – produkter kräver teknisk bedömning, EU-försäkran om överensstämmelse och CE-märkning (11–12 §§), vilket är en annan process än en redogörelse.

Undantag och begränsningar:

- **5 §** – innehåll utanför lagen: kartor (navigeringskartor om väsentlig information ges tillgängligt digitalt) och innehåll från tredje part som aktören varken finansierar, utvecklar eller kontrollerar. Det är tillgänglighetslagens motsvarighet till 9 § DOS-lagen.
- **10 §** – mikroföretag (färre än tio anställda och högst 2 miljoner euro i årsomsättning eller balansomslutning): tjänster behöver inte uppfylla tillgänglighetskraven. För produkter gäller kraven, men vissa administrativa skyldigheter är eftergivna.
- **Övergångsbestämmelser** – förinspelat tidsberoende media, filformat och arkiv publicerade före 2025-06-28 omfattas inte; tjänster får fortsätta tillhandahållas med produkter som lagligen användes före ikraftträdandet, och enligt avtal ingångna dessförinnan, dock längst t.o.m. 2030-06-27; självserviceterminaler får användas i 20 år.

## Tillgänglighetslagen – paragrafer som informationen rör

- **25 §** – tjänsteleverantören ska ta fram nödvändig information om hur tjänsten uppfyller tillgänglighetskraven. Åberopas undantag enligt 7 § ska det av informationen framgå vilka krav undantaget omfattar. Tjänsten ska åtföljas av informationen.
- **24 § förordningen** – informationen ska innehålla en redogörelse för de krav som är tillämpliga på tjänsten och, i den mån det behövs för att bedöma överensstämmelsen, en beskrivning av tjänstens utformning och funktion. Allmänheten ska ha tillgång till informationen i skriftlig och muntlig form, på ett tillgängligt sätt, och den ska sparas så länge tjänsten tillhandahålls.
- **PTS vägledning om innehållet:** beskrivning av tjänsten; vilka tillgänglighetskrav som är relevanta (EN 301 549 som ledning); hur kraven uppfylls – standard följs (presumtion) eller mer ingående egen beskrivning; vilka krav ett 7 §-undantag omfattar och varför; metoder för test och kvalitetssäkring.
- **7 §** – tillgänglighetskrav gäller inte om kravet innebär en större förändring av produktens eller tjänstens grundläggande karaktär eller medför en oproportionerligt stor börda. Har aktören tagit emot externa medel för tillgänglighetsarbetet får börde-undantaget inte åberopas.
- **8 §** – åberopat undantag ska dokumenteras, sparas med motivering och underrättas till marknadskontroll- eller tillsynsmyndigheten (för PTS:s områden via e-tjänsten LPTT-rapportering). Detta är en separat skyldighet utöver informationen till användarna.
- **24 § lagen** – tjänsteleverantören ska fortlöpande säkerställa att tjänsten uppfyller kraven. Upphör en tjänst att uppfylla dem ska bristen åtgärdas och tillsynsmyndigheterna underrättas – vid uppdatering av informationen: kontrollera att den fortfarande stämmer.

## Tillgänglighetslagen – tillsyn och sanktioner

| Myndighet | Tillsyn över |
|---|---|
| Post- och telestyrelsen (PTS) | Elektroniska kommunikationstjänster, banktjänster och e-handel. Därtill marknadskontroll av samtliga produkter och samordning mellan myndigheterna |
| Mediemyndigheten | Tjänster som ger åtkomst till audiovisuella medietjänster (webbplatser, appar, programguider) |
| Konsumentverket | Passagerartransport: webbplatser, appar och elektroniska biljetter |
| Transportstyrelsen | Passagerartransport: reseinformation och tjänster via interaktiva självserviceterminaler |
| Myndigheten för tillgängliga medier (MTM) | E-böcker |

Konsumenter kan klaga på produkters och tjänsters tillgänglighet till PTS (som inte återkopplar men använder klagomålen i tillsynen). Vid brister uppmanas aktören att åtgärda; därefter kan myndigheten förelägga med vite (35 §) eller ta ut sanktionsavgift på 10 000 till 10 000 000 kronor (37–39 §§). Beslut kan överklagas till förvaltningsdomstol (41 §).

## Skillnader mellan lagarna som påverkar dokumentet

| Område | DOS-lagen (2018:1937) | Tillgänglighetslagen (2023:254) |
|---|---|---|
| Dokumentet | Tillgänglighetsredogörelse (13 §) med Digg-föreskriven mall (MDFFS 2019:2 §6) | Information om tjänstens tillgänglighet (25 §) – ingen föreskriven mall, PTS vägledning är förebilden |
| Vem omfattas | Offentliga aktörer | Den som tillhandahåller tjänster mot konsumenter inom 4 §-områdena – oavsett aktörstyp |
| Följsamhetsord | ”Helt”, ”delvis” eller ”inte” förenlig – krav med exakt ordval | Inte krav; skriv tydligt om kända brister finns |
| Meddelandefunktion | Krav (13 § andra stycket); formulär enligt Digg | Inget krav; kontaktväg är god praxis |
| Datum | Bedömnings- och uppdateringsdatum – krav | God praxis, inte lagkrav |
| Undantag | 12 § oskäligt betungande anpassning; bedömningen redovisas i redogörelsen | 7 § grundläggande karaktär eller oproportionerligt stor börda; vilka krav det gäller framgår av informationen, bedömningen dokumenteras och underrättas myndigheten separat (8 §) |
| Innehåll utanför lagen | 9 § (äldre filformat, kartor, tredjepartsinnehåll) | 5 § (kartor, tredjepartsinnehåll) och övergångsbestämmelserna |
| Tillsyn | Digg (digg.se/tdosanmalan) | Sex myndigheter per tjänsteområde – se tabellen ovan |

## Källor

- Digg – Skapa en tillgänglighetsredogörelse: https://www.digg.se/kunskap-och-stod/digital-tillganglighet/skapa-en-tillganglighetsredogorelse (senast uppdaterad 2025-10-10, hämtad 2026-09-01) med Word-mallar för [webbplats](https://www.digg.se/download/18.129a4fef1939e2e1c1f14ca6/1694510960862/mall-for-tillganglighetsredogorelse-webbplats-svenska.docx) och [app](https://www.digg.se/download/18.129a4fef1939e2e1c1f14ca0/1694510960846/mall-for-tillganglighetsredogorelse-app-svenska%20\(1\).docx)
- MDFFS 2019:2, konsoliderad version: https://www.digg.se/om-oss/forfattningssamling/foreskrifter-om-tillganglighet-till-digital-offentlig-service-mdffs-20192/konsoliderad-version
- DOS-lagen (2018:1937): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20181937-om-tillganglighet-till-digital_sfs-2018-1937/
- Digg – rättslig vägledning, undantag från kraven: https://www.digg.se/kunskap-och-stod/digital-tillganglighet/rattslig-vagledning/8.-undantag-fran-kraven
- Anmäl bristande tillgänglighet: https://www.digg.se/tdosanmalan
- PTS – lagen om vissa produkters och tjänsters tillgänglighet: https://pts.se/digital-inkludering/lagen-om-vissa-produkters-och-tjansters-tillganglighet/ (hämtad 2026-09-17)
- PTS – Information om tjänstens tillgänglighet: https://pts.se/digital-inkludering/lagen-om-vissa-produkters-och-tjansters-tillganglighet/information-om-tjanstens-tillganglighet/ (hämtad 2026-09-17)
- Lag (2023:254) om vissa produkters och tjänsters tillgänglighet: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2023254-om-vissa-produkters-och-tjansters_sfs-2023-254/
- Förordning (2023:676) om vissa produkters och tjänsters tillgänglighet: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-2023676-om-vissa-produkters-och_sfs-2023-676/
- PTSFS 2024:6 om vissa tjänsters tillgänglighet: https://pts.se/regelbibliotek/foreskrifter-om-vissa-tjansters-tillganglighet/
