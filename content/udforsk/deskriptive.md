---
title: Deskriptive mål
weight: 1
---
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
