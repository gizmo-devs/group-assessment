"""
This is the where the main logic for the application is contained.
"""
from os import path
from .custom_modules import file_handler as fh
from .custom_modules import filter as fltr

def init():
    # Example of how to collect the data from the files
    print("Loading in crime files...")
    crime_data = fh.load_files_in_directory("crime_files")
    print("Loading postcodes...")
    postcode_data = fh.load_file(path.join("postcodes", "postcodes.csv"))

    # How to use/display the data.
    print("Showing 1st element of crime data:")
    print(crime_data[0])
    print("Showing 1st element of Postcode Data:")
    print(postcode_data[0])
    
    filtered_crime_data = fltr.Filter(crime_data, (50.827973, -4.544117), 5)
    print(filtered_crime_data)