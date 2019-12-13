import pandas as pd
df  = pd.read_csv('features_data_with_normalization.csv')
df_2 = pd.read_csv('equity_value_data.csv')
platform = df['platform']
time = df_2


