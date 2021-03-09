import sys

OPTS = {
    "1": "distance",
    "2": "date",
    "3": "category"
}

def sort_option():
    expected = set(['distance', '1',  'date', '2', 'category', '3'])
    while True:
        criteria = input("Please enter a option: \n[1] distance \n[2] date \n[3] category \n\n")
        if criteria in expected :
          print("it is in expected")
          return OPTS[criteria]
        else:
          print ('\n\nPlease choose/enter one of the following: \n\n*For distance* 1 \n*For date*  2 \n*For category* 3 \n\n')


def ask_to_sort():
    yes = ['yes', 'y']
    no = ['no', 'n']

    while True:
      userInput_ask = input("\n\nDo you want to Sort by Distance, Date or Category? \nPlease Enter 'Y' or 'N'\n\n").lower()
      if userInput_ask in yes:
        return True
      elif userInput_ask in no:
          return False
        # sys.exit("Program Terminated \n")
      else:
        print(userInput_ask + " was not recognised." + "\nPlease type only " + ",".join(yes) + ",".join(no))


if __name__ == '__main__':
    if ask_to_sort():
        print("sorted Value ", sort_option())
