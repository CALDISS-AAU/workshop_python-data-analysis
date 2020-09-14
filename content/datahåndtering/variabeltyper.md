---
title: Variabeltyper (numerisk og tekst)
weight: 3
---
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