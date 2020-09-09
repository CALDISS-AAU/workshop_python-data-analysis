---
title: Data og datasæt
weight: 1
---
I disse Python lektioner gennemgås, hvordan Python anvendes til dataanalyse, men hvad er data overhovedet for noget?

Som udgangspunkt arbejder vi med en meget bred forståelse af data: alle former for information om noget. Grunden til at der i dag er så meget snak om data, dataanalyse, maskinlæring osv., er fordi at stadig mere og mere information digitaliseres, hvorfor det kan gøres til genstand for analyser.

Navn, alder, uddannelse, indkomst, yndlingsfilm, mest aflyttede sange i 2020, antal gange rejst med bus 2 i Aalborg, køb i supermarkeder, størrelse på bolig, indbo, brug af el, varme og vand osv. Alle disse informationer er data og alt sammen kan indgå i analyser til at sige noget om en person eller, mere relevant, flere personer med lignende karakteristika.

Data som en mere eller mindre tilfældig strøm af tilfældig information er vanskelig at arbejde med. Data skal på en eller anden måde være i system for, at det kan analyseres - det gælder både maskinel/computationel analyse eller menneskelig analyse.

Når man taler om et datasæt, mener man typisk en eller anden form for afgrænset mængde data, der måske eller måske ikke er struktureret i en eller anden form.

## Struktureret og ustruktureret data

Man adskiller typisk mellem struktureret og ustruktureret data.

**Struktureret data**

