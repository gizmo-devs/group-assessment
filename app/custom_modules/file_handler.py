"""
This file holds file operations for CRUD
Create, Read, Update, Delete
"""
# python / system modules
from os import path, listdir
import csv, json

# custom imports
from app import APP_ROOT

#Add a global for the file_handler module
DATA_FILES_LOC = path.join(APP_ROOT, "data_files")


def path_exists(filepath, dir=False):
    """
    A simple function to check if a file or folder exists
    :param filepath:    filepath to check
    :type filepath:     string
    :param dir:         is it a directory
    :type dir:          boolean
    :return:            True or False
    :rtype:             Boolean
    """
    # Check that the filepath param supplied is a String.
    assert isinstance(filepath, str), f"filepath '{filepath}' needs to be a string"
    if dir:
        if path.exists(filepath):
            return True
    else:
        if path.isfile(filepath):
            return True

    return False


def read_csv_file(filepath):
    """
    read csv file 'filename' and create a dict with the results.
    :param filepath:    csv filename and loaction
    :type filepath:     string
    :return:            contents of CSV
    :rtype:             list of dicts
    """
    # make sure that the path to the file exists.
    assert path_exists(filepath), f"{filepath} was not recognised. Please enter a valid filepath"
    data = []
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
    # check to make sure that target directory is in the data_files folder.
    assert path_exists(path.join(DATA_FILES_LOC,directory), True), f"{directory} Directory needs to exist."
    loaded_data = []
    # for .csv file in directory
    for f in listdir(path.join(DATA_FILES_LOC, directory)):
        if f.endswith(".csv"):
            loaded_data.extend(load_file(path.join(DATA_FILES_LOC, "crime_files", f)))
        else:
            continue
    return loaded_data


def load_file(fpath, in_data_files=True):
    """
    loads fpath.
    :param fpath: file path (inc filename and ext)
    :type fpath: string
    :return: returns the contents of the csv
    :rtype: dict
    """
    if in_data_files:
        file_path = path.join(DATA_FILES_LOC, fpath)
    else:
        file_path = fpath

    assert path_exists(file_path), f"{file_path} could not be found."

    if path_exists(file_path):
        return read_csv_file(file_path)
    else:
        print(f"Could not read file {file_path}")


# Version 1
# Date Creation 9/3/2021
# File output-er function for crime data
# This takes values from the dictionary and outputs data into a csv

def file_outputer(name_of_file,crime_data):
    fields = []
    file_name = name_of_file + ".csv"
    for data in crime_data:
        for d in data:
            fields.append(d)

# dynamically created fields using keys
    field_names = list(dict.fromkeys(fields))

    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(crime_data)

# Example code run file_outputer("testing", crime_data)


if __name__ == '__main__':
    import pprint
    # TESTS:
    # fail_path = path.join(DATA_FILES_LOC, "test")
    # fail_file = path.join(DATA_FILES_LOC, 'crime_files', 'FAIL-2020-01-devon-and-cornwall-street.csv')
    # print(f"Does {DATA_FILES_LOC} exist? :", path_exists(DATA_FILES_LOC, dir=True))
    # print(f"Does {path.join(DATA_FILES_LOC, 'crime_files','2020-01-devon-and-cornwall-street.csv')} exist? :", path_exists(path.join(DATA_FILES_LOC, "crime_files","2020-01-devon-and-cornwall-street.csv"), dir=True))
    # print(f"Does {fail_path} exist? :", path_exists(fail_path, dir=True))
    # print(f"Does {fail_file} exist? :", path_exists(fail_file, dir=True))
    # file_path = "crime_files/FAIL-2020-01-devon-and-cornwall-street.csv"
    # print(f"loading one file '{file_path}'")
    # file_data = load_file(file_path)
    # print("List elements created from one file: ", len(file_data))
    # print("1st element from one file: ")
    #
    # pprint.pprint(file_data[0])
    dir_data = load_files_in_directory('Incorect_crime_files')
    print("Number of elements created from all the .csv files in 'crime_data': ", len(dir_data))


    # Should throw an assert error as 10 is not a string
    # path_exists(10)

    # try loading a file that doesnt exits
    # fail_file = path.join(DATA_FILES_LOC, "fail.xml")
    # assert path_exists(fail_file), f"could not find path: {fail_file}"

    # check to make sure that the result from reading the files is a list
    # assert isinstance(load_files_in_directory("crime_files"), list), \
    #     "Elements returned from load_files_in_directory should be a List."
