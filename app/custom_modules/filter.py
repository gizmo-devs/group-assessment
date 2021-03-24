"""
Filtering the dictionary by radius.
"""
from app.assigned_modules import geodist as gd


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

if __name__ == '__main__':
    #using the file handler for loading the crime files
    import file_handler as fh
    
    crime_data = fh.load_files_in_directory("crime_files")
    print("Initial Data length")
    print(len(crime_data))
    
    print("\nFiltered Data Length from point 1")
    filtered_data_1 = Filter((crime_data), (50.71422888, -2.4366918), 5)
    print(len(filtered_data_1))
    assert(len(crime_data)>len(filtered_data_1))
    
    print("\nFiltered Data Length from point 2")
    filtered_data_2 = Filter((crime_data), (50.71799154, -3.52638455), 5)
    print(len(filtered_data_2))
    assert(len(crime_data)>len(filtered_data_2))
    
    print("\nFiltered Data Length from point 3")
    filtered_data_3 = Filter((crime_data), (50.50699801, -4.77120732), 5)
    print(len(filtered_data_3))
    assert(len(crime_data)>len(filtered_data_3))