import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

HELPER=f"""
Welcome to Check Crimes application.

This application filters and sorts the .csv files in {os.path.join(APP_ROOT, 'data_files')} directory.

The filtering and sorting criteria is inputted from the user.

If you want to exit the application at ay time type 'quit' exit.
or should you want to start again, type 'restart'.
"""
