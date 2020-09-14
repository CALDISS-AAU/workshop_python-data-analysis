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

ess2014 = pd.read_csv('https://github.com/CALDISS-AAU/workshop_python-data-analysis/raw/master/datasets/ESS2014DK_sub1.csv')
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



{[{TABLE 1}]}


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
    1         Good
    2         Good
    3    Very good
    4          Bad
    Name: health, dtype: object
    

Dog vil man typisk refere til enkeltkolonner på denne måde:


```python
print(ess2014['health'].head())
```

    0    Very good
    1         Good
    2         Good
    3    Very good
    4          Bad
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

1. Indlæs datasættet ESS2014DK_sub1 med `pd.read_csv()`. Funktionen kan indlæse data direkte fra et link (husk at importere pandas biblioteket).

    - Link til data: https://github.com/CALDISS-AAU/workshop_python-data-analysis/raw/master/datasets/ESS2014DK_sub1.csv
    
2. Brug `np.mean()` (`numpy.mean()`) til at udregne middelværdien af `height` variablen i datasættet. Hvad er middelværdien?



{{%expand "Løsning" %}} 


```python
import pandas as pd
import numpy as np

ess2014 = pd.read_csv('https://github.com/CALDISS-AAU/workshop_python-data-analysis/raw/master/datasets/ESS2014DK_sub1.csv')

print(np.mean(ess2014['height']))
```

    174.15887850467288
    

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




    0    167.0
    1    168.0
    2    182.0
    3    188.0
    4    156.0
    5    167.0
    6    169.0
    7    184.0
    8    182.0
    9    172.0
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
    1         Good
    2         Good
    3    Very good
    4          Bad
    5         Good
    6         Good
    7         Good
    8         Good
    9    Very good
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



{[{TABLE 2}]}


Metoden fungerer også på enkeltvariable:


```python
ess2014['weight'].describe()
```




    count    740.000000
    mean      76.178108
    std       15.597381
    min       43.000000
    25%       65.000000
    50%       74.500000
    75%       85.000000
    max      135.000000
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

Der knytter sig også en række metoder til at danne de enkelte deskriptive mål.

Herunder printes fx middelværdien, standardafvigelsen, minimums- og maksimumsværdien for variablen `weight`:


```python
import numpy as np

print(ess2014['weight'].mean())
print(ess2014['weight'].std())
print(ess2014['weight'].min())
print(ess2014['weight'].max())
```

    76.17810810810812
    15.597381262076514
    43.0
    135.0
    


```python
type(ess2014['weight'].std())
```




    float



Ovenstående værdier fortæller, at `weight` indeholder værdier fra 38.0 til 137.0 med en middelværdi på 75.86 og en standardafvigelse på 15.59 (middelværdien af de afstande, som hver observation afviger fra middelværdien).

## Deskriptive mål og kategoriske variable

Sammenlignes outputtet fra `.describe()` med indholdet af datasættet ses, at der ikke udregnes deskriptive mål for alle variable. 

Når `.describe()` bruges på et hel dataframe, udregnes kun mål for numeriske variabeltyper; altså variable, der kun består af tal.

Metoden kan dog også bruges på en kategorisk variabel som `ppltrst`:


```python
ess2014['ppltrst'].describe()
```




    count     749
    unique     11
    top         8
    freq      230
    Name: ppltrst, dtype: object



**Hvornår er en variabel kategorisk?**

Det kan måske give anledning til undren, hvorfor der fx ikke kan beregnes en middelværdi af `ppltrst`, da variablen umiddelbart indeholder tal:


```python
ess2014['ppltrst'].head()
```




    0                             4
    1    Most people can be trusted
    2                             5
    3                             8
    4                             4
    Name: ppltrst, dtype: object



Ved et nærmere kig viser det sig dog, at variablen også indeholder tekstværdier.

`.unique()` returnerer de unikke værdier i variablen:


```python
ess2014['ppltrst'].unique()
```




    array(['4', 'Most people can be trusted', '5', '8', '7', '9', '2', '6',
           '3', "You can't be too careful", '1', nan], dtype=object)



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
min_age = 2014 - ess2014['yrbrn'].max()
max_age = 2014 - ess2014['yrbrn'].min()
mean_age = 2014 - ess2014['yrbrn'].mean()

