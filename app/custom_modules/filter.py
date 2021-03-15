"""
Filtering the dictionary by radius.
"""
import math
from ..assigned_modules import geodist as gd


def Filter(crime_data, postcode_latlng, radius):
    
    print(type(crime_data))
    filtered_data = []
    
    for i in crime_data:
        if i['Longitude'] == "" or i['Latitude'] == "":
            continue
        else:
            lng = float(i['Longitude'])
            lat = float(i['Latitude'])
            if gd.distance(postcode_latlng,(lat,lng)) <= radius:
                filtered_data.append(i)

    return filtered_data