# WCAG-kriterier till användningssituationer

Referens för läget utkast: översätt tekniska granskningsfynd (WCAG eller EN 301 549) till användarvänliga bristpunkter, sorterade per användningssituation. Mappningen är vägledande – bedöm alltid fyndet i sitt sammanhang. Ett fynd kan höra hemma i flera situationer; välj de som beskriver vilka användare som påverkas.

Så skrivs en bristpunkt: **vad** som inte fungerar, **var** det finns (sida, vy eller funktion), **hur** det påverkar användaren, och kriteriumnumret inom parentes. Teknisk detalj hör hemma i granskningsrapporten – i redogörelsen räcker kriteriumhänvisningen.

Exempel: ”Bilder i nyhetsflödet saknar textalternativ, så informationen försvinner för dig som inte kan se bilderna (WCAG 1.1.1).”

## Princippet uppfattas (WCAG 1.x)

| Kriterium | Situationer | Typisk brist |
|---|---|---|
| 1.1.1 Icketextinnehåll | utan synförmåga, nedsatt syn | Bilder, ikoner och diagram saknar textalternativ |
| 1.2.1 Endast ljud och endast video | utan hörsel, utan synförmåga | Förinspelat ljud eller video utan alternativ i text |
| 1.2.2 Textning (förinspelad) | utan hörsel, nedsatt hörsel | Video saknar textning |
| 1.2.4 Textning (live) | utan hörsel, nedsatt hörsel | Direktsänd video saknar textning |
| 1.2.5 Videobeskrivning (förinspelad) | utan synförmåga | Video saknar ljudbeskrivning av det som syns |
| 1.3.1 Info och relationer | utan synförmåga | Rubrikstruktur, tabeller, formuläretiketter eller listor kodas så att skärmläsare inte uppfattar sammanhanget |
| 1.3.2 Meningsfull ordning | utan synförmåga | Innehåll läses upp i förvirrande ordning |
| 1.3.4 Orientering | nedsatt rörlighet, nedsatt syn | Innehåll försvinner eller låses när skärmen roteras |
| 1.3.5 Identifiera syfte med indata | kognitiv nedsättning | Fält uppfyller inte syftet automatiskt (autocomplete) |
| 1.4.1 Användning av färg | nedsatt färgseende | Information bärs enbart av färg, till exempel obligatoriska fält som bara markeras rött |
| 1.4.3 Kontrast (minimum) | nedsatt syn, nedsatt färgseende | Text har för låg kontrast mot bakgrunden |
| 1.4.4 Textstorlek | nedsatt syn | Texten försvinner eller klipps vid förstoring |
| 1.4.5 Bilder av text | nedsatt syn | Text finns bara som bild och kan inte förstoras |
| 1.4.10 Omflöde | nedsatt syn | Innehåll kräver horisontell scrollning vid förstoring eller smal skärm |
| 1.4.11 Icke-textkontrast | nedsatt syn | Ikoner, knappramar och fokusmarkeringar har för låg kontrast |
| 1.4.12 Textavstånd | nedsatt syn | Text går inte att läsa när radavstånd eller teckenavstånd ökar |

## Princippet hanteras (WCAG 2.x)

| Kriterium | Situationer | Typisk brist |
|---|---|---|
| 2.1.1 Tangentbord | utan synförmåga, nedsatt finmotorik eller styrka, nedsatt rörlighet | Funktioner kan bara nås med mus eller pekskärm |
| 2.1.2 Inga tangentbordsfällor | utan synförmåga, nedsatt finmotorik eller styrka | Fokus fastnar i en komponent och kommer inte ut igen |
| 2.2.1 Justerbar tid | kognitiv nedsättning, nedsatt rörlighet | Tidsgränser går inte att förlänga |
| 2.2.2 Pausa, stoppa, dölja | känslighet för flimmer, nedsatt syn | Rörligt eller automatiskt uppdaterat innehåll går inte att pausa |
| 2.3.1 Tre blinkningar | känslighet för flimmer | Innehåll blinkar mer än tre gånger per sekund |
| 2.4.1 Hoppa över block | utan synförmåga | Ingen möjlighet att hoppa förbi återkommande menyinnehåll |
| 2.4.2 Sidtitel | utan synförmåga, kognitiv nedsättning | Sidtitlar beskriver inte sidans innehåll eller är tomma |
| 2.4.3 Fokusordning | utan synförmåga | Fokus flyttas oväntat, till exempel när en dialog öppnas |
| 2.4.4 Länksyfte | utan synförmåga, kognitiv nedsättning | Länkar som ”läs mer” förklarar inte vart de leder |
| 2.4.5 Flera sätt | kognitiv nedsättning | Ingen sökfunktion eller sidkarta utöver menyn |
| 2.4.6 Rubriker och etiketter | kognitiv nedsättning, nedsatt syn | Rubriker och etiketter beskriver inte innehållet eller fältet |
| 2.4.7 Synligt fokus | nedsatt syn, nedsatt finmotorik eller styrka | Det syns inte var tangentbordsfokus finns |
| 2.5.3 Etikett i namnet | utan röstförmåga | Röststyrning fungerar inte eftersom den synliga texten inte ingår i elementets namn |
| 2.5.4 Rörelseaktivering | nedsatt rörlighet, nedsatt finmotorik eller styrka | Skaka eller luta enheten är enda sättet att styra en funktion |

