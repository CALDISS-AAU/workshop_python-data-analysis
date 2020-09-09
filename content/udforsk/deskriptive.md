---
title: Deskriptive mål
weight: 1
---
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
