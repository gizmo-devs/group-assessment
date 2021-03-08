import json
from datetime import datetime

def sorter(data, sort_option):
  # sort data depending on option chosen
  if sort_option == 'date':
    sorted_date = sorted(data, key=lambda x: datetime.strptime(x['Month'], '%Y-%m'))
    return sorted_date
  if sort_option == 'distance':
    sorted_distance = sorted(data, key=lambda x: x['Distance'], reverse=False)
    return sorted_distance
  if sort_option == 'category':
    sorted_category = sorted(data, key=lambda x: x['Crime type'], reverse=False)
    return sorted_category

if __name__ == '__main__':
  # Using the file_handler for loading the json
  import file_handler as fh

  data = fh.load_files_in_directory("crime_files")

  print("Original Data")
  print(json.dumps(data[:3]))

  print("Sorted Data by Date")
  print(json.dumps(sorter(data, 'date')[:3]))

  print("Sorted Data by Crime Category")
  print(json.dumps(sorter(data, 'category')[:3]))

  # commented out for now as 'Distance' key does not yet exist.
  # print("Sorted Data by Distance")
  # print(json.dumps(sorter(data, 'distance')[:3]))