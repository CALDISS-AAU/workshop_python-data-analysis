# Introduktion til Python til Dataanalyse

Denne lektion gennemgår hvordan Python anvendes til dataanalyse. Der introduceres især til data frames i Python biblioteket "pandas".

# {#Kapitel}Data i Python

I dette første kapitel tages et kig på, hvad data er for en størrelse, og hvordan et struktureret datasæt ser ud i Python. 

# {#Afsnit}Data og datasæt

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

# {#Afsnit}Introduktion til pandas

Pakken `pandas` (https://pandas.pydata.org/) er et Python bibliotek til datahåndtering og dataanalyse. Pandas egner sig særligt til data i tabeller struktureret i rækker og kolonner. En datatabel kaldes inden for pandas en "DataFrame"; et bestemt Python objekt specifikt til at lagre og bearbejde data i tabeller.

Denne lektion gennemgår diverse basale funktioner til at indlæse, udforske og håndtere en pandas DataFrame. Se også den officielle dokumentation for flere guides, introduktioner og beskrivelser til at arbejde med pandas: https://pandas.pydata.org/docs/

## Indlæs og inspicer data med pandas

`pandas` pakken indeholder funktioner til at indlæse data i forskellige formater; herunder CSV, JSON, Excel, Stata, SAS osv.

I det nedenstående indlæses pandas biblioteket, hvorefter datasættet "ESS2014DK_subset.csv" indlæses. Biblioteket `numpy` indlæses også, da det indeholder en række brugbare funktioner til at foretage beregninger på pandas dataframes:


```python
import numpy as np
import pandas as pd

ess2014 = pd.read_csv('https://github.com/CALDISS-AAU/workshop_python-data-analysis/raw/master/datasets/ESS2014DK_subset.csv')
```

{{% notice note %}}
Bemærk importkonventionerne for `numpy` og `pandas`. `numpy` importeres typisk som `np` og `pandas` typisk som `pd`.
{{% /notice%}}

{{% notice info %}}
Datasættet, som indlæses her, er et uddrag af datasættet fra European Social Survey (ESS) 2014. ESS er en europæisk surveyundersøgelse, der gentages hvert andet år. Surveyet behandler spørgsmål om folks helbred, beskæftigelse, politiske holdninger, tillid osv. I dette uddrag er der kun inkluderet de danske respondenter og et mindre udpluk variable.
{{% /notice%}}

Datasættet er nu indlæst som et dataframe objekt i Python, som man kan interagere med. 

Metoden `.head()` printer de første fem rækker af datasættet:


```python
ess2014.head()
```




[TABLE 1]



Dataframes er et tabulært dataformat. Når en fil indlæses som en pandas dataframe, skal filen derfor være i et format, der kan konverteres til tabelformat (data i rækker og kolonner).

I dette datasæt udgør observationerne (rækkerne) enkeltpersoner, som har besvaret spørgeskemaet. De enkelte kolonner indeholder oplysninger om de enkelte personer. 
Af ovenstående print af de første fem række kan man fx læse, at personen i række 4 (rækkeindeks 3) er en kvinde født i 1958, som er 162 cm høj.

{{% notice info %}} Subsettet af ESS 2014 indeholder følgende kolonner:
- `idno`: Personens id-numre/respondentnøgle
- `ppltrst`: Personens vurdering på en skala fra 0-10 af, hvor meget de stoler på andre mennesker
- `happy`: Personens vurdering på en skala fra 0-10 af, hvor glade de føler sig
- `health`: Personens vurdering af eget helbred fra "Very bad" til "Very good"
- `cgtsday`: Antal cigaretter personen ryger om dagen
- `alcfreq`: Hvor ofte personen drikker alkohol
- `height`: Personens højde i centimeter
- `weight`: Personens vægt i kilo
- `gndr`: Personens køn (mand/kvinde)
- `yrbrn`: Personens fødselsår
{{% /notice %}}

{{% notice info %}} **NaN?**

Som det ses af datasættet fremgår værdien `NaN` flere gange i datasættet (særligt under kolonnen `cgtsday`). 

`NaN` angiver missingværdi. En missingværdi er en ikke-gyldig værdi; fx hvis en person ikke svarer, informationen ikke har været muligt at skaffe eller andet.

{{% /notice %}}

## Series og dataframes

En dataframe kan siges at bestå af en samling af kolonner. En kolonne i en dataframe kaldes en `series`.

Navnene på kolonnerne, som en dataframe indeholder, kan ses af attributen `.columns`:


```python
ess2014.columns
```




    Index(['idno', 'ppltrst', 'happy', 'health', 'cgtsday', 'alcfreq', 'height',
           'weight', 'gndr', 'yrbrn'],
          dtype='object')



Hver kolonne ligger som et attribut i dataframen, og kan derfor tilgås direkte. Herunder printes `health` kolonnen:


```python
print(ess2014.health.head())
```

    0    Very good
    1    Very good
    2         Good
    3         Good
    4    Very good
    Name: health, dtype: object


Dog vil man typisk refere til enkeltkolonner på denne måde:


```python
print(ess2014['health'].head())
```

    0    Very good
    1    Very good
    2         Good
    3         Good
    4    Very good
    Name: health, dtype: object


Der er ikke forskel mellem de to måder at gøre det på, men sidstviste måde er mere gængs og gør kode mere overskuelig.

Typen kan tjekkes med `type()`. Herunder ses det, at hele dataframen er et dataframe objekt, mens den enkelte kolonne (`health`) er et series objekt:


```python
print(type(ess2014))
print(type(ess2014['health']))
```

    <class 'pandas.core.frame.DataFrame'>
    <class 'pandas.core.series.Series'>


### Pandas series og lister

En pandas series er på mange måder sammenlignelig med en Python liste: Det er en række værdier, hvor hvert element har et indeks.

Ligesom med lister, kan enkeltelementer af en series tilgås ved at refere til deres indeks:


```python
print(ess2014['health'][122]) #Printer indeks 122
```

    Very good


Lister kan konverteres direkte til pandas series med `pd.Series()`:


```python
a_list = [1, 5, 9, 12, 18]
a_series = pd.Series(a_list)

print(a_list)
print(a_series)
```

    [1, 5, 9, 12, 18]
    0     1
    1     5
    2     9
    3    12
    4    18
    dtype: int64


Læg i ovenstående mærke til, at når en series printes, printes elementernes indeks ud også. Dette er fordi, at man selv kan specificere indeksværdier i en pandas series:


```python
values = ["value1", "value2", "value3", "value4", "value5"]
a_series = pd.Series(a_list, index = values)

print(a_series)
```

    value1     1
    value2     5
    value3     9
    value4    12
    value5    18
    dtype: int64


Gives en serie indeksværdier, kan enkeltelementer referes til både med deres indeksnummer og indeksværdi:


```python
print(a_series[2]) # Printer den 3. værdi ud fra indeksnummer (indeks 2)
print(a_series['value3']) # Printer den 3. værdi ud fra indeksværdi ("value3")
```

    9
    9


**Operationer på serier**

Den store forskel på lister og pandas series er, at man kan foretage beregninger direkte på serier.

Fx kan man ikke multiplicere enkeltværdierne i en liste direkte (nedenstående printer bare listen 2 gange):


```python
a_list * 2
```




    [1, 5, 9, 12, 18, 1, 5, 9, 12, 18]



Pandas series kan man derimod foretage operationer direkte på:


```python
a_series * 2
```




    value1     2
    value2    10
    value3    18
    value4    24
    value5    36
    dtype: int64



Dette gør også, at man kan bruge funktioner fra fx `numpy` til at udregne forskellige mål ud fra en series.

Herunder udregnes fx middelværdi for `a_series`:


```python
import numpy as np

np.mean(a_series)
```




    9.0



---
## ØVELSE: Indlæs datasæt

1. Indlæs datasættet ESS2014DK med `pd.read_csv()`. Funktionen kan indlæse data direkte fra et link (husk at importere pandas biblioteket).

    - Link til data: https://github.com/CALDISS-AAU/workshop_python-data-analysis/raw/master/datasets/ESS2014DK_subset.csv
    
2. Brug `np.mean()` (`numpy.mean()`) til at udregne middelværdien af `height` variablen i datasættet. Hvad er middelværdien?



{{%expand "Løsning" %}} 


```python
import pandas as pd
import numpy as np

ess2014 = pd.read_csv('https://github.com/CALDISS-AAU/workshop_python-data-analysis/raw/master/datasets/ESS2014DK_subset.csv')

print(np.mean(ess2014['height']))
```

    173.75217100868403


{{% /expand%}}

---

# {#Afsnit}Variabeltyper

Man adskiller overordnet mellem to typer af variable; særligt inden for strukuterede datasæt: kontinuerlige og kategoriske. 


## Kontinuerlige variable

Kontinuerlige variable kan tage en nærmest uafgrænset mængde af forskellige numeriske værdier, hvor man ikke i forvejen kan afgrænse, hvilke værdier, som variablen kan antage. Indkomst, vægt og alder er eksempler på kontinuerlige variable. Selvfølgelig er der værdier, som disse variable ikke kan tage - fx negative værdier - men man kan med disse variable ikke vide i forvejen, hvilke værdier, man vil ende ud med. 

I datasættet ESS2014DK er `weight`, `height` og `yrbrn` eksempler på kontinuerlige variable. 

Tag fx et kig på værdierne i `height`:


```python
ess2014['height'].head(10)
```




    0    178.0
    1    172.0
    2    176.0
    3    162.0
    4    175.0
    5    160.0
    6    167.0
    7    194.0
    8    176.0
    9    157.0
    Name: height, dtype: float64



Variablen indeholder personens højde i cm og kan derfor antale et stort antal forskellige værdier. Variablen er kontinuerlig, fordi selvom variablen selvfølgelig ikke kan antage alle værdier (fx -157 eller 1.234), så kan det ikke i forvejen afgrænses præcist, hvilke værdier der vil ende i datasættet.

## Kategoriske variable

Kategoriske variable kan i modsætning til kontinuerlige kun antage et afgrænset og i forvejen defineret sæt af værdier. 

Fødselskommune, partitilhør eller hvorvidt man kan lide jazz, er eksempler på kategoriske variable. Spørgsmål i spørgeskemaer med forhåndsdefinerede svarmuligheder er altid kategoriske. 

I datasættet ESS2014DK er `happy`, `health` og `alcfreq` eksempler på kategoriske variable.

Tag et kig på værdierne i `health`:


```python
ess2014['health'].head(10)
```




    0    Very good
    1    Very good
    2         Good
    3         Good
    4    Very good
    5         Fair
    6         Good
    7         Fair
    8         Fair
    9         Good
    Name: health, dtype: object



Variablen indeholder personens vurdering af eget helbred fra "Very bad" til "Very good". Det er derfor i forvejen afgrænset, hvilke værdier, der kan optræde i datasættet, hvorfor den er kategorisk.

---
## VIDENSCHECK

Tag et kig på variablerne `cgtsday` og `ppltrst`. 

*Hvilken type variabel er de?*

{{%expand "Løsning" %}} `cgtsday` er kontinuerlig, da den kan antage et ikke i forvejen afgrænset forskellige numeriske værdier. 

`ppltrst` er kategorisk, da den kun kan antage i forvejen definerede værdier.

{{%/expand %}}

---

# {#Kapitel}Udforsk Data i Python

Med datasættet indlæst, kan forskellige funktioner bruges til at udforske indholdet i data - enten ved at beregne forskellige deskriptive mål eller ved at foretage visualiseringer.

# {#Afsnit}Deskriptive mål

Én måde at udforske et datasæt er ved at se nærmere på forskellige deskriptive mål for variable i datasættet.

Metoden `.describe()` danner deskriptive mål for alle (kompatible) variable i datasættet:


```python
ess2014.describe()
```




[TABLE 2]



Metoden fungerer også på enkeltvariable:


```python
ess2014['weight'].describe()
```




    count    1473.000000
    mean       75.855261
    std        15.599516
    min        38.000000
    25%        65.000000
    50%        74.000000
    75%        85.000000
    max       137.000000
    Name: weight, dtype: float64



`.describe()` danner følgende mål:
- `count`: Antal svar ekskl. missing
- `mean`: Middelværdien
- `std`: Standardafvigelsen
- `min`: Minimumværdien
- `25%`: 1. kvartil
- `50%`: 2. kvartil
- `75%`: 3. kvartil
- `max`: Maksimumværdien

Pakken `numpy` indeholder funktioner til, at disse værdier kan dannes enkeltvis.

Herunder printes fx middelværdien, standardafvigelsen, minimums- og maksimumsværdien for variablen `weight`:


```python
import numpy as np

print(np.mean(ess2014['weight']))
print(np.std(ess2014['weight']))
print(np.min(ess2014['weight']))
print(np.max(ess2014['weight']))
```

    75.85526137135099
    15.594219726642477
    38.0
    137.0


Ovenstående værdier fortæller, at `weight` indeholder værdier fra 38.0 til 137.0 med en middelværdi på 75.86 og en standardafvigelse på 15.59 (middelværdien af de afstande, som hver observation afviger fra middelværdien).

## Deskriptive mål og kategoriske variable

Sammenlignes outputtet fra `.describe()` med indholdet af datasættet ses, at der ikke udregnes deskriptive mål for alle variable. 

Når `.describe()` bruges på et hel dataframe, udregnes kun mål for numeriske variabeltyper; altså variable, der kun består af tal.

Metoden kan dog også bruges på en kategorisk variabel som `ppltrst`:


```python
ess2014['ppltrst'].describe()
```




    count     1500
    unique      11
    top          8
    freq       475
    Name: ppltrst, dtype: object



**Hvornår er en variabel kategorisk?**

Det kan måske give anledning til undren, hvorfor der fx ikke kan beregnes en middelværdi af `ppltrst`, da variablen umiddelbart indeholder tal:


```python
ess2014['ppltrst'].head()
```




    0    6
    1    8
    2    8
    3    8
    4    5
    Name: ppltrst, dtype: object



Ved et nærmere kig viser det sig dog, at variablen også indeholder tekstværdier.

`.unique()` returnerer de unikke værdier i variablen:


```python
ess2014['ppltrst'].unique()
```




    array(['6', '8', '5', '9', '7', '3', '4', 'Most people can be trusted',
           '2', "You can't be too careful", '1', nan], dtype=object)



Af ovenstående ses, at variablen indeholder tekstværdierne "Most people can be trusted" (svarende til 10 på skalaen) og "You can't be too careful" (svarende til 0 på skalaen).

Hvis der skal udregnes middelværdi på denne variablen, skal værdierne først konverteres om til numeriske værdier (mere om dette senere).

---
## ØVELSE: Deskriptive mål

Brug `.describe()` eller passende numpy kommandoer til at finde ud af følgende:

- Hvor gammel er den yngste person i datasættet?
- Hvor gammel er den ældste person i datasættet?
- Hvad er gennemsnitsalderen i datasættet?

Husk at datasættet er fra 2014.

{{%expand "Løsning" %}}



```python
min_age = 2014 - np.max(ess2014['yrbrn'])
max_age = 2014 - np.min(ess2014['yrbrn'])
mean_age = 2014 - np.mean(ess2014['yrbrn'])

print(min_age, max_age, mean_age)
```

    15 100 48.108521970705624


{{% notice tip %}} Brug "f-strings" til at indsætte python-objekter direkte i et stykke tekst: {{%/ notice%}}


```python
print(f"Den yngste person i datasættet er {min_age} år gammel, den ældste person i datasættet er {max_age} år gammel og gennemsnitsalderen er {mean_age} år.")
```

    Den yngste person i datasættet er 15 år gammel, den ældste person i datasættet er 100 år gammel og gennemsnitsalderen er 48.108521970705624 år.


{{% notice tip %}} Brug `np.round()` til at afrunde værdier: {{% /notice%}}


```python
mean_age_rounded = np.round(mean_age, decimals = 0)

print(f"Gennemsnitsalderen i datasættet er {mean_age_rounded} år.")
```

    Gennemsnitsalderen i datasættet er 48.0 år.


{{% /expand%}}

# {#Afsnit}Visualisering af data med seaborn

En god måde at udforske sit datasæt er ved at anvende visualiseringer. På den måde kan man visuelt orientere sig i, hvad data indeholder og hvordan data fordeler sig.

I dette afsnit bruges pakken `seaborn` til at danne visualiseringer. `seaborn` bygger ovenpå `matplotlib`, men giver visualiseringerne et mere moderne udseende, og giver flere muligheder for at passe visualiseringen til.

Fordi `seaborn` bygger ovenpå `matplotlib` skal begge biblioteker importeres (læg mærke til importkonventionerne). Derefter aktiveres `seaborn` med `sns.set()`. Når aktiveret erstatter `seaborn` standard `matplotlib` plots:


```python
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
```

{{%notice info%}} Linjen `%matplotlib inline` er en såkaldt "magic function". Den bruges, når man skriver Python i Jupyter Notebook, da den gør sådan, at plots printes direkte i notebooken. Hvis ikke den linje er kørt, vil plots dukke op i et vindue for sig (nogen gange er indstillingen dog sat til i forvejen).

{{/%notice%}}

Når man bruger `seaborn` sammen med `pandas` kan man lave visualiseringer/plots på to måder. Med den ene måde kalder man den specifikke visualiseringsfunktion fra seaborn og specificerer data, som skal bruges i visualisering. Med den anden måde referer man til den specifikke kolonne (series) fra dataframe, som man ønsker at visualisere og specificerer et plot (denne måde virker derfor kun til at visualisere én variabel).

## Plotting af series og dataframes

Der er en række metoder tilknyttet specifikt til pandas dataframe og series, så man kan danne et plot direkte fra.

### Histogram

`.plot.hist()` danner fx et histogram over variablen:


```python
sns.set(rc={'figure.figsize':(10,6)}) # Ændrer størrelsen af plots
ess2014['height'].plot.hist()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x296d23ba2e8>




![png](output_78_1.png)


Et histogram viser observationer som bjælker i intervaller sorteret efter værdi (lav til højest). På den måde kan man hurtigt danne sig et overblik over, hvordan data fordeler sig.

Af ovenstående ses fx at omkring 340 personer har en højde på omkring 168-173 cm. Desuden ses at meget få har en højde omkring 200 cm.

### Boxplot

`.plot.box()` danner et boxplot over variablen:


```python
ess2014['height'].plot.box()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x296d20d30b8>




![png](output_81_1.png)


Et boxplot er en anden måde at se på fordelingen af en variabel. Den vandrette linje i midten er middelværdien. De øvrige linjer angiver (fra top til bund): minimum, 1. kvartil, 3. kvartil, maksimum.

Metoden kan også anvendes på en dataframe:


```python
ess2014.plot.box()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x296d210c668>




![png](output_83_1.png)


Ovenstående plot giver ikke meget mening, da variable ikke har sammenlignelige værdier, hvorfor y-aksen bliver helt tosset.

Hvis man har et datasættet med flere variable med sammenlignelige værdier, kan man visualisere disse ved at dannet et subset af datasættet og lave et plot (mere om dette senere).

### Andre plots

Her er nogen andre plots, der kan dannes direkte på baggrund af en series (hvis variabeltypen tillader):

- `.plot.bar()`: Danner et barplot over variablen
- `.plot.pie()`: Danner et cirkelplotsover variablen
- `.plot.line()`: Danner et linjeplot 

Barplots og cirkelplots egner sig bedre til kategoriske variable. Dog er kategoriske variable i datasættet (fx `happy` og `ppltrst`) lige nu kodet på en måde, der ikke tillader at lave plots over dem.

Dette gennemgås senere.

## Plotting med seaborn

Plots kan også dannes ved først at refere specifikt til den plotting funtkion, som man vil bruge, og derefter specificere data.

Nedenstående linje danner et scatterplot for `height` og `weight`. Ved `seaborn` plottingfunktioner specificeres, hvilke værdier der skal udgøre x-aksen og hvilke, der skal udgøre y-aksen. `seaborn` forventer typisk series, så man kan specificere series direkte i funktionerne. Dog kan man også, som i nedenstående, specificere kolonne/variabelnavne og til sidst specificere data med argumentet `data = `:


```python
sns.scatterplot(data = ess2014, x = 'height', y = 'weight')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x296d23741d0>




![png](output_87_1.png)


Et scatterplot danner en prik for hver observations placering på to variable. Plottet egner sig derfor særdeles godt til at udforske umiddelbare sammenhænge (om en variabel er beslægtet med en anden).

Af ovenstående ses det, at vægt tenderer en smule til at stige i takt med højden (hvilket selvfølgelig ikke er overraskende).

---
## ØVELSE: Plotting

Dan et histogram over varialben `yrbrn` i ESS2014DK datasættet.

{{%expand "Løsning" %}}


```python
ess2014['yrbrn'].hist()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x296d21d05f8>




![png](output_90_1.png)


{{%/expand%}}

# {#Kapitel}Datahåndtering med pandas

Indtil videre er data blevet udforsket, som det er. Dog er et datasæt sjældent til at gå lige til, og vil ofte kræve forskellige håndteringer.

Typiske datahåndteringer inkluderer:

- Udvælge specifikke observationer af variable af datasættet, som er særligt relevante
- Rekode variable, fx ved at slå værdier sammen
- Danne nye variable, fx på baggrund af eksisterende variable
- Ændre typen af variabel, hvis den ikke kan læses ordentlig af Python

# {#Afsnit}Subsetting (draft)

"Subsetting" vil sige at udvælge specifikke dele af data.

Man subsetter pandas med metoderne `.loc()` og `.iloc()`. `.loc()` bruges til at subsette ud fra række- og kolonnenavne, mens `.iloc()` bruges til at subsette ud fra række- og kolnneindeks.

Format for subsetting: `data.loc[rækker, kolonner]`

Selekter bestemte rækker:


```python
ess2014.loc[2:10, :]
```




[TABLE 3]



Selekter bestemte kolonner (specificeres som en liste):


```python
ess2014.loc[:, ['gndr', 'alcfreq']].head()
```




[TABLE 4]



Selekter bestemte rækker og kolonner:


```python
ess2014.loc[2:10, ['gndr', 'alcfreq']]
```




[TABLE 5]



Selekter ud fra kolonneindeks:


```python
ess2014.iloc[2:10, [8, 6]]
```




[TABLE 6]



Bemærk at datasæt ikke ændres. Hvis subset skal gemmes, skal det gemmes i et nyt objekt (ny dataframe):


```python
ess2014_subset = ess2014.loc[2:10, ['gndr', 'alcfreq']]

ess2014_subset.head()
```




[TABLE 7]



## Subsetting med booleans (logiske værdier)

I stedet for at specificere indeksnumrene, kan man i stedet specificere betingelser:


```python
ess2014.loc[ess2014['height'] > 180, :].head()
```




[TABLE 8]




```python
ess2014.loc[(ess2014['height'] > 180) & (ess2014['gndr'] == 'Female'), :].head()
```




[TABLE 9]



---
## VIDENSCHECK

*Hvad er forskellen på `.loc[]` og `.iloc[]`?*

{{%expand "Løsning"%}}

`.loc[]` bruges til at selektere ud fra række- og kolonne*navne*.

`.iloc[]` bruges til at selektere ud fra række- og kolonne*indeks*.

Bemærk, at hvis rækker ikke har navne, referes blot til deres indeks med `.loc[]` også.

{{%/expand%}}

---

---

## ØVELSE: Selekter observationer

*Dan et subet bestående af mænd født efter 1980.*

{{%expand "Løsning"%}}


```python
ess2014_subset = ess2014.loc[(ess2014['gndr'] == 'Male') & (ess2014['yrbrn'] > 1980), :]

ess2014_subset.head()
```




[TABLE 10]



{{%/expand%}}

# {#Afsnit}Variabelgenerering og rekodning (draft)

## Variabelgenerering

Ofte har man brug for at tilføje oplysninger til et datasæt i form af nye variable.

Man danner en ny variabel blot ved at referere til et kolonnenavn, som endnu ikke er brugt.

I nedenstående dannes `height_m`; en variabel for højde i meter:


```python
ess2014['height_m'] = ess2014['height'] / 100

ess2014.head()
```




[TABLE 11]



---

## ØVELSE: Dan en aldersvariabel

*Tilføj en aldersvariabel til ESS2014DK datasættet (husk at data er fra 2014)*

{{%expand "Løsning"%}}


```python
ess2014['age'] = 2014 - ess2014['yrbrn']

ess2014.head()
```




[TABLE 12]



{{%/expand%}}

## Rekodning

Ofte har man brug for at rekode variable.

Variable rekodes ved at overskrive værdier i en eksisterende variabel.

Det er god praksis ikke at rekode de oprindelige variable i datasættet, så man vil i stedet lave en kopi af variablen og så rekode den i stedet.

Hvis man fx vil rekode en kontinuerlig variabel til kategorisk, kan man gøre brug af booleans. 

I nedenstående inddeles personer i datasættet i tre højde kategorier baseret på, om de har en højde under 1. kvartil ("short"), over 3. kvartil ("tall") eller midt imellem ("medium").


```python
quart1 = ess2014['height'].quantile(0.25)
quart3 = ess2014['height'].quantile(0.75)

ess2014['height_cat'] = np.nan # Danner en "tom" variabel bestående af missing

ess2014.loc[ess2014['height'] <= quart1, 'height_cat'] = "short"
ess2014.loc[(ess2014['height'] > quart1) & (ess2014['height'] < quart3), 'height_cat'] = "medium"
ess2014.loc[ess2014['height'] >= quart3, 'height_cat'] = "tall"

ess2014.head(10)
```




[TABLE 13]



Alternativt, hvis der bare skal deles i tre lige store grupper:


```python
ess2014['height_cat'] = pd.cut(ess2014['height'], 3, labels = ["short", "medium", "tall"])

ess2014.head(10)
```




[TABLE 14]



## Missingværdier

Missing værdier er angivet med `NaN`. Man kan undersøge, om en variabel indeholder missing, ved at bruge metoden `isnull()`:


```python
ess2014['cgtsday'].isnull().head()
```




    0    False
    1     True
    2     True
    3     True
    4     True
    Name: cgtsday, dtype: bool



Denne kan også bruges i `.loc[]`:


```python
ess2014.loc[ess2014['cgtsday'].isnull(), :].head()
```




[TABLE 15]



---
## ØVELSE: Rekodning

`cgtsday` angiver, hvor mange cigaretter om dagen personen ryger. Ud fra denne kan dannes en "ryger"-variabel.

*Dan en variabel, der angiver, hvorvidt personen ryger eller ej*

TIP: Brug `isnull()` og `notnull()` til at selektere missingværdier eller ikke-missingværdier

{{%expand "Løsning"%}}


```python
ess2014['smoker'] = np.nan

ess2014.loc[(ess2014['cgtsday'].isnull()) | (ess2014['cgtsday'] == 0), 'smoker'] = 'not a smoker'
ess2014.loc[ess2014['cgtsday'].notnull() | (ess2014['cgtsday'] > 0), 'smoker'] = 'smoker'

ess2014.head(10)
```




[TABLE 16]



{{%/expand%}}

# {#Afsnit}Variabeltyper (numerisk og tekst)

- Check: Hvilken variabeltype?
- Øvelse: Ændr variabeltype

# {#Kapitel}Kategoriske variable

# {#Afsnit}Typer af kategoriske variable (nominal, ordinal)

- Check: Er variabel ordinal eller nominal? ("teoretisk")

# {#Afsnit}Kategoriske variable i Python

- Check: Er variabel ordinal eller nominal? (kodning i python)
- Øvelse: Konverter fra karakter til kategorisk
- Øvelse: Konverter fra nominal til ordinal

# {#Afsnit}Rekodning af kategoriske variable

- Check: hvornår ændres variable ved rekodning?
- Øvelse: Rekod kategorisk med mapping

# {#Kapitel}Supplerende materiale

# {#Afsnit}Litteratur

- Python for Data Analysis, kap 5
- Python for Data Analysis, kap 9 - seaborn
- Python for Data Analysis, kap 12 - categorical

# {#END}