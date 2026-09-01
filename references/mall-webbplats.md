# Mall – tillgänglighetsredogörelse för webbplats

> **Syfte:** Mall för tillgänglighetsredogörelse enligt lagen om tillgänglighet till digital offentlig service (DOS-lagen, 2018:1937). Avsedd att publiceras som en tillgänglig webbsida – det är Diggs utgångsrekommendation.

> **Ursprung:** Rubriklydelse och avsnittsordning följer Diggs officiella Word-mall för webbplatser (svenska). Kravinnehållet kommer från MDFFS 2019:2 §6 och Diggs vägledning. Medvetna avvikelser från Word-mallen: datum skrivs `ÅÅÅÅ-MM-DD` (otydligare format i Word-mallen), länken till tjänsten direkt under ingressen, och den uttryckliga anmälningslänken till Digg i tillsynsblocket.

> **Källor:** Digg – [Skapa en tillgänglighetsredogörelse](https://www.digg.se/kunskap-och-stod/digital-tillganglighet/skapa-en-tillganglighetsredogorelse) med [Word-mall för webbplats](https://www.digg.se/download/18.129a4fef1939e2e1c1f14ca6/1694510960862/mall-for-tillganglighetsredogorelse-webbplats-svenska.docx); [MDFFS 2019:2, konsoliderad version](https://www.digg.se/om-oss/forfattningssamling/foreskrifter-om-tillganglighet-till-digital-offentlig-service-mdffs-20192/konsoliderad-version).

## Så här använder du mallen

Platshållarna följer Diggs konvention:

- `{så här}` – obligatorisk information. Måste du fylla i.
- `[så här]` – frivillig information.
- `<så här>` – information som ska ersättas med faktiska data (datum, länkar).

När du fyller i tar du bort hela platshållarsyntaxen – klamrar, hakparenteser och vinkelparenteser. Ta bort avsnitt markerade `VILLKORLIGT` om de inte är aktuella. Behåll alla obligatoriska avsnitt och rubrikernas exakta lydelse och nivå (H1/H2/H3/H4) – de motsvarar krav i DOS-lagen och Diggs mall. Gäller redogörelsen en e-tjänst i stället för en webbplats: byt ut ordet ”webbplatsen” överallt, konsekvent, men behåll rubrikernas struktur och ordning.

Det här gäller för alla redogörelser:

- Skriv alltid datum som `ÅÅÅÅ-MM-DD`.
- Lista bristerna under ”Bristande förenlighet med lagkraven” utifrån **användningssituationer** (Digg rekommenderar det), inte utifrån tekniska kategorier. Använd bara de situationer där det finns brister – ta bort de tomma.
- Ange alltid vilket WCAG-kriterium (EN 301 549) som inte uppfylls när det är känt – det gör bristerna spårbara och kontrollerbara.
- Redogörelsen ska publiceras i ett tillgängligt format och vara lätt att hitta: länkad tydligt från startsidan eller åtkomlig från alla sidor, till exempel i en sidfot.
- Redogörelsen ska gå att nå utan inloggning. Enligt Diggs vägledning: ”Det är Diggs uppfattning att användare behöver kunna ta del av tillgänglighetsredogörelsen för en webbplats eller app utan att först behöva logga in eller identifiera sig. En tillgänglighetsredogörelse som enbart är åtkomlig efter att personer har loggat in på webbplatsen eller appen är inte lätt åtkomlig.” Digg kallar detta sin uppfattning (vägledning), inte ett uttryckligt lagkrav, men den är ledande vid tillsyn.

## Fält att fylla i innan publicering

| Fält | Värde |
|---|---|
| Aktörens namn | `{aktörens namn}` |
| Tjänstens namn | `{tjänstens namn}` |
| Länk till tjänsten | `<https://...>` |
| Följsamhet | helt / delvis / inte |
| Bedömningsdatum (senaste ingående granskningen) | `<ÅÅÅÅ-MM-DD>` |
| Senast uppdaterad | `<ÅÅÅÅ-MM-DD>` |
| Utvärderingsmetod | intern / extern / kombination / uppskattning utan granskning |
| Formulärlänk för bristrapportering | `<https://...>` |
| E-post | `{e-postadress}` |
| Telefon | `[telefonnummer]` |
| Svarstid | `[svarstid]` |
| 12 §-undantag åberopas | ja / nej |
| Innehåll utanför lagen (9 §) finns | ja / nej |

---

# Mall

```markdown
# Tillgänglighet för {tjänstens namn}

{aktörens namn} står bakom {tjänstens namn}. Vi vill att så många som möjligt ska kunna använda den här webbplatsen. Det här dokumentet beskriver hur {tjänstens namn} uppfyller lagen om tillgänglighet till digital offentlig service, eventuella kända tillgänglighetsproblem och hur du kan rapportera brister till oss så att vi kan åtgärda dem.

Gå direkt till {tjänstens namn}: <https://länk-till-tjänsten>
```

> **Rubrik H1 + ingress:** Obligatoriskt. Ingressen ska nämna aktören, tjänstens namn, DOS-lagen och att det går att rapportera brister. Länken till tjänsten direkt under ingressen är en medveten komplettering till Diggs Word-mall – många redogörelser saknar den idag.

---

```markdown
## Hur tillgänglig är webbplatsen?

[Om helt:] Vi har inga kända brister i tillgängligheten för den här webbplatsen.

[Om delvis eller inte:] Vi är medvetna om att delar av webbplatsen inte är helt tillgängliga. Se avsnittet om innehåll som inte är tillgängligt nedan för mer information.
```

> **Kort svar:** Obligatoriskt. Det här är den lättlästa sammanfattningen – själva följsamhetsgraden med exakt ord (helt, delvis eller inte) anges i avsnittet ”Teknisk information om webbplatsens tillgänglighet” nedan, precis som i Diggs mall.

---

```markdown
## Vad kan du göra om du inte kan använda delar av webbplatsen?

Om du behöver innehåll från {tjänstens namn} som inte är tillgängligt för dig, men som är undantaget från lagens tillämpningsområde enligt beskrivning nedan, kan du [meddela oss](<länk-till-formulär>).

[Svarstiden är normalt {svarstid}.]

Du kan också kontakta oss på följande sätt:
- skicka e-post till {e-postadress}
- [ring {telefonnummer}]
```

> **Begäran om tillgängliggörande:** Obligatoriskt. Det här blocket uppfyller kravet på en funktion där användaren både kan meddela brister och begära tillgängliggörande av undantaget innehåll (13 § andra stycket och 15 § DOS-lagen). Länken ska gå till ett tillgängligt formulär – e-post och telefon är bara komplement, de räcker inte enligt Digg eftersom de inte är tillgängliga för alla.

---

```markdown
## Rapportera brister i webbplatsens tillgänglighet

Vi strävar hela tiden efter att förbättra webbplatsens tillgänglighet. Om du upptäcker problem som inte är beskrivna på den här sidan, eller om du anser att vi inte uppfyller lagens krav, [meddela oss](<länk-till-formulär>) så att vi får veta att problemet finns.
```

> **Meddelandefunktion:** Obligatoriskt enligt Digg. Samma formulärlänk som i föregående avsnitt.

---

```markdown
## Tillsyn

Myndigheten för digital förvaltning, Digg, har ansvaret för tillsyn över lagen om tillgänglighet till digital offentlig service. Du kan anmäla till Digg om du tycker att vår digitala service har brister i tillgänglighet.

Du kan också anmäla till Digg om du tycker att vår bedömning av vad som är oskäligt betungande ska granskas, om du tycker att vår tillgänglighetsredogörelse har brister eller om du tycker att vi inte har hanterat din begäran om tillgängliggörande korrekt.

Anmäl till Digg: [digg.se/tdosanmalan](https://www.digg.se/tdosanmalan)
```

> **Tillsynsblock:** Obligatoriskt. De två styckena följer Diggs mall och ska vara identiska på alla redogörelser. Kravet på information om anmälan till Digg och en länk till anmälningsfunktionen står i 6 § DOS-föreskriften – använd alltid adressen digg.se/tdosanmalan.

---

```markdown
## Teknisk information om webbplatsens tillgänglighet

[Om helt:] Den här webbplatsen är helt förenlig med lagen om tillgänglighet till digital offentlig service.

[Om delvis:] Den här webbplatsen är delvis förenlig med lagen om tillgänglighet till digital offentlig service, på grund av de brister som beskrivs nedan.

[Om inte:] Den här webbplatsen är inte förenlig med lagen om tillgänglighet till digital offentlig service. Otillgängliga delar beskrivs nedan.
```

> **Följsamhetsgrad:** Obligatoriskt. Använd exakt ett av orden helt, delvis eller inte – det är ordalydelsen i lagrummet och i Diggs mall. Undvik vaga formuleringar som ”Vi är medvetna om att delar inte är helt tillgängliga” utan något av orden – där saknas en uttrycklig följsamhetsgrad.

---

```markdown
## Innehåll som inte är tillgängligt

[Helt tillgänglig: skriv ”Det finns inget känt innehåll som inte är tillgängligt.” och ta bort alla tre underavsnitten.]

[Annars: behåll den här meningen:] Det innehåll som beskrivs nedan är på ett eller annat sätt inte helt tillgängligt.

### Bristande förenlighet med lagkraven — VILLKORLIGT

#### Problem vid användning utan synförmåga
- {beskrivning av innehåll och problem, med WCAG-kriterium}

#### Problem vid användning med nedsatt syn
- {beskrivning av innehåll och problem, med WCAG-kriterium}

#### Problem vid användning med nedsatt färgseende
- {beskrivning av innehåll och problem, med WCAG-kriterium}

#### Problem vid användning utan hörsel
- {beskrivning av innehåll och problem, med WCAG-kriterium}

#### Problem vid användning med nedsatt hörsel
- {beskrivning av innehåll och problem, med WCAG-kriterium}

#### Problem vid användning utan röstförmåga
- {beskrivning av innehåll och problem, med WCAG-kriterium}

#### Problem vid användning med nedsatt finmotorik eller styrka
- {beskrivning av innehåll och problem, med WCAG-kriterium}

#### Problem vid användning med nedsatt rörlighet
- {beskrivning av innehåll och problem, med WCAG-kriterium}

#### Problem vid användning vid känslighet för flimmer
- {beskrivning av innehåll och problem, med WCAG-kriterium}

#### Problem vid användning vid kognitiv nedsättning
- {beskrivning av innehåll och problem, med WCAG-kriterium}

[Vår ambition är att ha åtgärdat alla kända tillgänglighetsproblem senast <ÅÅÅÅ-MM-DD>.]

### Oskäligt betungande anpassning (12 §) — VILLKORLIGT

[Kvar endast om undantaget åberopas.]

{aktörens namn} åberopar undantag för oskäligt betungande anpassning enligt 12 § lagen om tillgänglighet till digital offentlig service för nedanstående innehåll:

- {beskrivning av innehåll}

Bedömning: {beskriv hur hänsynen till konsekvenserna för personer med funktionsnedsättning vägts in i bedömningen, inklusive uppskattade kostnader och fördelar}

### Innehåll som inte omfattas av lagen (9 §) — VILLKORLIGT

[Kvar endast om sådant innehåll finns.]

Det innehåll som beskrivs här är inte fullt tillgängligt, men undantas enligt 9 § lagen om tillgänglighet till digital offentlig service:

- {beskrivning av innehåll, till exempel dokument publicerade före den 23 september 2018, kartor eller innehåll från tredje part}
```

> **Brister:** Obligatoriskt om tjänsten inte är helt tillgänglig. Underavsnittet ”Bristande förenlighet med lagkraven” sorterar bristerna per användningssituation – Diggs rekommenderade struktur med de tio situationerna ovan. Beskriv konkret vad som inte fungerar, var det finns (sida eller funktion) och vilket WCAG-kriterium som inte uppfylls. Ta bort tomma situationer. Avsnittet om 12 § kräver att bedömningsgrunden redovisas (13 § DOS-lagen). Avsnittet om 9 § används för innehåll utanför lagens tillämpningsområde – kontrollera att innehållet verkligen omfattas av undantaget innan du använder det.

---

```markdown
## Hur vi testat webbplatsen

[Välj ett alternativ:]
- Vi har gjort en självskattning (intern testning) av {tjänstens namn}.
- {extern aktör} har gjort en oberoende granskning av {tjänstens namn}.
- Vi har gjort en självskattning (intern testning) som kompletterats med extern granskning av {tjänstens namn}.
- Vi har uppskattat tillgängligheten utan granskning.

Senaste bedömningen gjordes den <ÅÅÅÅ-MM-DD>.

[Metod, frivilligt men rekommenderat:] Testningen omfattade automatiserade och manuella stickprov i webbläsarna {Edge/Chrome} med skärmläsaren {NVDA/JAWS/VoiceOver}. {Eventuellt: test med tangentbordsnavigering, kontrastanalys m.m.}

[Granskningsrapport, frivilligt: länk till rapport]

[Webbplatsen publicerades den <ÅÅÅÅ-MM-DD>.]

Redogörelsen uppdaterades senast den <ÅÅÅÅ-MM-DD>.
```

> **Utvärderingsmetod + datum:** Obligatoriskt. Bedömningsdatumet gäller den senaste ingående granskningen som ligger till grund för hela redogörelsen. ”Redogörelsen uppdaterades senast” gäller den senaste översynen – även en översyn utan fullständig granskning räknas. Digg rekommenderar en översyn av aktualiteten minst en gång om året; för e-tjänster kan det behövas en uppdatering vid varje produktionssättning.

---

## Checklista innan publicering

- [ ] H1 + ingress nämner aktör, tjänst, DOS-lagen och möjligheten att rapportera brister
- [ ] Länk till själva tjänsten finns under ingressen
- [ ] Kort svar (”Hur tillgänglig är webbplatsen?”) stämmer med följsamhetsgraden
- [ ] Följsamhetsgrad uttryckt med exakt ord (helt/delvis/inte) under ”Teknisk information”
- [ ] Brister listade per användningssituation, med WCAG-kriterium (eller ”inget känt innehåll”)
- [ ] 12 §-avsnittet bara med om undantaget åberopas – med redovisad bedömning
- [ ] 9 §-avsnittet bara med om sådant innehåll finns
- [ ] Formulärlänk finns i både ”Vad kan du göra…” och ”Rapportera brister…”
- [ ] Tillsynsblock med aktiv `digg.se/tdosanmalan`-länk
- [ ] Bedömningsdatum och senast uppdaterad angivna (ÅÅÅÅ-MM-DD), bedömning före eller samma dag som uppdatering
- [ ] Utvärderingsmetod angiven
- [ ] Redogörelsen går att nå utan inloggning och länkas från startsidan eller sidfoten
- [ ] Inga platshållare kvar (`{ }`, `[ ]`, `< >`), inga VILLKORLIGT-markeringar kvar
