---
title: Introduktion til pandas
weight: 2
---
pandas` (https://pandas.pydata.org/) er et Python bibliotek til datahåndtering og dataanalyse. Pandas egner sig særligt til data i tabeller struktureret i rækker og kolonner. En datatabel kaldes inden for pandas en "DataFrame"; et bestemt Python objekt specifikt til at lagre og bearbejde data i tabeller.

Denne lektion gennemgår diverse basale funktioner til at indlæse, udforske og håndtere en pandas DataFrame. Se også den officielle dokumentation for flere guides, introduktioner og beskrivelser til at arbejde med pandas: https://pandas.pydata.org/docs/

## Indlæsning af data med pandas

`pandas` pakken indeholder funktioner til at indlæse data i forskellige formater; herunder CSV, JSON, Excel, Stata, SAS osv.

I det nedenstående indlæses pandas biblioteket, hvorefter datasættet "ESS2014DK_subset.csv" indlæses. Biblioteket `numpy` indlæses også, da det indeholder en række brugbare funktioner til at foretage beregninger på pandas dataframes:


```python
import numpy as np
import pandas as pd

ess2014 = pd.read_csv('https://github.com/CALDISS-AAU/workshop_python-data-analysis/raw/master/data/ESS2014DK_subset.csv')
```

{{% notice note %}}
Bemærk importkonventionerne for `numpy` og `pandas`. `numpy` importeres typisk som `np` og `pandas` typisk som `pd`.
{{% /notice%}}

{{% notice info %}}
Datasættet, som indlæses her, er et uddrag af datasættet fra European Social Survey (ESS) 2014. ESS er en europæisk surveyundersøgelse, der gentages hvert andet år. Surveyet behandler spørgsmål om folks helbred, beskæftigelse, politiske holdninger, tillid osv. I dette uddrag er der kun inkluderet de danske respondenter og et mindre udpluk variable.
{{% /notice%}}


```python

```
