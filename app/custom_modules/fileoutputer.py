# Version 1
# Date Creation 9/3/2021
# File output-er function for crime data
# This takes values from the dictionary and outputs data into a csv
import csv

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











