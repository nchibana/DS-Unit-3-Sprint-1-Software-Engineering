import pandas as pd
import numpy as np

def contingency(df, feature1, feature2):
  contingency_table = pd.crosstab(
      df[feature1],
      df[feature2],
      margins = True)
  
  row_sums = contingency_table.iloc[0:contingency_table.shape[0]-1,contingency_table.shape[1]-1].values
  col_sums = contingency_table.iloc[contingency_table.shape[0]-1,0:contingency_table.shape[1]-1].values
  total = contingency_table.loc['All', 'All']
  expected = []
  for i in range(len(row_sums)):
    expected_row = []
    for column in col_sums:
      expected_val = column*row_sums[i]/total
      expected_row.append(expected_val)
    expected.append(expected_row)
    
  contingency_no_margins = pd.crosstab(df[feature1], df[feature2])
  contingency = contingency_no_margins.values
  chi_squared = ((contingency - expected)**2/(expected)).sum()
  
  print(f"Chi-Squared: {chi_squared}")
  return contingency_table

def null(df):
  print(df.isnull().sum())
  
 
# 1. does the code follow PEP8? Yes, code seems to follow guidelines.
# 2. are comments adequate, does every function or class have a docstring? Although there are no comments or docstrings, code is organized and neat enough for reader to be able to follow along.
# 3. are variable names sensible and do they help the reader figure out what's going on? Variable names are well labeled so the reader can make sense of it all.
# 4. would you use this module? I would certainly use this module.
