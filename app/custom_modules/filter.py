"""
Filtering the dictionary by radius.
"""
import math
from .assigned_modules import geodist as gd


def Filter(crime_data, postcode_latlng, radius):
    for i in crime_data:
        lng = crime_data[i][key = 'Longitude']
        lat = crime_data[i][key = 'Latitude']
        
        filtered_data = ()    
        if gd.distance(postcode_latlng,(lat,lng))<=radius:
            filtered_data.append(crime_data[i])
    
    return filtered_data
 