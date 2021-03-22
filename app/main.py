"""
This is the where the main logic for the application is contained.
"""
from os import path
import sys
import app
from .custom_modules import file_handler as fh
from .custom_modules import input_validation as iv
from .custom_modules import user_interaction as ui
from .custom_modules import data_manipulation as dm


def check_app_commands(cmd):
    if cmd == ('restart'):
        restart()
    if cmd == ('quit'):
        quit()
    if cmd == ('help'):
        print(app.HELPER)
    return


def restart():
    print("Restarting")
    return init()


def quit():
    print('Exiting')
    sys.exit(0)


def init():
    # Example of how to collect the data from the files
    print("Loading in crime files...")
    crime_data = fh.load_files_in_directory("crime_files")
    print("Loading postcodes...")
    postcode_data = fh.load_file(path.join("postcodes", "postcodes.csv"))

    # Validate postcode
    pcode = iv.user_pcode()

    # Get 1st element that matches.
    pcode_coord = [(float(x['ETRS89GD-Lat']), float(x['ETRS89GD-Long'])) for x in postcode_data
                   if x['Postcode'].replace(" ", "").strip() == pcode.upper()][0]

    # Validate Radius
    r = iv.user_radius()

    print(f"looking for crimes within a radius of {r}km from {pcode.upper()}")

    # Get crime using the filter
    crime_data = dm.Filter(crime_data, pcode_coord, r)

    # Set the sort_by as empty parameter.
    sort_by = ""

    # Sort the results
    if ui.ask_to_sort():
        sort_by = ui.sort_option()

    if sort_by in ['date', 'distance', 'category']:
        crime_data = dm.sorter(crime_data, sort_by)

    if len(crime_data) == 0:
        print("No results found. Nothing to export. Ending")
        exit(0)

    # Get user input for export name
    export_name = ui.export_name()

    # export to csv
    fh.file_outputer(export_name, crime_data)
