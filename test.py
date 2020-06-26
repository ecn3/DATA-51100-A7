import numpy as np
from pandas import Series, DataFrame
import pandas as pd

# Set up an example DataFrame
df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'], 'key2' : ['one', 'two', 'one', 'two', 'one'],'data1' : np.random.randn(5),'data2' : np.random.randn(5)})

# Split data1 values into groups by key1
grouped = df['data1'].groupby(df['key1'])

# Function to find some stats for each group
def get_range_and_mean(a):
    return Series([a.max()-a.min(), a.mean()], index=['range','mean'])

# Function to do some transformations
def f(group):
    return pd.DataFrame({'original' : group, 'demeaned' : group - group.mean()})

# Function to get more stats
def get_stats(group):
    return {'min': group.min(), 'max': group.max(), 'count': group.count(), 'mean': group.mean()}

# Apply and combine
print grouped.apply(f)
print grouped.apply(get_range_and_mean)
print grouped.apply(get_stats)


