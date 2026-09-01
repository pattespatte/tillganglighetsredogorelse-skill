# Krav och källor – tillgänglighetsredogörelse

Referens för skillens lägen utkast och kontrollera: vad lagen och Digg kräver, var det står och var det hamnar i mallen.

## Regelverket i korthet

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

## Användningssituationer (Digg)

Förteckna brister utifrån hur de påverkar användaren – inte utifrån tekniska kategorier. De tio situationerna:

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

## Mallens medvetna avvikelser från Diggs Word-mall

| Avvikelse | Skäl |
|---|---|
| Datum som `ÅÅÅÅ-MM-DD` i stället för Word-mallens ”dag månad år” | Otvetydigt, sorteringsbart och maskinellt kontrollerbart |
| Uttrycklig raden ”Anmäl till Digg: digg.se/tdosanmalan” i tillsynsblocket | Kravet på länk till anmälningsfunktionen är uttryckligt (6 §); synlig textlänk är säkrast |
| Länk till tjänsten direkt under ingressen | Digg saknar den i mallen; den hjälper användaren och saknas ofta i publicerade redogörelser |
| WCAG-kriterium angivet i varje bristpunkt | Gör bristerna spårbara och kontrollerbara; Digg kräver ”detaljerad, fullständig och tydlig” förteckning med skäl |

## Källor

- Digg – Skapa en tillgänglighetsredogörelse: https://www.digg.se/kunskap-och-stod/digital-tillganglighet/skapa-en-tillganglighetsredogorelse (senast uppdaterad 2025-10-10, hämtad 2026-09-01) med Word-mallar för [webbplats](https://www.digg.se/download/18.129a4fef1939e2e1c1f14ca6/1694510960862/mall-for-tillganglighetsredogorelse-webbplats-svenska.docx) och [app](https://www.digg.se/download/18.129a4fef1939e2e1c1f14ca0/1694510960846/mall-for-tillganglighetsredogorelse-app-svenska%20\(1\).docx)
- MDFFS 2019:2, konsoliderad version: https://www.digg.se/om-oss/forfattningssamling/foreskrifter-om-tillganglighet-till-digital-offentlig-service-mdffs-20192/konsoliderad-version
- DOS-lagen (2018:1937): https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20181937-om-tillganglighet-till-digital_sfs-2018-1937/
- Digg – rättslig vägledning, undantag från kraven: https://www.digg.se/kunskap-och-stod/digital-tillganglighet/rattslig-vagledning/8.-undantag-fran-kraven
- Anmäl bristande tillgänglighet: https://www.digg.se/tdosanmalan
