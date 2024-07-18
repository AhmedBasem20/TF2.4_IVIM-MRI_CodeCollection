import pandas as pd

df = pd.read_csv('test_output.csv')

# Filter out the columns that start with 'bval'
df_filtered = df.loc[:, ~df.columns.str.startswith('bval')]
#compress and save the file.
df_filtered.to_csv('test_output.csv.gz', compression='gzip')
