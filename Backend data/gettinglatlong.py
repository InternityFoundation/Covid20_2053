# importing the requests library 
import requests 
import pandas as  pd

def getlocation():
    population=pd.read_csv("/Users/neel/Desktop/hackcovid/backend/Datasets/input_file_v1_dashboard.csv",index_col ="Ward")
    # api-endpoint 
    population.insert(6, "Latitude", 0 , True)
    population.insert(7, "Longitude", 0 , True)
    row=0
    for place in population['Ward location']:
        URL ="https://api.mapbox.com/geocoding/v5/mapbox.places/"+place.split("/")[0]+".json?limit=2&access_token=pk.eyJ1IjoibmVlbHBhcmloYXIiLCJhIjoiY2s5NWZ1bDZjMDY3NTNtcjFpdjZ4bnhmdiJ9.ZzFeFsBaPwQ42F1frkzrmA"
        r= requests.get(URL)
        data = r.json() 
        # extracting latitude, longitude and formatted address  
        # of the first matching location 
        latitude = data['features'][0]['center'][0]
        longitude = data['features'][0]['center'][1]
        population.iloc[row,6]=latitude
        population.iloc[row,7]=longitude
        row=row+1
        #formatted_address = data['formatted_address'] 
        # printing the output 
        
        print("Latitude:%s\nLongitude:%s\n"
            %(latitude, longitude))
    return population
    
# # location given here 
# location = "delhi technological university"
  
# # defining a params dict for the parameters to be sent to the API 
# PARAMS = {'address':location} 
  
# # sending get request and saving the response as response object 
# r = requests.get(url = URL, params = PARAMS) 
  
 
