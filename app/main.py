"""
This is the where the main logic for the application is contained.
"""
from os import path
from .custom_modules import file_handler as fh
from .custom_modules import postcode_validate as pv
from .custom_modules import radius_validate as rv
from .custom_modules import sort_option as so
from .custom_modules import sorter as custom_sort
from .custom_modules import fileoutputer as output
from .custom_modules import filter as custom_filter


def init():
    # Example of how to collect the data from the files
    print("Loading in crime files...")
    crime_data = fh.load_files_in_directory("crime_files")
    print("Loading postcodes...")
    postcode_data = fh.load_file(path.join("postcodes", "postcodes.csv"))

    # How to use/display the data.
    """
    print("Showing 1st element of crime data:")
    print(crime_data[0])
    print("Showing 1st element of Postcode Data:")
    print(postcode_data[0])
    """

    # Validate postcode
    pcode = pv.user_pcode()

    # Get 1st element that matches.
    pcode_coord = [(float(x['ETRS89GD-Lat']), float(x['ETRS89GD-Long'])) for x in postcode_data \
                   if x['Postcode'].replace(" ", "").strip() == pcode.upper()][0]

    # Uncomment to show Postcode.
    # print(pcode_coord)

    # Validate Radius
    r = rv.user_radius()

    print(f"looking for crimes within a radius of {r}km from {pcode.upper()}")

    # Get crime using the filter
    crime_data = custom_filter.Filter(crime_data, pcode_coord, r)

    # Set the sort_by as empty parameter.
    sort_by = ""

    # Sort the results
    if so.ask_to_sort():
        sort_by = so.sort_option()

    if sort_by in ['date', 'distance', 'category']:
        crime_data = custom_sort.sorter(crime_data, sort_by)

    if len(crime_data) == 0:
        print("No results found. Nothing to export. Ending")
        exit(0)

    # ask for export name
    # export_name = so.export_name()
    export_name = "exmaple_sjdghvsh"

    # export to csv
    output.file_outputer(export_name, crime_data)