---
title: Introduktion til pandas
weight: 2
---
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
