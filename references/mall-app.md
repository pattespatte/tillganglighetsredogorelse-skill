# Mall – tillgänglighetsredogörelse för mobil applikation

> **Syfte:** Mall för tillgänglighetsredogörelse för en mobil applikation enligt lagen om tillgänglighet till digital offentlig service (DOS-lagen, 2018:1937).

> **Ursprung:** Rubriklydelse och avsnittsordning följer Diggs officiella Word-mall för appar (svenska). Kravinnehållet kommer från MDFFS 2019:2 §6 och Diggs vägledning. Medvetna avvikelser från Word-mallen: datum skrivs `ÅÅÅÅ-MM-DD`, och den uttryckliga anmälningslänken till Digg i tillsynsblocket.

> **Källor:** Digg – [Skapa en tillgänglighetsredogörelse](https://www.digg.se/kunskap-och-stod/digital-tillganglighet/skapa-en-tillganglighetsredogorelse) med [Word-mall för app](https://www.digg.se/download/18.129a4fef1939e2e1c1f14ca0/1694510960846/mall-for-tillganglighetsredogorelse-app-svenska%20\(1\).docx); [MDFFS 2019:2, konsoliderad version](https://www.digg.se/om-oss/forfattningssamling/foreskrifter-om-tillganglighet-till-digital-offentlig-service-mdffs-20192/konsoliderad-version).

## Så här använder du mallen

Platshållarna följer Diggs konvention: `{så här}` – obligatorisk information, `[så här]` – frivillig information, `<så här>` – information som ska ersättas av faktiska data. Ta bort hela platshållarsyntaxen när du fyller i, och ta bort avsnitt markerade `VILLKORLIGT` som inte är aktuella.

Regler för appar:

- Redogörelsen för en app ska finnas på aktörens webbplats eller i anslutning till informationen där användaren laddar ner appen. Den får också finnas i appen – men aldrig enbart där, eftersom användaren ska kunna läsa den utan att först ladda ner och installera appen (6 § fjärde stycket DOS-föreskriften).
- Nämn appens version och, om appen finns för flera operativsystem, vilket system avsnitten gäller. Digg tillåter en gemensam redogörelse för flera operativsystem bara om det är tydligt vilken information som gäller vilket system.
- Skriv alltid datum som `ÅÅÅÅ-MM-DD`.
- Lista bristerna per användningssituation (tio situationer, se mallen för webbplatser – samma lista gäller) och ange WCAG-kriterium när det är känt.
- Uppdatera redogörelsen när förändringar i appen påverkar tillgängligheten – i praktiken ofta vid varje releas som förändrar gränssnittet.

## Fält att fylla i innan publicering

| Fält | Värde |
|---|---|
| Aktörens namn | `{aktörens namn}` |
| Appens namn | `{appens namn}` |
| Appens version | `{version}` |
| Operativsystem (om flera) | `[iOS/Android/…]` |
| Offentliggjord (versionsdatum) | `<ÅÅÅÅ-MM-DD>` |
| Följsamhet | helt / delvis / inte |
| Bedömningsdatum (senaste ingående granskningen) | `<ÅÅÅÅ-MM-DD>` |
| Senast uppdaterad | `<ÅÅÅÅ-MM-DD>` |
| Utvärderingsmetod | intern / extern / kombination / uppskattning utan granskning |
| Formulärlänk för bristrapportering | `<https://...>` |
| E-post | `{e-postadress}` |
| Telefon | `[telefonnummer]` |
| 12 §-undantag åberopas | ja / nej |
| Innehåll utanför lagen (9 §) finns | ja / nej |

---

# Mall

```markdown
# Tillgänglighet för {appens namn}

Redogörelsen avser {appens namn} version {version}, offentliggjord den <ÅÅÅÅ-MM-DD>.

{aktörens namn} står bakom den här mobila applikationen. Vi vill att så många som möjligt ska kunna använda den. Det här dokumentet beskriver hur {appens namn} uppfyller lagen om tillgänglighet till digital offentlig service, eventuella kända tillgänglighetsproblem och hur du kan rapportera brister till oss så att vi kan åtgärda dem.
```

> **Rubrik H1 + ingress:** Obligatoriskt. Versionsraden gör tydligt vilken appversion redogörelsen avser – Digg kräver att det framgår vilken information som gäller vilket operativsystem när samma redogörelse täcker flera.

---

```markdown
## Hur tillgänglig är den mobila applikationen?

[Om helt:] Vi har inga kända brister i tillgängligheten för den här mobila applikationen.

[Om delvis eller inte:] Vi är medvetna om att delar av den mobila applikationen inte är helt tillgängliga. Se avsnittet om innehåll som inte är tillgängligt nedan för mer information.
```

> **Kort svar:** Obligatoriskt. Följsamhetsgraden med exakt ord (helt, delvis eller inte) anges i avsnittet ”Teknisk information om den mobila applikationens tillgänglighet” nedan.

---

```markdown
## Vad kan du göra om du inte kan använda delar av den mobila applikationen?

Om du behöver innehåll från {appens namn} som inte är tillgängligt för dig, men som är undantaget från lagens tillämpningsområde enligt beskrivning nedan, kan du [meddela oss](<länk-till-formulär>).

[Svarstiden är normalt {svarstid}.]

Du kan också kontakta oss på följande sätt:
- skicka e-post till {e-postadress}
- [ring {telefonnummer}]
```

> **Begäran om tillgängliggörande:** Obligatoriskt. Funktionen ska klara både bristrapportering och begäran om tillgängliggörande (13 § andra stycket och 15 § DOS-lagen). Formuläret – som finns på webbplatsen, inte bara i appen – är den primära funktionen; e-post och telefon kompletterar.

---

```markdown
## Rapportera brister i den mobila applikationens tillgänglighet

Vi strävar hela tiden efter att förbättra den mobila applikationens tillgänglighet. Om du upptäcker problem som inte är beskrivna på den här sidan, eller om du anser att vi inte uppfyller lagens krav, [meddela oss](<länk-till-formulär>) så att vi får veta att problemet finns.
```

> **Meddelandefunktion:** Obligatoriskt enligt Digg. Samma formulärlänk som i föregående avsnitt.

---

```markdown
## Tillsyn

Myndigheten för digital förvaltning, Digg, har ansvaret för tillsyn över lagen om tillgänglighet till digital offentlig service. Du kan anmäla till Digg om du tycker att vår digitala service har brister i tillgänglighet.

Du kan också anmäla till Digg om du tycker att vår bedömning av vad som är oskäligt betungande ska granskas, om du tycker att vår tillgänglighetsredogörelse har brister eller om du tycker att vi inte har hanterat din begäran om tillgängliggörande korrekt.

Anmäl till Digg: [digg.se/tdosanmalan](https://www.digg.se/tdosanmalan)
```

> **Tillsynsblock:** Obligatoriskt. Ska vara identiskt på alla redogörelser. Använd alltid adressen digg.se/tdosanmalan.

---

```markdown
## Teknisk information om den mobila applikationens tillgänglighet

[Om helt:] Den här mobila applikationen är helt förenlig med lagen om tillgänglighet till digital offentlig service.

[Om delvis:] Den här mobila applikationen är delvis förenlig med lagen om tillgänglighet till digital offentlig service, på grund av de brister som beskrivs nedan.

[Om inte:] Den här mobila applikationen är inte förenlig med lagen om tillgänglighet till digital offentlig service. Otillgängliga delar beskrivs nedan.
```

> **Följsamhetsgrad:** Obligatoriskt. Använd exakt ett av orden helt, delvis eller inte. Finns appen för flera operativsystem med olika följsamhet: ge varje system sitt eget uttalande.

---

```markdown
## Innehåll som inte är tillgängligt

[Helt tillgänglig: skriv ”Det finns inget känt innehåll som inte är tillgängligt.” och ta bort alla tre underavsnitten.]

[Annars: behåll den här meningen:] Det innehåll som beskrivs nedan är på ett eller annat sätt inte helt tillgängligt.

### Bristande förenlighet med lagkraven — VILLKORLIGT

Lista bristerna per användningssituation, med samma tio situationer som för webbplatser (utan synförmåga, nedsatt syn, nedsatt färgseende, utan hörsel, nedsatt hörsel, utan röstförmåga, nedsatt finmotorik eller styrka, nedsatt rörlighet, känslighet för flimmer, kognitiv nedsättning). Använd H4-rubriker i formuleringen ”Problem vid användning …” – se mallen för webbplatser.

- {beskrivning av innehåll och problem, med WCAG-kriterium och vilken funktion i appen det gäller}

[Vår ambition är att ha åtgärdat alla kända tillgänglighetsproblem senast <ÅÅÅÅ-MM-DD>.]

### Oskäligt betungande anpassning (12 §) — VILLKORLIGT

[Kvar endast om undantaget åberopas.]

{aktörens namn} åberopar undantag för oskäligt betungande anpassning enligt 12 § lagen om tillgänglighet till digital offentlig service för nedanstående innehåll:

- {beskrivning av innehåll}

Bedömning: {beskriv hur hänsynen till konsekvenserna för personer med funktionsnedsättning vägts in i bedömningen, inklusive uppskattade kostnader och fördelar}

### Innehåll som inte omfattas av lagen (9 §) — VILLKORLIGT

[Kvar endast om sådant innehåll finns.]

Det innehåll som beskrivs här är inte fullt tillgängligt, men undantas enligt 9 § lagen om tillgänglighet till digital offentlig service:

- {beskrivning av innehåll}
```

> **Brister:** Obligatoriskt om appen inte är helt tillgänglig. Ange vilken funktion eller skärm i appen problemet gäller och vilket WCAG-kriterium som inte uppfylls. Ta bort tomma situationer.

---

```markdown
## Hur vi testat den mobila applikationen

[Välj ett alternativ:]
- Vi har gjort en självskattning (intern testning) av {appens namn}.
- {extern aktör} har gjort en oberoende granskning av {appens namn}.
- Vi har gjort en självskattning (intern testning) som kompletterats med extern granskning av {appens namn}.
- Vi har uppskattat tillgängligheten utan granskning.

Senaste bedömningen gjordes den <ÅÅÅÅ-MM-DD>.

[Metod, frivilligt men rekommenderat:] Testningen omfattade automatiserade och manuella stickprov med skärmläsarna {VoiceOver/TalkBack}. {Eventuellt: test med tangentbordsnavigering, kontrastanalys, Switch Access m.m.}

[Granskningsrapport, frivilligt: länk till rapport]

Redogörelsen uppdaterades senast den <ÅÅÅÅ-MM-DD>.
```

> **Utvärderingsmetod + datum:** Obligatoriskt. Bedömningsdatumet gäller den senaste ingående granskningen. Uppdatera redogörelsen när förändringar i appen påverkar tillgängligheten.

---

## Checklista innan publicering

- [ ] H1 + ingress med versionsrad; aktör, appnamn, DOS-lagen och rapportera brister nämns
- [ ] Följsamhetsgrad uttryckt med exakt ord (helt/delvis/inte) under ”Teknisk information”
- [ ] Brister listade per användningssituation, med WCAG-kriterium och vilken funktion det gäller
- [ ] 12 §-avsnittet bara med om undantaget åberopas – med redovisad bedömning
- [ ] 9 §-avsnittet bara med om sådant innehåll finns
- [ ] Formulärlänk finns i både ”Vad kan du göra…” och ”Rapportera brister…”
- [ ] Tillsynsblock med aktiv `digg.se/tdosanmalan`-länk
- [ ] Bedömningsdatum och senast uppdaterad angivna (ÅÅÅÅ-MM-DD), bedömning före eller samma dag som uppdatering
- [ ] Utvärderingsmetod angiven
- [ ] Redogörelsen finns på webbplatsen eller där appen laddas ner – inte enbart i appen
- [ ] Flera operativsystem: tydligt vilken information som gäller vilket system
- [ ] Inga platshållare kvar (`{ }`, `[ ]`, `< >`), inga VILLKORLIGT-markeringar kvar
