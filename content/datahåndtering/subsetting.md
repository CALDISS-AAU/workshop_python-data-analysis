---
title: Subsetting (draft)
weight: 1
---
Subsetting" vil sige at udvælge specifikke dele af data.

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
