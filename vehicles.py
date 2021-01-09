import pandas as pd
df = pd.read_csv('data/vehicles.csv')
print(f'Data frame shape is: {df.shape}')

print(f'Data frame lenght is: {len(df.index)}')

print(f'Columns names are: {df.columns.to_list()}')

print(f'Columns type are: {df.dtypes}')

print(f'The amount of null values per column is: {df.isnull().sum()}')

print("The minimun values in numerical columns are: " + str(df[['Engine Displacement', 'Cylinders', 'Fuel Barrels/Year', 'City MPG', 'Combined MPG', 'CO2 Emission Grams/Mile', 'Fuel Cost/Year']].min()))

print("The maximun values in numerical columns are: " + str(df[['Engine Displacement', 'Cylinders', 'Fuel Barrels/Year', 'City MPG', 'Combined MPG', 'CO2 Emission Grams/Mile', 'Fuel Cost/Year']].max()))