*Struktureret data* er data, der på en eller anden måde er sat i system. Den klassiske repræsentation af struktureret data er i et tabulært format, hvor hver række indeholder en *observation* og hver kolonne indeholder en *variabel* (eller "feature", som det omtales inden for maskinlæring. En observation kan være en person, et land, et firma, et tidspunkt, en kommune osv., mens en variabel er en eller anden form for information om observationen.

Tabellen herunder er et eksempel på struktureret data:

|Navn |Alder |Beskæftigelse |
|-----|------|--------------|
|Lars | 34 | Slagter|
|Gertrud | 62 | Rådgiver|
|Henning | 43 | Revisor|
|Agnes | 38 | Tømrer|

Struktureret data er kendeteget ved at være sat i system sådan, at man umiddelbart kan analysere og spørge data om noget. I ovenstående tabel kan man fx meget hurtigt undersøge, hvor mange der er ældre end 40, hvem der har et fornavn der starter med "H" eller hvem der har beskæftigelse inden for byggeri.

**Ustruktureret data**

*Ustruktureret data* er data, som - kort sagt - ikke er sat i system. Hvis data ikke er struktureret, vil man typisk kalde det ustruktureret data. Tekst, billeder og video er typiske eksempler på ustruktureret data, da disse blot er rå information uden nogen måde at adskille en type information fra en anden. Mange moderne dataanalyseteknikker fokuserer på ustruktureret data, hvor man enten udvikler teknikker til at skabe overblik over ustruktureret data eller forsøger at give data en form for struktur.

Nedenstående er et eksempel på ustruktureret data:

```
["Hvorfor går man ikke i dialog med ⁦@DRC_dk⁩ i stedet for at opsige kontrakten uden varsel. Er det kun for at føre stærk mand politik? DRC yder en fremragende indsats på baggrund af den opgave de har fået #dkpol https://jyllands-posten.dk/indland/ECE12248020/tesfaye-forsoeger-sig-med-en-ny-loesning-paa-alle-udlaendingeministres-problem/ …",
"Alle tæller ❤️ https://twitter.com/cekicozlem/status/1276034922587832326 …",
"Det er så godt arbejde💚 https://twitter.com/fannybroholm/status/1275360842847080449 …",
"Tilfreds med den klima og energiaftale, der er lavet nu. Det er den første delaftale om at nå 70% reduktion i 2030. Særligt glad for at den indeholder principaftale om en CO2 afgiftsreform #dkpol #dkgreen pic.twitter.com/3slrMxLT5B",
"Godt første skridt for den fri natur #dkpol #dkgreen ⁦@alternativet_⁩ https://www.altinget.dk/miljoe/artikel/wermelin-lander-aftale-om-de-foerste-naturnationalparker …",
"Spændende udmelding. ⁦@alternativet_⁩ ønsker også en grøn   Klimaafgift, hvor udgangspunktet er at forureneren betaler #dkgreen #dkpol https://www.altinget.dk/artikel/venstre-og-radikale-laegger-faelles-pres-paa-regeringen-vil-have-ensartet-co2-afgift?SNSubscribed=true&ref=newsletter&refid=fredag-middag-190620&utm_campaign=altingetdk%20Altinget.dk&utm_medium%09=e-mail&utm_source=nyhedsbrev …",
"Så vigtigt at KL tager ansvar for den proces #dkpol #dkgreen https://www.altinget.dk/miljoe/artikel/professor-om-affaldsaftale-kl-og-kommunerne-skal-gribe-chancen-for-at-loese-tingene-selv …",
"Hurra - stor dag for Danmark💚👏🏼👏🏼 https://twitter.com/alternativet_/status/1273555055476723713 …",
"Til klimaforhandlinger i Finansministeriet. Vi sidder og diskuterer rammerne - de næste dage bliver intensive #dkpol #dkgreen @alternativet_ @ Christiansborg Palace  https://www.instagram.com/p/CBi3d0oB9lB/?igshid=ii78cjnx2n72 …",
"Aftale om mindre affald, mindre forbrænding og mere genbrug - god dag for klimaet og miljøet. 1. skridt i en stor miljøpakke #dkpol ⁦@alternativet_⁩ https://www.dr.dk/nyheder/indland/live-regeringen-praesenterer-ny-aftale-om-affald …"]
```

I ovenstående kan man stadig overføre ideen om observationer (i dette tilfælde tweets fra danske politikere), men der er ingen variable eller features givet på forhånd. Der er derfor ingen umiddelbar struktur at gøre brug af for at foretage sig analyser.

## Fra data til dataanalyse

Uanset om data er struktureret eller ustruktureret, er de næsten aldrig klar til at analysere med det samme. Data skal næsten altid tilpasses den analyse, som man ønsker at foretage og de spørgsmål, som man ønsker at få svar på med sin analyse. 

For struktureret data indebærer dette at få identificeret de relevante dele af sine data (er det fx alle observationer, der er relevante?) samt undersøge og rekode variable sådan, at de meningsfuldt kan bruges i sin analyse.

For ustruktureret data indebærer det på en eller anden måde at få sat system i eller skabt overblik over data.

Ofte vil man også arbejde med data fra flere kilder, hvorfor en del forarbejde også kan gå med at få data kombineret i et samlet datasæt.

---
## VIDENSCHECK

*Hvilke af nedenstående er eksempler på datasæt?:*

* Navnet på butikschefen i det lokale supermarked
* Alle værker af H.C. Andersen
* En oversigt over medlemmer af DFØJ med information om navn, fødselsår, arbejdssted og uddannelse
* Filmen "Vampire's Kiss" med Nicolas Cage fra 1988
* Et kontoudtog
* Alle film med Nicolas Cage

{{%expand "Løsning" %}} Distinktionen mellem data og datasæt kan være vanskelig; særligt når man også taler om datasæt af ustruktureret data.

Her gives et bud på hver.

* Navnet på butikschefen i det lokale supermarked: *Ikke et datasæt, da det blot er en enkelt information (et enkelt datapunkt)*


* Alle værker af H.C. Andersen: *Et ustruktureret datasæt. Literatur- og kulturstudier beskæftiger sig meget med indhold af literære værker. Med teknikker i dag kan man godt analysere samlinger af tekst.*


* En oversigt over medlemmer af DFØJ med information om navn, fødselsår, arbejdssted og uddannelse: *Et "klassisk" struktureret datasæt. Observationerne er medlemmerne af DFØJ og variablene er de forskellige informationer for hvert medlem.*


* Filmen "Vampire's Kiss" med Nicolas Cage fra 1988: *Ikke et datasæt.*


* Et kontoudtog: *Diskutabelt. Ofte er en enkelt persons kontoudtog ikke af megen interesse (udover for personen selv og personens bankrådgiver). En samling af kontoudtog vil nok være mere at betragte som et egentlig datasæt (et datasæt med transaktioner som observationer og beløb, tidspunkt og beskrivelse som variable), men et enkelt datasæt kunne også betragtes som et datasæt af transaktioner for den ene person.*


* Alle film med Nicolas Cage: *Et ustruktureret datasæt. Lig med værkerne af H.C. Andersen kunne et studie af dette også være af interesse. Computationel analyse af disse er noget mere kompliceret, men mulig!*

{{% /expand%}}
