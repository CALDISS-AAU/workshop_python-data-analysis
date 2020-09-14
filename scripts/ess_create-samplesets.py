# This scripts produces sample data for workshop "Python for Data Analysis"
# It introduces 500 missing values into the data sets and splits data into 2

import pandas as pd
import numpy as np
import random

# Read the data
ess = pd.read_csv('https://github.com/CALDISS-AAU/workshop_python-data-analysis/raw/master/datasets/ESS2014DK_subset.csv')

# Setting seed for random functions
random.seed(422)

# Define simple function for adding missing
def introduce_missing(df, nan_n):
    df_withna = df.copy()
    for i in range(0, nan_n, 1):
        random_row = random.randint(0, df.shape[0]-1)
        random_col = random.randint(1, df.shape[1]-1)
        df_withna.iloc[random_row, random_col] = np.NaN
    
    return(df_withna)

# Create copy of dataset with missing values
ess_withnan = introduce_missing(ess, 500)

# Divide row indexes
rows = list(range(0, ess.shape[0], 1))
rows1 = random.sample(rows, int(ess.shape[0]/2))
rows2 = [row for row in rows if row not in rows1]

# Create subsets
ess1 = ess.loc[rows1, :]
ess2 = ess.loc[rows2, :]

# Save subsets
ess1.to_csv('../datasets/ESS2014DK_sub1.csv')
ess2.to_csv('../datasets/ESS2014DK_sub2.csv')