print(min_age, max_age, mean_age)
```

    15 100 47.67509986684422
    

{{% notice tip %}} Brug "f-strings" til at indsætte python-objekter direkte i et stykke tekst: {{%/ notice%}}


```python
print(f"Den yngste person i datasættet er {min_age} år gammel, den ældste person i datasættet er {max_age} år gammel og gennemsnitsalderen er {mean_age} år.")
```

    Den yngste person i datasættet er 15 år gammel, den ældste person i datasættet er 100 år gammel og gennemsnitsalderen er 47.67509986684422 år.
    

{{% notice tip %}} Brug `np.round()` (fra `numpy`) til at afrunde værdier: {{% /notice%}}


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




    <AxesSubplot:ylabel='Frequency'>




![png](output_76_1.png)


Et histogram viser observationer som bjælker i intervaller sorteret efter værdi (lav til højest). På den måde kan man hurtigt danne sig et overblik over, hvordan data fordeler sig.

Af ovenstående ses fx at omkring 340 personer har en højde på omkring 168-173 cm. Desuden ses at meget få har en højde omkring 200 cm.

Størrelsen på bjælkerne kan ændres med argumentet `bins = `:


```python
ess2014['height'].plot.hist(bins = 30)
```




    <AxesSubplot:ylabel='Frequency'>




![png](output_78_1.png)


### Boxplot

`.plot.box()` danner et boxplot over variablen:


```python
ess2014['height'].plot.box()
```




    <AxesSubplot:>




![png](output_80_1.png)


Et boxplot er en anden måde at se på fordelingen af en variabel. Den vandrette linje i midten er middelværdien. De øvrige linjer angiver (fra top til bund): minimum, 1. kvartil, 3. kvartil, maksimum.

Metoden kan også anvendes på en dataframe:


```python
ess2014.plot.box()
```




    <AxesSubplot:>




![png](output_82_1.png)


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




    <AxesSubplot:xlabel='height', ylabel='weight'>




![png](output_86_1.png)


Et scatterplot danner en prik for hver observations placering på to variable. Plottet egner sig derfor særdeles godt til at udforske umiddelbare sammenhænge (om en variabel er beslægtet med en anden).

Af ovenstående ses det, at vægt tenderer en smule til at stige i takt med højden (hvilket selvfølgelig ikke er overraskende).

---
## ØVELSE: Plotting

Dan et histogram over varialben `yrbrn` i ESS2014DK datasættet.

{{%expand "Løsning" %}}


```python
ess2014['yrbrn'].hist(bins = 30)
```




    <AxesSubplot:>




![png](output_89_1.png)


{{%/expand%}}

---

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



{[{TABLE 3}]}


Selekter bestemte kolonner (specificeres som en liste):


```python
ess2014.loc[:, ['gndr', 'alcfreq']].head()
```



{[{TABLE 4}]}


Selekter bestemte rækker og kolonner:


```python
ess2014.loc[2:10, ['gndr', 'alcfreq']]
```



{[{TABLE 5}]}


Selekter ud fra kolonneindeks:


```python
ess2014.iloc[2:10, [8, 5]]
```



{[{TABLE 6}]}


Bemærk at datasæt ikke ændres. Hvis subset skal gemmes, skal det gemmes i et nyt objekt (ny dataframe):


```python
ess2014_subset = ess2014.loc[2:10, ['gndr', 'alcfreq']]

ess2014_subset.head()
```



{[{TABLE 7}]}


## Subsetting med booleans (logiske værdier)

I stedet for at specificere indeksnumrene, kan man i stedet specificere betingelser:


```python
ess2014.loc[ess2014['height'] > 180, :].head()
```



{[{TABLE 8}]}



```python
ess2014.loc[(ess2014['height'] > 180) & (ess2014['gndr'] == 'Female'), :].head()
```



{[{TABLE 9}]}


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



{[{TABLE 10}]}


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



{[{TABLE 11}]}


---

## ØVELSE: Dan en aldersvariabel

*Tilføj en aldersvariabel til ESS2014DK datasættet (husk at data er fra 2014)*

{{%expand "Løsning"%}}


```python
ess2014['age'] = 2014 - ess2014['yrbrn']

ess2014.head()
```



{[{TABLE 12}]}


{{%/expand%}}

---

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



{[{TABLE 13}]}


Alternativt, hvis der bare skal deles i tre lige store grupper:


```python
ess2014['height_cat'] = pd.cut(ess2014['height'], 3, labels = ["short", "medium", "tall"])

