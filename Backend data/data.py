import pandas as pd
from gettinglatlong import getlocation


population = getlocation()
cases = pd.read_csv("/Users/neel/Desktop/hackcovid/backend/Datasets/Facilities_in_Mumbai_COVID_19_Cases.csv",index_col ="Ward")
    # Deleting unecessary rows
print(population.columns[4:7])
for column in population[population.columns[0:4]]:
    population.drop(column, axis=1, inplace=True)
print(population)
for column in population[population.columns[4:]]:
    population.drop(column, axis=1, inplace=True)
print(population)
    # deleting null values
cases.fillna(0, inplace=True)

print(cases)
    # Merging both dataframes
cases = pd.merge(cases, population,left_on='Ward', right_on='Ward')

totalno_of_rows = cases.shape[0]
cases.insert(5, "Zone", 0, True)
print(cases)
for row in range(0, totalno_of_rows):
    percentage = (cases.iloc[row, 3]*1.5+cases.iloc[row, 2]
                      * 2.6+cases.iloc[row, 1]*3.6)/cases.iloc[row, 4]
    if percentage >= 0.0002:
        cases.iloc[row, 5] = 5 #RED
    elif percentage >= 0.0001 and percentage <= 0.0002:
        cases.iloc[row, 5] = 4 #Orange
    elif percentage < 0.0001 and percentage > 0:
        cases.iloc[row, 5] = 2 #BLUE
    else:
        cases.iloc[row, 5] = 0 #GREEN

print(cases['Zone'])
file_line = '/Users/neel/Desktop/hackcovid/backend/Datasets/BMC_Wards.geojson'
file_poly = 'heat.geojson'
print(cases.loc['A'])
import json
with open(file_line, 'r') as f:
    data = json.load(f)


for feature in data['features']:
    if feature['properties']['name'] == cases.loc[feature['properties']['name']].name:
        feature['properties']['zone'] = int(cases.loc[feature['properties']['name']]['Zone'])
        feature['geometry']['type'] = 'Point'
        feature['geometry']['coordinates'] = [cases.loc[feature['properties']['name']]['Latitude'],cases.loc[feature['properties']['name']]['Longitude']]       
        
print(data)
with open(file_poly, 'w+') as f:
    json.dump(data, f, indent=2)




