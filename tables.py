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
table2_grouped =  table2_df.groupby(['HHL','ACCESS'])['WGTP']

def get_table_sums(group):
    return {'WGTP':group.sum()}

table2_stacked = table2_grouped.apply(get_table_sums) 
table2_stacked = table2_stacked/table2_df['WGTP'].sum()

table2 = table2_stacked.unstack(level=-1).unstack(level=-1)

# Convert HHL values to text descriptions
table2.rename(index=hhl_text_descriptions, inplace=True)

# Rename header
table2.index.names = ['HHL - Household language']

# Convert ACCESS values to text descriptions
table2.rename(columns=access_text_descriptions, inplace=True)

# Get sum column
table2_row_sums = table2['WGTP','Yes w/ Subsrc.']+table2['WGTP','Yes, wo/ Subsrc.']+table2['WGTP','No']
# Add sum_col to df
table2['WGTP','All'] = table2_row_sums

# Get sum row
table2.loc['All'] = table2.sum()

# Apply formatting to table2 values
table2['WGTP','Yes w/ Subsrc.'] = pd.Series(["{0:.2f}%".format(val * 100) for val in table2['WGTP','Yes w/ Subsrc.']], index = table2.index)
table2['WGTP','Yes, wo/ Subsrc.'] = pd.Series(["{0:.2f}%".format(val * 100) for val in table2['WGTP','Yes, wo/ Subsrc.']], index = table2.index)
table2['WGTP','No'] = pd.Series(["{0:.2f}%".format(val * 100) for val in table2['WGTP','No']], index = table2.index)
table2['WGTP','All'] = pd.Series(["{0:.2f}%".format(val * 100) for val in table2['WGTP','All']], index = table2.index)

# TABLE 3: Quantile Analysis of HINCP
# Get DataFrame drop NA values
table3_df = pums_df[['HINCP','WGTP']].dropna()

# Get Groupby
table3_grouped =  table3_df.groupby(pd.qcut(table3_df['HINCP'], 3, labels=["low", "medium", "high"]))


def get_table3_columns(group):
    return {'min':group.min(),'max':group.max(),'mean':group.mean(),'household_count':group['WGTP'].sum()}

# Apply to grouped to get stacked dataframe
table3_stacked = table3_grouped.apply(get_table3_columns)

# Get rid of range to clean quartile data
def get_cleaned_values(quartile):
    return {'min':quartile['min'][0],'max':quartile['max'][0],'mean':quartile['mean'][0].round(6),'household_count':quartile['household_count']}

# Reset values
table3_stacked['low'] = get_cleaned_values(table3_stacked['low'])
table3_stacked['medium'] = get_cleaned_values(table3_stacked['medium'])
table3_stacked['high'] = get_cleaned_values(table3_stacked['high'])


print(table3_stacked)

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
#print("                                              sum")
#print(table2)
# Table 3
#print("*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***\n")