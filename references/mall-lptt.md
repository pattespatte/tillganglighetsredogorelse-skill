# Mall – information om tjänstens tillgänglighet (lagen 2023:254)

> **Syfte:** Mall för den information om tjänstens tillgänglighet som en tjänsteleverantör ska ta fram enligt 25 § lagen (2023:254) om vissa produkters och tjänsters tillgänglighet (tillgänglighetslagen). Informationen fyller en liknande funktion som en tillgänglighetsredogörelse enligt DOS-lagen – men begreppet tillgänglighetsredogörelse används inte i lagen och det finns ingen föreskriven mall. Strukturen här följer Post- och telestyrelsens (PTS) vägledning om informationen.

> **Ursprung:** Kravinnehållet kommer från 25 § lagen, 24 § förordningen (2023:676) om vissa produkters och tjänsters tillgänglighet samt – för tjänster under PTS tillsyn – 3–5 §§ PTSFS 2024:6, tolkat enligt PTS vägledning. Undantagsavsnittet följer 7–8 §§ lagen.

> **Källor:** [PTS – Information om tjänstens tillgänglighet](https://pts.se/digital-inkludering/lagen-om-vissa-produkters-och-tjansters-tillganglighet/information-om-tjanstens-tillganglighet/); [Lag (2023:254)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2023254-om-vissa-produkters-och-tjansters_sfs-2023-254/); [Förordning (2023:676)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-2023676-om-vissa-produkters-och_sfs-2023-676/).

## Innan du använder mallen

Lagen gäller tjänster som erbjuds till konsumenter inom sex områden (4 §): elektronisk kommunikation, åtkomst till audiovisuella medietjänster, passagerartransport, banktjänster, e-böcker och e-handel. Det är tjänsten – inte aktörstypen – som avgör omfattningen. Tjänster som tillhandahålls av mikroföretag (färre än tio anställda och högst 2 miljoner euro i årsomsättning eller balansomslutning) undantas från kraven (10 §). Avgör först att lagen verkligen gäller – se `references/krav-och-kallor.md`.

Platshållarna följer samma konvention som DOS-mallarna:

- `{så här}` – obligatorisk information. Måste du fylla i.
- `[så här]` – frivillig information.
- `<så här>` – information som ska ersättas med faktiska data (datum, länkar).

När du fyller i tar du bort hela platshållarsyntaxen. Ta bort avsnitt markerade `VILLKORLIGT` som inte är aktuella. Behåll rubrikernas lydelse och nivå – de är skillens struktur, även om lagen inte föreskriver någon mall.

Det här gäller för informationen:

- Informationen ska åtfölja tjänsten. För tjänster under PTS tillsyn innebär det att den tas med i de allmänna villkoren eller i ett motsvarande dokument (PTSFS 2024:6). Länka den dessutom tydligt från startsidan eller gör den åtkomlig från alla sidor, till exempel i en sidfot – det är PTS rekommendation.
- Allmänheten ska ha tillgång till informationen i tal och skrift, och den ska ges på ett sätt som är tillgängligt för personer med funktionsnedsättning (24 § förordningen).
- Informationen ska sparas så länge tjänsten tillhandahålls.
- Finns tjänsten som både webbplats och app är det en tjänst – skriv en information som täcker båda. Nämn appen i beskrivningen. Informationen ska finnas på aktörens webbplats eller där appen laddas ner, och bör även vara åtkomlig i appen.
- Skriv alltid datum som `ÅÅÅÅ-MM-DD`. Datum är god praxis här, inte lagkrav – ange dem ändå, de gör informationen trovärdig och går att kontrollera.
- Lista bristerna per användningssituation med samma tio situationer som i DOS-mallarna, och ange WCAG/EN 301 549-kriterium när det är känt.
- Skilj på kända brister (avsnittet ”Delar som kan vara svåra att använda”) och åberopade undantag (7 §-avsnittet). Ett undantag ska dokumenteras, sparas och underrättas till tillsynsmyndigheten enligt 8 § – det är en separat skyldighet utöver den publika informationen.

## Fält att fylla i innan publicering

| Fält | Värde |
|---|---|
| Aktörens namn | `{aktörens namn}` |
| Tjänstens namn | `{tjänstens namn}` |
| Länk till tjänsten | `<https://...>` |
| Tjänsteområde (styr tillsynsmyndigheten) | e-handel / banktjänster / elektronisk kommunikation / passagerartransport / åtkomst till audiovisuella medietjänster / e-böcker |
| Standarden EN 301 549 följs | ja / nej (nej kräver mer ingående beskrivning) |
| Kända brister | nej / lista per användningssituation |
| 7 §-undantag åberopas | ja / nej |
| Test- och kvalitetssäkringsmetoder | `{metoder}` |
| Senaste kontroll | `<ÅÅÅÅ-MM-DD>` |
| Senast uppdaterad | `<ÅÅÅÅ-MM-DD>` |
| E-post | `{e-postadress}` |
| Telefon | `[telefonnummer]` |
| Kontaktformulär (frivilligt) | `[länk]` |

---

# Mall

```markdown
# Tillgänglighet för {tjänstens namn}

{aktörens namn} erbjuder {tjänstens namn}. Vi vill att så många som möjligt ska kunna använda tjänsten. Den här informationen beskriver hur {tjänstens namn} uppfyller tillgänglighetskraven i lagen (2023:254) om vissa produkters och tjänsters tillgänglighet, vilka delar som kan vara svåra att använda och hur du kan kontakta oss.

Gå direkt till {tjänstens namn}: <https://länk-till-tjänsten>
```

> **Rubrik H1 + ingress:** Obligatoriskt. Ingressen ska nämna aktören, tjänstens namn, lagen och att det går att kontakta aktören. Lagen föreskriver inte denna lydelse – strukturen följer PTS vägledning och håller dokumentet likt en tillgänglighetsredogörelse.

---

```markdown
## Om tjänsten

{Vad tjänsten är och hur den fungerar, i korthet. Beskriv de delar som behövs för att man ska kunna bedöma om tjänsten är tillgänglig – till exempel att den består av en webbutik och en mobil app, att betalning görs via kort eller Swish och att kundservice erbjuds via chatt.}

[Om tjänsten även finns som app: nämn {appens namn} här. Informationen gäller hela tjänsten.]
```

> **Tjänstebeskrivning:** Obligatoriskt. Enligt 24 § förordningen ska informationen innehålla en redogörelse för de tillämpliga kraven och, i den mån det behövs för att bedöma överensstämmelsen, en beskrivning av tjänstens utformning och funktion. PTS vägledning betonar den allmänna beskrivningen.

---

```markdown
## Hur tillgänglig är tjänsten?

[Om tjänsten följer standarden:] Vi utformar och utvecklar {tjänstens namn} med ledning av standarden EN 301 549. En tjänst som följer standarden antas uppfylla tillgänglighetskraven i lagen (presumtion om överensstämmelse).

[Om tjänsten inte följer standarden:] {tjänstens namn} följer inte en standard i sin helhet. Så här uppfyller tjänsten tillgänglighetskraven: {mer ingående beskrivning av hur tjänsten är möjlig att uppfatta, hantera, begripa och robust – vilka funktioner, stöd och tekniska lösningar som gör det}

[Om inga kända brister:] Vi känner för närvarande inte till några delar av tjänsten som kan vara svåra att använda.

[Om kända brister:] Vi känner till att vissa delar av tjänsten kan vara svåra att använda. Se nedan.
```

> **Kravuppfyllelse:** Obligatoriskt. Enligt PTS vägledning kan aktören ange att den följer aktuell standard (EN 301 549 ger presumtion om överensstämmelse enligt 9 § lagen) eller i stället beskriva mer ingående hur kraven följs. Notera skillnaden mot DOS-lagen: lagen kräver inte orden helt, delvis eller inte – men var tydlig med om kända brister finns.

---

```markdown
## Delar av tjänsten som kan vara svåra att använda

[Inga kända brister: behåll meningen och ta bort alla situationer nedan samt 7 §-avsnittet.] Vi känner inte till några delar av tjänsten som kan vara svåra att använda. Hör gärna av dig om du upptäcker något – se Kontakta oss nedan.

[Annars: behåll meningen:] Följande delar av {tjänstens namn} kan vara svåra att använda:

### Problem vid användning utan synförmåga
- {beskrivning av innehåll och problem, med WCAG-kriterium}

### Problem vid användning med nedsatt syn
- {beskrivning av innehåll och problem, med WCAG-kriterium}

### Problem vid användning med nedsatt färgseende
- {beskrivning av innehåll och problem, med WCAG-kriterium}

### Problem vid användning utan hörsel
- {beskrivning av innehåll och problem, med WCAG-kriterium}

### Problem vid användning med nedsatt hörsel
- {beskrivning av innehåll och problem, med WCAG-kriterium}

### Problem vid användning utan röstförmåga
- {beskrivning av innehåll och problem, med WCAG-kriterium}

### Problem vid användning med nedsatt finmotorik eller styrka
- {beskrivning av innehåll och problem, med WCAG-kriterium}

### Problem vid användning med nedsatt rörlighet
- {beskrivning av innehåll och problem, med WCAG-kriterium}

### Problem vid användning vid känslighet för flimmer
- {beskrivning av innehåll och problem, med WCAG-kriterium}

### Problem vid användning vid kognitiv nedsättning
- {beskrivning av innehåll och problem, med WCAG-kriterium}

[Vi arbetar med att åtgärda bristerna. Vår ambition är att ha åtgärdat dem senast <ÅÅÅÅ-MM-DD>.]
```

> **Kända brister:** Obligatoriskt. PTS anger syftet med informationen: användaren ska förstå vilka delar av tjänsten som kan vara svåra att använda, och varför. Situationerna är samma tio som i DOS-mallarna – använd bara de som har brister, ta bort de tomma. Översätt granskningsfynd med `references/wcag-till-situation.md`.

---

```markdown
## Undantag från tillgänglighetskraven (7 §) — VILLKORLIGT

[Kvar endast om undantag åberopas.]

{aktörens namn} åberopar undantag enligt 7 § lagen (2023:254) om vissa produkters och tjänsters tillgänglighet för följande delar av tjänsten och deras tillgänglighetskrav:

- {vilken del av tjänsten och vilket tillgänglighetskrav undantaget gäller}

Motivering: {om det är fråga om en större förändring av tjänstens grundläggande karaktär eller en oproportionerligt stor börda, och varför}
```

> **Undantag:** VILLKORLIGT. Enligt 25 § andra stycket lagen ska det av informationen framgå vilka tillgänglighetskrav som omfattas av ett åberopat undantag. Tänk på 8 §: bedömningen ska dokumenteras, sparas och underrättas till tillsynsmyndigheten – det sker separat från den publika informationen (för PTS-områden via PTS e-tjänst LPTT-rapportering).

---

```markdown
## Hur vi kontrollerar tillgängligheten

Vi kontrollerar {tjänstens namn} genom {automatiserade verktyg / manuella test med skärmläsare och tangentbord / test med verkliga användare / återkommande kvalitetssäkring i utvecklingsflödet – beskriv era metoder}.

Senaste kontrollen gjordes den <ÅÅÅÅ-MM-DD>.

Informationen uppdaterades senast den <ÅÅÅÅ-MM-DD>.
```

> **Kontrollmetod:** Obligatoriskt. PTS vägledning kräver en beskrivning av de metoder för test eller kvalitetssäkring som används – användartester, maskinella tester eller manuella tester. Datumen är god praxis, inte lagkrav.

---

```markdown
## Kontakta oss

Om du upptäcker en brist som inte beskrivs här, eller om du behöver informationen på ett annat sätt, kan du kontakta oss:

- skicka e-post till {e-postadress}
- [ring {telefonnummer}]
- [använd vårt [kontaktformulär](<länk-till-formulär>)]
```

> **Kontakt:** Obligatoriskt i mallen (god praxis – lagen kräver ingen meddelandefunktion som DOS-lagen gör). Minst en kontaktväg måste finnas kvar när du fyllt i. E-post och telefon räcker här, ett formulär är ett bra komplement.

---

```markdown
## Tillsyn

{Tillsynsmyndigheten} har tillsyn över {tjänsteområdet} enligt lagen (2023:254) om vissa produkters och tjänsters tillgänglighet. Du kan anmäla brister i en tjänsts tillgänglighet till den myndigheten.

[För tjänster under PTS – elektronisk kommunikation, banktjänster och e-handel:] PTS tar emot klagomål om produkters och tjänsters tillgänglighet: [pts.se/tillganglighetslagen](https://pts.se/digital-inkludering/lagen-om-vissa-produkters-och-tjansters-tillganglighet/)
```

> **Tillsyn:** Obligatoriskt. Rätt myndighet beror på tjänsteområdet – se tabellen i `references/krav-och-kallor.md`: PTS (elektronisk kommunikation, banktjänster, e-handel), Mediemyndigheten (åtkomst till audiovisuella medietjänster), Konsumentverket (passagerartransport: webbplatser, appar, e-biljetter), Transportstyrelsen (passagerartransport: reseinformation via självserviceterminaler) och Myndigheten för tillgängliga medier (e-böcker). Skriv ut den myndighet som gäller just den här tjänsten.

---

## Checklista innan publicering

- [ ] H1 + ingress nämner aktör, tjänst, lagen (2023:254) och kontaktväg
- [ ] Länk till tjänsten finns under ingressen
- [ ] Tjänstebeskrivning som räcker för att bedöma tillgängligheten
- [ ] Hur kraven uppfylls: standard följs (EN 301 549) eller egen, mer ingående beskrivning
- [ ] Kända brister per användningssituation med WCAG-kriterium – eller meningen om inga kända brister
- [ ] 7 §-avsnittet bara med om undantag åberopas – med vilka krav det gäller och motivering
- [ ] 8 § påmind: undantagsbedömning dokumenterad och myndigheten underrättad (internt, inte i informationen)
- [ ] Test- och kvalitetssäkringsmetoder beskrivna; datum i ÅÅÅÅ-MM-DD
- [ ] Minst en kontaktväg finns (e-post, telefon eller formulär)
- [ ] Tillsynsavsnittet nämner rätt myndighet för tjänsteområdet
- [ ] Informationen åtföljer tjänsten (allmänna villkoren eller motsvarande) och är lätt att hitta från startsidan eller sidfoten
- [ ] App: informationen finns även på webbplatsen eller nedladdningssidan
- [ ] Inga platshållare kvar (`{ }`, `[ ]`, `< >`), inga VILLKORLIGT-markeringar kvar
