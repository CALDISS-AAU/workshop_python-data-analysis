---
title: Typer af kategoriske variable (nominal, ordinal)
weight: 1
---
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

