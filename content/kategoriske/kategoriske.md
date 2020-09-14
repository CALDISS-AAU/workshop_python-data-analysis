---
title: Kategoriske variable i Python
weight: 2
---
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




![png](/output_209_1.png)


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




![png](/output_211_1.png)


{{%/expand%}}

---