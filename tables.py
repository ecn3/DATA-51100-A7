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
pums_dataframe = pd.read_csv('ss13hil.csv')

# TABLE 1: Statistics of HINCP, grouped by HHT

# Get grouped
table1_grouped = pums_dataframe['HINCP'].groupby(pums_dataframe['HHT'])

# Function for getting each column in group
def get_table1(group):
    return {'mean':group.mean(),'std':group.std(),'count':group.count(),'min':group.min(),'max':group.max()}

# Apply to grouped to get stacked dataframe
table1_stacked = table1_grouped.apply(get_table1)

# HHT descriptions by value
hht_text_descriptions =  {
1.0:'Married couple household',
5.0:'Nonfamily household:Male householder:Not living alone',
7.0:'Nonfamily household:Female householder:Not living alone',
2.0:'Other family household:Male householder, no wife present',
3.0:'Other family household:Female householder, no husband present',
4.0:'Nonfamily household:Male householder:Living alone',
6.0:'Nonfamily household:Female householder:Living alone'}

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
# TODO Table should use the HHL types (text descriptions) as the index
# TODO Columns should be the text descriptions of ACCESS values
''' TODO  Each table entry is the sum of WGTP column for the given HHL/ACCESS combination, 
divided by the sum of WGTP values in the data.
Entries need to be formatted as percentages.
'''
# TODO Any rows containing NA values in HHL, ACCESS, or WGTP columns should be excluded.

# TABLE 3: Quantile Analysis of HINCP
# TODO Rows should correspond to different quantiles of HINCP: low (0-1/3), medium (1/3-2/3), high (2/3-1)
# TODO Columns displayed should be: min, max, mean, household_count
# TODO The household_count column contains entries with the sum of WGTP values for the corresponding range of HINCP values (low, medium, or high)

# OUTPUT

# Display the tables to the screen
# Header info
print("DATA-51100-002, SUMMER 2020")
print("Christian Nelson")
print("PROGRAMMING ASSIGNMENT #7\n")

# Table 1
print("*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***")
print(table1)

# Table 2
#print("*** Table 2 - HHL vs. ACCESS - Frequency Table ***\n")

# Table 3
#print("*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***\n")