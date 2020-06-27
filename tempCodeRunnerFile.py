# Christian Nelson
# 6/24/2020
# DATA-51100-002, SUMMER 2020
# PROGRAMMING ASSIGNMENT #7 tables

# Import Statements
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# Output formating
pd.options.display.max_colwidth = 100

# Load ss13hil.csv into a DATAFRAME
pums_df = pd.read_csv('ss13hil.csv')

# TABLE 1: Statistics of HINCP, grouped by HHT

# Get grouped
table1_grouped = pums_df['HINCP'].groupby(pums_df['HHT'])

# Function for getting each column in group
def get_table1(group):
    return {'mean':group.mean(),'std':group.std(),'count':group.count(),'min':group.min(),'max':group.max()}

# Apply to grouped to get stacked dataframe
table1_stacked = table1_grouped.apply(get_table1)

# HHT descriptions by value
hht_text_descriptions =  {
1:'Married couple household',
2:'Other family household:Male householder, no wife present',
3:'Other family household:Female householder, no husband present',
4:'Nonfamily household:Male householder:Living alone',
5:'Nonfamily household:Male householder:Not living alone',
6:'Nonfamily household:Female householder:Living alone',
7:'Nonfamily household:Female householder:Not living alone'}

# Convert HHT values to text descriptions
table1_stacked.rename(index=hht_text_descriptions, inplace=True)

# unstack dataframe
table1 = table1_stacked.unstack(level=-1)

# Sort by mean column descending
table1.sort_values('mean',ascending=False, inplace=True)

# Rename header
table1.index.names = ['HHT - Household/family type']

# Rearrange columns
table1 = table1[['mean','std','count','min','max']]

# Get rid of decimals on count min max
table1['count'] = table1['count'].astype(int)
table1['min'] = table1['min'].astype(int)
table1['max'] = table1['max'].astype(int)


# TABLE 2: HHL vs. ACCESS

# Get DataFrame drop NA values
table2_df = pums_df[['HHL','ACCESS','WGTP']].dropna()

# HHL descriptions by value
hhl_text_descriptions =  {
1:'English only',
2:'Spanish',
3:'Other Indo-European languages',
4:'Asian and Pacific Island languages',
5:'Other language'}

# ACCESS descriptions by value
access_text_descriptions =  {
1:'Yes w/ Subsrc.',
2:'Yes, wo/ Subsrc.',
3:'No'}

# Get Groupby
table2_grouped =  table2_df.groupby(['HHL','ACCESS']).sum()/table2_df['WGTP'].sum()
# unstack dataframe
table2 = table2_grouped.unstack(level=-1)

#tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker', margins=True)

# Convert HHL values to text descriptions
table2.rename(index=hhl_text_descriptions, inplace=True)

# Rename header
table2.index.names = ['HHL - Household language']

# Convert ACCESS values to text descriptions
table2.rename(columns=access_text_descriptions, inplace=True)


print(table2)



# TABLE 3: Quantile Analysis of HINCP
# TODO Rows should correspond to different quantiles of HINCP: low (0-1/3), medium (1/3-2/3), high (2/3-1)
# TODO Columns displayed should be: min, max, mean, household_count
# TODO The household_count column contains entries with the sum of WGTP values for the corresponding range of HINCP values (low, medium, or high)

# OUTPUT

# Display the tables to the screen
# Header info
#print("DATA-51100-002, SUMMER 2020")
#print("Christian Nelson")
#print("PROGRAMMING ASSIGNMENT #7\n")

# Table 1
#print("*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***")
#print(table1)

# Table 2
#print("*** Table 2 - HHL vs. ACCESS - Frequency Table ***\n")

# Table 3
#print("*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***\n")