ess2014.head(10)
```



{[{TABLE 14}]}


## Missingværdier

Missing værdier er angivet med `NaN`. Man kan undersøge, om en variabel indeholder missing, ved at bruge metoden `isnull()`:


```python
ess2014['cgtsday'].isnull().head()
```




    0     True
    1     True
    2    False
    3     True
    4     True
    Name: cgtsday, dtype: bool



Denne kan også bruges i `.loc[]`:


```python
ess2014.loc[ess2014['cgtsday'].isnull(), :].head()
```



{[{TABLE 15}]}


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



{[{TABLE 16}]}


{{%/expand%}}

# {#Afsnit}Variabeltyper (numerisk og tekst)

Ligesom Python generelt adskiller mellem typer af objekter, har hver kolonne (series) i en data frame også en type.

Typen kan tjekkes med `.dtypes`; enten for hele datasættet eller en enkelt kolonne.


```python
ess2014['height'].dtypes
```




    dtype('float64')




```python
ess2014.dtypes
```




    idno             int64
    ppltrst         object
    happy           object
    health          object
    cgtsday        float64
    alcfreq         object
    height         float64
    weight         float64
    gndr            object
    yrbrn            int64
    height_m       float64
    age              int64
    height_cat    category
    smoker          object
    dtype: object



Af ovenstående ses at datasættet indeholder typerne `int64` (integer/heltal), `float64` ("float point"/decimaltal) og `object`. 

`object` typen bruges, når kolonnen både indeholder tekst og tal. På den måde mistes ikke noget information ved indlæsning Typen kan give problemer, da mange funktioner og metoder forventer enten en ren numerisk kolonne eller ren tekst/kategorisk kolonne. Det hænder også, at variable kun med tekst indlæses som `object`.

Man bør altid undersøge variable af typen `object` nærmere og se, om en anden type er mere passende (numerisk, tekst/karakter eller kategorisk). Dette fordi at `object`-typen fortæller meget lidt om, hvad data indeholder, hvor de andre typer med det samme fortæller, hvilken type data, som kolonnen indeholder.

## Ændring af variabeltype

Kolonnetypen ændres med metoden `.astype()`:

- `astype('string')`: Konverter til string (tekstværdier)
- `astype('categorical')`: Konverter til kategorisk
- `astype('int')`: Til heltal
- `astype('float')`: Til decimaltal

**Konvertering til tekst**

Tjek hvilke værdier kolonnen indeholder:


```python
ess2014['gndr'].unique()
```




    array(['Female', 'Male'], dtype=object)



Kolonnen indeholder værdierne "Male" og "Female"; en kategorisk variabel bestående kun af tekst-værdier. Den kan derfor lige så godt konverteres til teksttype.

Konvertering af kolonne til tekst gøres med `.astype('string')`:


```python
ess2014['gndr'] = ess2014['gndr'].astype('string')
```

Typen er nu string/tekst (`StringDtype`):


```python
ess2014['gndr'].dtypes
```




    StringDtype



{{%notice note%}} Variable med afgrænsede tekstværdier er kategoriske variable, og det giver ofte mere mening at konvertere disse til kategorisk frem for tekst. Dette gennemgås senere i dette materiale.
{{%/notice%}}

**Konvertering til numerisk**

`yrbrn` konverteres til tekst for at have en variabel at konvertere til tal.

Tjek først typen:


```python
ess2014['yrbrn'].dtypes
```




    dtype('int64')



Typen er `int64` (decimaltal). Konverter til tekst:


```python
ess2014['yrbrn'] = ess2014['yrbrn'].astype('string')
```

Tjek at typen er string:


```python
ess2014['yrbrn'].dtypes
```




    StringDtype



Konvertering til heltal igen - Gøres med `.astype('int')`:


```python
ess2014['yrbrn'] = ess2014['yrbrn'].astype('int')
```

Tjek at typen er ændret tilbage:


```python
ess2014['yrbrn'].dtypes
```




    dtype('int32')



**Konverter kolonne med blanding af typer**

Ofte kan man rende ind i, at en kolonne indeholder en blanding af typer.

Det gælder fx for `ppltrst` og `happy`.

Tjek hvilke værdier kolonnen indeholder:


```python
ess2014['ppltrst'].unique()
```




    array(['4', 'Most people can be trusted', '5', '8', '7', '9', '2', '6',
           '3', "You can't be too careful", '1', nan], dtype=object)



Variablen indeholder både tal og tekst. Hvis der konverteres til tal, gives der fejl:


```python
ess2014['ppltrst'] = ess2014['ppltrst'].astype('int')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-67-8b2ee5027ea0> in <module>
    ----> 1 ess2014['ppltrst'] = ess2014['ppltrst'].astype('int')
    

    C:\programs\Continuum\anaconda3\lib\site-packages\pandas\core\generic.py in astype(self, dtype, copy, errors)
       5535         else:
       5536             # else, only a single dtype is given
    -> 5537             new_data = self._mgr.astype(dtype=dtype, copy=copy, errors=errors,)
       5538             return self._constructor(new_data).__finalize__(self, method="astype")
       5539 
    

    C:\programs\Continuum\anaconda3\lib\site-packages\pandas\core\internals\managers.py in astype(self, dtype, copy, errors)
        593         self, dtype, copy: bool = False, errors: str = "raise"
        594     ) -> "BlockManager":
    --> 595         return self.apply("astype", dtype=dtype, copy=copy, errors=errors)
        596 
        597     def convert(
    

    C:\programs\Continuum\anaconda3\lib\site-packages\pandas\core\internals\managers.py in apply(self, f, align_keys, **kwargs)
        404                 applied = b.apply(f, **kwargs)
        405             else:
    --> 406                 applied = getattr(b, f)(**kwargs)
        407             result_blocks = _extend_blocks(applied, result_blocks)
        408 
    

    C:\programs\Continuum\anaconda3\lib\site-packages\pandas\core\internals\blocks.py in astype(self, dtype, copy, errors)
        587             vals1d = values.ravel()
        588             try:
    --> 589                 values = astype_nansafe(vals1d, dtype, copy=True)
        590             except (ValueError, TypeError):
        591                 # e.g. astype_nansafe can fail on object-dtype of strings
    

    C:\programs\Continuum\anaconda3\lib\site-packages\pandas\core\dtypes\cast.py in astype_nansafe(arr, dtype, copy, skipna)
        964         # work around NumPy brokenness, #1987
        965         if np.issubdtype(dtype.type, np.integer):
    --> 966             return lib.astype_intsafe(arr.ravel(), dtype).reshape(arr.shape)
        967 
        968         # if we have a datetime/timedelta array of objects
    

    pandas\_libs\lib.pyx in pandas._libs.lib.astype_intsafe()
    

    ValueError: invalid literal for int() with base 10: 'Most people can be trusted'


Variablen er en skala fra 0-10, så den kan i princippet behandles som numerisk. Det kræver bare, at værdierne ændres sådan, at variablen kan tvinges om.

- "Most people can be trusted" skal være "10"
- "You can't be too careful" skal være "0"

Værdier kan erstattes med metoden `.replace()`. Her ændres oplysninger i datasættet, hvorfor man altid bør lave en ny variabel:


```python
ess2014['ppltrst_num'] = ess2014['ppltrst']
```

Nu kan værdierne erstattes i den nye variabel med `replace()`. Metoden skal bruge en dictionary, hvor nøglerne består af værdierne, som skal ændres, og værdierne skal være de værdier, som skal ændres.


```python
ess2014['ppltrst_num'] = ess2014['ppltrst_num'].replace({"Most people can be trusted": "10", "You can't be too careful": "0"})
```

Variabel indeholder nu værdierne "0" og "10".


```python
ess2014['ppltrst_num'].unique()
```




    array(['4', '10', '5', '8', '7', '9', '2', '6', '3', '0', '1', nan],
          dtype=object)



Variablen kan nu konverteres til tal (der konverteres til float/decimaltal, da missingværdier (`NaN`) ikke kan være heltal):


```python
ess2014['ppltrst_num'] = ess2014['ppltrst_num'].astype('float')
```

Variablen er nu numerisk, så man fx kan foretage beregninger:


```python
ess2014['ppltrst_num'].mean()
```




    6.998664886515354



### Lad pandas gætte typen

Metoden `convert_dtypes()` bruges til at lade pandas gætte den mest passende type


```python
ess2014['alcfreq'].dtypes
```




    dtype('O')



Variabeltypen er 'O' (for `object`).


```python
ess2014['alcfreq'] = ess2014['alcfreq'].convert_dtypes()
```

Tjek hvilken type pandas har konverteret til ved at gætte:


```python
ess2014['alcfreq'].dtypes
```




    StringDtype



Pandas gætter typen til at være string.

---

# ØVELSE: Ændr variabeltypen

1. Check hvilken type variabel `happy` er med `.dtypes`.

2. Variablen kan laves til numerisk. Lav en kopi af variablen (evt. kald den `happy_num`).

3. Rekod tekstværdierne til tal med `.replace()` - Husk at rekodninger skal specificeres som en dictionary ( `{"gammel værdi": "ny værdi", "gammel værdi": "ny værdi"}` ).
    - "Extremely happy" skal kodes til "10"
    - "Extremely unhappy" skal kodes til "0"
    
4. Konverter variablen til numerisk med `.astype('float')`.

5. Udregn gennemsnit for variablen med `.mean()`.

{{%expand "Løsning"%}}


```python
print(ess2014['happy'].dtypes)

ess2014['happy_num'] = ess2014['happy']
ess2014['happy_num'] = ess2014['happy_num'].replace({"Extremely happy": "10", "Extremely unhappy": "0"})
ess2014['happy_num'] = ess2014['happy_num'].astype('float')

print(ess2014['happy_num'].dtypes)

ess2014['happy_num'].mean()
```

    object
    float64
    




    8.278666666666666



{{%/expand %}}

---

# {#Kapitel}Kategoriske variable

Variable, der har en afgrænset mængde svarmuligheder, kaldes for kategoriske.

# {#Afsnit}Typer af kategoriske variable (nominal, ordinal)

Man adskiller mellem to typer af kategoriske variable.

**Ordinale**

Ordinalt skalerede variable er variable, som kan rangordnes; altså hvor der kan differentieres hierarkisk mellem værdierne.

Af ESS2014 datasættet er `health` et eksempel på en ordinal-skaleret variabel.


```python
ess2014['health'].unique()
```




    array(['Very good', 'Good', 'Bad', 'Fair', 'Very bad', nan], dtype=object)



Variablen indeholder personens egen vurdering af helbred. 

Den er kategorisk, da man kun kan vælge mellem i forvejen definerede svarmuligheder. 

Den er ordinal, da man kan rangere værdierne: "Good" er bedre end "Bad", "Very bad" er værre end "Fair" osv.

**Nominale**

Nominalt skalerede variable er variable, som *ikke* kan rangordnes.

I ESS2014 datasættet er `gndr` et eksempel på en nominal-skaleret variabel:


```python
ess2014['gndr'].unique()
```




    <StringArray>
    ['Female', 'Male']
    Length: 2, dtype: string



**Talværdier og kategoriske variable**

Selvom en variabel indeholder talværdier, kan de stadig godt være kategoriske.

Et centralt karakteristika ved ikke-kategoriske (kontinuerlige) variable er, at man kan måle den præcise afstand mellem målinger. Det kan man fx for variable som `height` og `weight`.

Ved variable som `ppltrst` og `happy` kan man ikke måle den præcise afstand. Selvom man kan sige, at 8 er større end 4 og man kan regne en difference mellem to personers score på disse variable, så er det stadig ikke en præcis afstand som regnes.

Herunder vises fx værdierne for `ppltrst` for rækkeindeks 27 og 90:


```python
ess2014.loc[[27, 90], 'ppltrst']
```




    27    8
    90    9
    Name: ppltrst, dtype: object



Her ses, at række 90 svarer 9 og række 27 svarer 8. Man kan derfor godt udregne, at række 90 har givet en højere score en række 27.

Dog kan det argumenteres, at det ikke er den præcise afstand der regnes, da der er tale om en skala for, hvor meget man stoler på andre mennesker. Talværdien er derfor svær at omsætte til noget faktisk (hvor meget tillid er fx en score på 8 frem for en score på 9?), og hvordan spørgsmålet og skalaen tolkes vil variere fra person til person (er mængden af tillid, som den ene person tildeler en score på 8 den samme mængde, som en anden person tildeler en score på 8?).

Af denne grund er sådanne variable som udgangspunkt kategoriske. Det ses dog ofte, at sådanne variable behandles som numeriske alligevel, da det er nødvendigt for mange typer analyser.

---

## VIDENSCHECK

*Er variablen `alcfreq` ordinalt eller nominalt skaleret?*

{{%expand "Løsning"%}}
`alcfreq` er en ordinalt skaleret variabel, da værdierne kan rangordnes.
{{%/expand%}}

---


# {#Afsnit}Kategoriske variable i Python

Python/Pandas kan ikke selv gætte sig til, hvad der er kategorisk, da de blot ligner tekst, set fra Pythons synspunkt.

Når man arbejder med kategoriske variable i Python, skal man derfor selv kode dem om til at være kategorisk

Variable kodes til kategoriske med `astype('category')`. Herunder kodes `health` om til kategorisk, da det er en kategorisk variabel:


```python
ess2014['health'] = ess2014['health'].astype('category')
```

Når man kigger på variablen nu ses, at den er ændret til typen `category`. Derudover vises, hvilke kategorier variablen har.


```python
ess2014['health'].head()
```




    0    Very good
    1         Good
    2         Good
    3    Very good
    4          Bad
    Name: health, dtype: category
    Categories (5, object): ['Bad', 'Fair', 'Good', 'Very bad', 'Very good']



Variable kodes som standard til nominalt skalerede variable. Dette kan ses, ved at kigge på `dtypes`, hvor `ordered` angiver, om variablen er kodet nominalt eller ordinalt (`ordered = False` for nominalt, `ordered = True` for ordinalt):


```python
ess2014['health'].dtypes
```




    CategoricalDtype(categories=['Bad', 'Fair', 'Good', 'Very bad', 'Very good'], ordered=False)



## Konvertering til ordinal

For at konvertere til ordinal, skal man specificere sig egen type, som kan sættes på variablen.

Indtil videre er der gennemgået forskellige "indbyggede" typer: `int`, `float`, `string`, `category`. Men det er også muligt at genere sin egen type.

Dette er nødvendigt for at kode en variabel ordinal. Man gør følgende:

- Dan et `CategoricalDtype` objekt
- Specificer kategorierne som liste i argumentet `categories = ` (sørg for at skrive dem i rækkefølge fra lav til høj, hvis ordinal)
- Specificer hvorvidt variablen er ordinal eller nominal med `ordered = True/False`

Herunder dannes kateogi-objektet, som kan bruges til `health`. `CategoricalDtype` skal importeres, før den kan bruges:


```python
from pandas.api.types import CategoricalDtype

health_cat = CategoricalDtype(categories = ['Very bad', 'Bad', 'Fair', 'Good', 'Very good'], ordered = True)
```

Kategoriobjektet er nu dannet, men er ikke tilknyttet variablen:


```python
health_cat
```




    CategoricalDtype(categories=['Very bad', 'Bad', 'Fair', 'Good', 'Very good'], ordered=True)



Kategoriobjektet tilknyttes med `astype()`:


```python
ess2014['health'] = ess2014['health'].astype(health_cat)
```

`health` er nu kodet som ordinal - læg mærke til hvordan rækkefølge er angivet med `<`:


```python
ess2014['health'].unique()
```




    ['Very good', 'Good', 'Bad', 'Fair', 'Very bad', NaN]
    Categories (5, object): ['Very bad' < 'Bad' < 'Fair' < 'Good' < 'Very good']



---

## ØVELSE: Konverter til kategorisk

1. Tag et kig på variablen `alcfreq`. Er variablen nominal eller ordinal?

2. Rekod `alcfreq` til at være kategorisk. Hvis den er ordinal, så dan et kategoriobjekt, som kan bruges til at kode variablen (tjek værdier i variablen med `.unique()`

{{%expand "Løsning"%}}


```python
ess2014['alcfreq'].unique() # Tjek værdier for at se, hvordan variablen er kodet (ordinalt)

alc_cat = CategoricalDtype(categories = ['Never', 'Less than once a month', 'Once a month',   # Danner kategoriobjekt
                                         '2-3 times a month', 'Once a week', 'Several times a week', 
                                         'Every day'], ordered = True)

ess2014['alcfreq'] = ess2014['alcfreq'].astype(alc_cat) # Ændrer typen

ess2014['alcfreq'].unique() # Bekræfter ændringen
```




    ['Never', 'Several times a week', 'Once a week', 'Every day', 'Less than once a month', 'Once a month', '2-3 times a month', NaN]
    Categories (7, object): ['Never' < 'Less than once a month' < 'Once a month' < '2-3 times a month' < 'Once a week' < 'Several times a week' < 'Every day']



{{%/expand%}}

---


## Hvorfor rekode til ordinal?

Rekodning til ordinal gøres ikke kun for syns skyld. Når man fortæller Python, at en variabel skal behandles som ordinal, kan man bruge rangordnen, når man arbejder med data.

Fx kan man nu filtrere ESS2014 datasættet efter, hvor mange der har et selvvurderet helbred på `Fair` eller mindre:


```python
ess2014.loc[ess2014['health'] <= 'Fair', :].head()
```



{[{TABLE 17}]}


## Rekodning af kategoriske variable

Kategoriske variable rekodes ligesom tekstvariable med `.replace()`.

Man kan med fordel specificere den dictionary, som skal rekodes efter, først, da man derved har den til rådighed, hvis fx flere variable skal rekodes på samme måde.

I nedenstående dannes en ny `alcfreq` variabel, der inddeler respondenter efter, om de drikker mindst en gang om ugen, mindre end en gang om ugen eller aldrig. Læg mærke til, hvordan værdier slås sammen på denne måde:


```python
ess2014['alcfreq'].unique()
```




    ['Never', 'Several times a week', 'Once a week', 'Every day', 'Less than once a month', 'Once a month', '2-3 times a month', NaN]
    Categories (7, object): ['Never' < 'Less than once a month' < 'Once a month' < '2-3 times a month' < 'Once a week' < 'Several times a week' < 'Every day']




```python
alc_recodedict = {'Several times a week': 'Once a week or more', 'Once a week': 'Once a week or more', 
                  'Every day': 'Once a week or more', 'Less than once a month': 'Less than once a week', 
                 'Once a month': 'Less than once a week', '2-3 times a month': 'Less than once a week'}

ess2014['alcfreq_3cat'] = ess2014['alcfreq'].replace(alc_recodedict)
```

Værdierne er nu ændret i den nye variabel. Bemærk, at typen konverteres tilbage til `object`. Det er derfor en fordel at rekode værdier *inden* man konverterer variablen til en kategorisk type.


```python
ess2014['alcfreq_3cat'].unique()
```




    array(['Never', 'Once a week or more', 'Less than once a week', nan],
          dtype=object)




```python
ess2014.head()
```



{[{TABLE 18}]}


## Plotting a kategoriske variable

Forskellige plots kan dannes pba. kategoriske. Få plots kan laves direkte på kategoriske, men skal i stedet laves på optællinger.

`.value_counts()` tæller værdier op i en variabel:


```python
ess2014['health'].value_counts()
```




    Very good    298
    Good         266
    Fair         146
    Bad           29
    Very bad      11
    Name: health, dtype: int64



`value_counts()` kan plottes direkte med fx `.plot.bar()`:


```python
ess2014['health'].value_counts().plot.bar()
```




    <AxesSubplot:>




![png](output_209_1.png)


---

## ØVELSE: Rekod kategorisk

1. Dan en varibel, der består af variablen `health` rekodet til at indeholde kategorierne "Good", "Fair" og "Bad".
    - "Very good" rekodes til "Good"
    - "Very bad" rekodes til "Bad"

2. (valgfri) Rekod variablen til at være ordinal

3. Dan et cirkelplot af den rekodede variabel med `.plot.pie()` (husk at brug `value_counts()`)

{{%expand "Løsning"%}}



```python
health_recodedict = {'Very good': 'Good', 'Very bad': 'Bad'}

health_cat3 = CategoricalDtype(categories = ['Bad', 'Fair', 'Good'], ordered = True)

ess2014['health_3cats'] = ess2014['health'].replace(health_recodedict)
ess2014['health_3cats'] = ess2014['health_3cats'].astype(health_cat3)

ess2014['health_3cats'].value_counts().plot.pie()
```




    <AxesSubplot:ylabel='health_3cats'>




![png](output_211_1.png)


{{%/expand%}}

---

# {#Kapitel}Supplerende materiale

# {#Afsnit}Litteratur

- McKinney, W 2018: *Python for Data Analysis*, kapitel 5, side 125-167

- McKinney, W 2018: *Python for Data Analysis*, kapitel 9, side 257-292

- McKinney, W 2018: *Python for Data Analysis*, kapitel 12, side 369-378

# {#Afsnit}Nyttige links

**DataCamp: *Python for Data Science Cheat Sheet - Pandas Basics*** - https://datacamp-community-prod.s3.amazonaws.com/dbed353d-2757-4617-8206-8767ab379ab3

**The Pandas Development Team: *10 Minutes to Pandas*** - https://pandas.pydata.org/docs/user_guide/10min.html#min

**Waskom, Michael: *An introduction to seaborn*** - https://seaborn.pydata.org/introduction.html

# {#END}
