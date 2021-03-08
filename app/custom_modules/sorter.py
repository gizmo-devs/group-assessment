import json
from datetime import datetime

# load dummy data into a variable
with open('/Users/bradley/Documents/GitHub/group-assessment/app/data_files/crime_files/Schema_criminal_files.json') as f:
  data = json.load(f)

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

sorter(data, 'date')

sorter(data, 'distance')

sorter(data, 'category')