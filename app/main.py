"""
This is the where the main logic for the application is contained.
"""
from os import path
from .custom_modules import file_handler as fh


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
