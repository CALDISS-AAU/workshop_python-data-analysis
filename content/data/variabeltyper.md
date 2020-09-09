---
title: Variabeltyper
weight: 3
---
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