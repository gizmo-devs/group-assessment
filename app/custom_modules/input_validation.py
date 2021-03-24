import app


def user_pcode():
    p_code = '_'
    digi_range = False
    digi_count = 0
    
    while len(p_code) not in range(6,9) or digi_range == False :
        
        p = input("Please enter a postcode: ")
        p_code = p.replace(" ","").lower()

        app.main.check_app_commands(p.lower())

        # Length check
        if len(p) not in range(6,9):
            print("Input Unsuccessful: Invalid Post code length.Please try again")
             
        else:
                
            # String Position check
            if p_code[-2:].isalpha() and p_code[0].isalpha():
                
                # Digit Checker
                for char in p:
                    if char.isdigit():
                        digi_count+=1

                if digi_count in range(2,4):
                    digi_range = True
                    # print ('Input Successful')
                else:
                    print("Input Unsuccessful [1]: Postcode must contain 2 or 3 digits. Please try again")
            
            else:
                 print('Input Unsuccessful [2]: Invalid Position of letters')

    return p_code


def user_radius():
    radius = ''
    within_range = False
    acceptable_values = ['1', '2', '5']

    while radius.isdigit() == False or within_range == False:

        radius = input("Please pick radius of 1, 2 or 5: ")
        app.main.check_app_commands(radius.lower())

        # Digit Check
        if radius.isdigit() == False:
            print("Input Failed: Please enter digit")

        # Range check
        if radius.isdigit() == True:
            if radius in acceptable_values:
                within_range = True
                # print('Input Successful')
            else:
                within_range = False
                print("Input Failed: Please enter a radius of 1, 2 or 5")

    return int(radius)
