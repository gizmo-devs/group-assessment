import sys

def sort_option():
  userInput_ask = input("\n\nDo you want to Sort by Distance, Date or Category? \nPlease Enter 'Y' or 'N'\n")
  if userInput_ask == 'Y':
    criteria = input("Please enter a option: \n[1] distance \n[2] date \n[3] category")
    return criteria
  else:
    sys.exit("Program Terminated")