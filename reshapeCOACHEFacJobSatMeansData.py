# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:28:29 2025

Read COACHE Means and Frequency Tables and Reformat

@author: Janet Lee jlee6@clemson.edu
"""

import pandas as pd
import glob

outputFile = 'data/output.xlsx'

cdf = pd.DataFrame()

# path to directory containing all the downloaded csv files from the COACHE report website
directory = 'data/means/'
allFilenames = glob.glob(directory + '*.xlsx')
df = pd.concat(pd.read_excel(filename, header=[0, 1, 2], index_col=[0, 1, 2]) for filename in allFilenames)

### Reshape data and drop non-data rows/columns

# Drop any rows where "Total New Ads" is not a number (NaN)
#df = df.dropna(subset=['Total New Ads'])

# Reset index so that we can use the Date as a column
#df = df.reset_index()

# Drop column where the index value is 'Total New Ads'
#df = df.drop(columns='Total New Ads')

# Melt the DataFrame to long format
#df = df.melt(id_vars='Hard Skills', var_name='Date', value_name='Quarterly Count')
#df = df.rename(columns={'Hard Skills':'Hard Skill'})

# output to Excel, include index
df.to_excel(outputFile, index=True)