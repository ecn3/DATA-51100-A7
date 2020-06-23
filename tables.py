# Christian Nelson
# 6/24/2020
# DATA-51100-002, SUMMER 2020
# PROGRAMMING ASSIGNMENT #7 tables

# Import Statements
import pandas as pd
from pandas import DataFrame
import numpy as np

# Output formating
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

# Load ss13hil.csv into a DATAFRAME
pums_dataframe = pd.read_csv('ss13hil.csv')

# TABLE 1: Statistics of HINCP, grouped by HHT
# TODO Table should use the HHT types (text descriptions) as the index
# TODO Columns should be: mean, std, count, min, max
# TODO Rows should be sorted by the mean column value in descending order

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
print("*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***\n")

# Table 2
print("*** Table 2 - HHL vs. ACCESS - Frequency Table ***\n")

# Table 3
print("*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***\n")