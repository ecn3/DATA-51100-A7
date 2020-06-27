import numpy as np
from pandas import Series, DataFrame
import pandas as pd

df = pd.DataFrame({'A': ['good', 'good', 'bad'], 'B' :[4,2,1], 'C':[10,10,10]})
df2 = pd.pivot_table(df, index=['A'], aggfunc=np.sum, margins=True)

print(df)
print(df2)