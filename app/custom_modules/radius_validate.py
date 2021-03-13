def user_radius():
    
    radius =''
    within_range = False
    acceptable_values = ['1','2','5']
    
    while radius.isdigit() == False or within_range == False:
        
        radius = input("Please pick radius of 1,2 or 5: ")
        
        #Digit Check
        if radius.isdigit() == False:
            print("Input Failed: Please enter digit")
        
        #Range check   
        if radius.isdigit() == True:
            if radius in acceptable_values:
                within_range = True
                print ('Input Successful')
            else:
                within_range = False
                print("Input Failed: Please enter a radius of 1,2 or 5")
        
    
    return int(radius)