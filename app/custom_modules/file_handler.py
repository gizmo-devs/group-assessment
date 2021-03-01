"""
This file holds file operations for CRUD
Create, Read, Update, Delete
"""
from os import path, listdir
from app import APP_ROOT
import csv, json

DATA_FILES_LOC = path.join(APP_ROOT, "data_files")


def file_exists(filepath, dir=False):
    """
    A simple function to check if a file or folder exists
    :param filepath:    filepath to check
    :type filepath:     string
    :param dir:         is it a directory
    :type dir:          boolean
    :return:            True or False
    :rtype:             Boolean
    """
    if dir:
        if path.exists(filepath):
            return True
        else:
            return False
    else:
        if path.isfile(filepath):
            return True
        else:
            return False


def read_csv_file(filepath):
    """
    read csv file 'filename' and create a dict with the results.
    :param filepath:    csv filename and loaction
    :type filepath:     string
    :return:            contents of CSV
    :rtype:             list of dicts
    """
    data=[]
    with open(filepath, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def write_file(data, fname="output.json"):
    """
    Output data (dict) to filename.
    Creates file in the custom_modules directory.
    :param data:    json to write to a file
    :type data:     dict
    :param fname:   file name defaulting to 'output.json'
    :type fname:    string
    :return:        N/A
    :rtype:         N/A
    """
    with open(fname, 'w') as f:
        f.write(json.dumps(data))
    return


def load_files_in_directory(directory):
    """
    Loop through each of the csv files in 'directory'
    :param directory:   directory to loop through to load files.
    :type directory:    string
    :return:            all of the csvs in directory
    :rtype:             dict
    """
    # for file in directory
    loaded_data = []
    for f in listdir(path.join(DATA_FILES_LOC, directory)):
        if f.endswith(".csv"):
            loaded_data.extend(load_file(path.join(DATA_FILES_LOC, "crime_files", f)))
        else:
            continue
    return loaded_data


def load_file(fpath):
    """
    loads fpath.
    :param fpath: file path (inc filename and ext)
    :type fpath: string
    :return: returns the contents of the csv
    :rtype: dict
    """
    if file_exists(fpath):
        return read_csv_file(fpath)
    else:
        print(f"Cound not read file {fpath}")


if __name__ == '__main__':
    print(file_exists(DATA_FILES_LOC, dir=True))
    print(load_files_in_directory("crime_files"))
    write_file(load_file(path.join(DATA_FILES_LOC, "postcodes", "postcodes.csv")), 'postcodes.json')