## Princippet begrips (WCAG 3.x)

| Kriterium | Situationer | Typisk brist |
|---|---|---|
| 3.1.1 Webbsidans språk | utan synförmåga | Sidans språk är inte angivet, så skärmläsare läser svensk text med fel uttal |
| 3.1.2 Språk för delar | utan synförmåga | Språkbyte i texten är inte angivet |
| 3.2.4 Konsekvent identifiering | kognitiv nedsättning | Samma funktion heter olika saker på olika sidor |
| 3.3.1 Identifierad indatafel | kognitiv nedsättning, nedsatt syn | Fel i formulär markeras utan att förklaras i text |
| 3.3.2 Etiketter eller instruktioner | kognitiv nedsättning, utan synförmåga | Fält saknar synlig etikett eller instruktion |
| 3.3.3 Förslag vid fel | kognitiv nedsättning | Felmeddelanden föreslår inte hur felet rättas |

## Princippet robust (WCAG 4.x)

| Kriterium | Situationer | Typisk brist |
|---|---|---|
| 4.1.2 Namn, roll, värde | utan synförmåga | Knappar, fält och dialoger saknar namn eller roll, så skärmläsare läser upp dem som bara ”knapp” eller meddelar ingenting; påverkar också röststyrning |
| 4.1.3 Statusmeddelanden | utan synförmåga | Bekräftelser och felmeddelanden visas utan att skärmläsare meddelar dem |

## Vanliga verktygsregler (axe) till kriterier

Automatiska verktyg (axe, Lighthouse, Siteimprove m.fl.) rapporterar regelnamn i stället för kriteriumnummer. Vanliga översättningar:

| axe-regel | Kriterium | Situation |
|---|---|---|
| image-alt, input-image-alt | 1.1.1 | utan synförmåga, nedsatt syn |
| button-name, link-name | 4.1.2 | utan synförmåga, utan röstförmåga |
| color-contrast | 1.4.3 | nedsatt syn, nedsatt färgseende |
| html-has-lang, html-lang-valid, valid-lang | 3.1.1, 3.1.2 | utan synförmåga |
| label, form-field-multiple-labels | 3.3.2, 1.3.1 | utan synförmåga, kognitiv nedsättning |
| heading-order, page-has-heading-one, list, listitem | 1.3.1 | utan synförmåga |
| region, bypass, landmark-unique | 2.4.1, 1.3.1 | utan synförmåga |
| frame-title | 4.1.2 | utan synförmåga |
| tabindex | 2.4.3 | utan synförmåga |
| video-caption, audio-caption | 1.2.2 | utan hörsel, nedsatt hörsel |
| meta-viewport | 1.4.4 | nedsatt syn |
| aria-allowed-attr, aria-valid-attr-value, aria-roles, duplicate-id | 4.1.2 | utan synförmåga |

## Att tänka på

- Automatiska verktyg hittar bara en del av bristerna – kanske runt en tredjedel av kriterierna kan testas maskinellt. En redogörelse som grundar sig enbart på automatisk skanning är inte en ingående granskning. Manuell testning (skärmläsare, tangentbord, förstoring) måste ingå i underlaget; komplettera annars med självskattningens förbehåll.
- För appar rapporteras ofta EN 301 549-klausuler (kapitel 5 och 11) i stället för WCAG-nummer – samma brister och situationer, ange klausulnumret som verktyget rapporterat.
- Nyare verktyg kan rapportera WCAG 2.2-kriterier (till exempel 2.4.11, 2.5.8). Föreskriften hänvisar till EN 301 549 V3.2.1 som bygger på WCAG 2.1 – kontrollera att fyndet inte enbart gäller 2.2 innan det tas med, och ange i så fall kriteriet ändå men notera standardversionen i bristtexten.
