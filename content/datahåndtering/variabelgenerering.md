---
title: Variabelgenerering og rekodning (draft)
weight: 2
---
Variabelgenerering

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
