"""
This is the where the main logic for the application is contained.
"""
from os import path, execl
import sys
import app
from .custom_modules import file_handler as fh
from .custom_modules import input_validation as iv
from .custom_modules import user_interaction as ui
from .custom_modules import data_manipulation as dm


def check_app_commands(cmd):
    """
    Check to see if the command given is for a help, restart or quit.
    :param cmd: help, restart or quit
    :type cmd: string
    """
    if cmd == ('restart'):
        restart()
    if cmd == ('quit'):
        quit()
    if cmd == ('help'):
        print(app.HELPER)
    return


def restart():
    """
    Command to restart the program
    """
    print("Restarting")
    print("")
    return execl(sys.executable, sys.executable, *sys.argv)


def quit():
    """
    Command to quit the program
    """
    print('Exiting')
    sys.exit(0)


def init():
    # Set initial variables
    pcode_coord = None
    sort_by = ""

    # Example of how to collect the data from the files
    print("Loading in crime files...")
    crime_data = fh.load_files_in_directory("crime_files")
    print("Loading postcodes...")
    postcode_data = fh.load_file(path.join("postcodes", "postcodes.csv"))

    # Validate postcode
    pcode = iv.user_pcode()

    # Get 1st element that matches.
    for record in postcode_data:
        if record['Postcode'].replace(" ", "").strip() == pcode.upper():
            pcode_coord = (float(record['ETRS89GD-Lat']), float(record['ETRS89GD-Long']))
            break

    # Unable to obtain postcode.
    if not pcode_coord:
        print(f"Cannot obtain coordinates for {pcode}.")
        restart()

    # Validate Radius
    r = iv.user_radius()

    print(f"looking for crimes within a radius of {r}km from {pcode.upper()}")

    # Get crime using the filter
    crime_data = dm.Filter(crime_data, pcode_coord, r)

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
