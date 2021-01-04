import pandas as pd
df = pd.read_csv('/home/emily/Bootcamp/vehicles_insight/data/vehicles.csv')
print(f'Data frame shape is: {df.shape}')

print(f'Data frame lenght is: {len(df.index)}')

print(f'Columns are: {df.columns.to_list()}')

print(f'The amount of null values per column is: {df.isnull().sum()}')

print(f'The minimun values in numerical columns are: {df[['Engine Displacement', 'Cylinders', 'Fuel Barrels/Year', 'City MPG', 'Combined MPG', 'CO2 Emission Grams/Mile', 'Fuel Cost/Year']].min()}')

print(f'The minimun values in numerical columns are: {df[['Engine Displacement', 'Cylinders', 'Fuel Barrels/Year', 'City MPG', 'Combined MPG', 'CO2 Emission Grams/Mile', 'Fuel Cost/Year']].max()}')

