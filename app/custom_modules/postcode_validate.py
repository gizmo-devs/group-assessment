def user_pcode():
    p_code = '_'
    digi_range = False
    digi_count = 0
    
    while len(p_code) not in range(6,9) or digi_range == False :
        
        p = input("Please enter your postcode: ")
        p_code = p.replace(" ","").lower()
        
    #Length check     
        if len(p) not in range(6,9):
            print ("Input Unsuccessful: Invalid Post code length.Please try again")
             
        else:
                
            #String Position check
            if p_code[-2:].isalpha() and p_code[0].isalpha():
                
                #Digit Checker
                for char in p:
                    if char.isdigit():
                        digi_count+=1                   
                                
                if digi_count in range(2,4):
                    digi_range = True
                    print ('Input Successful')
                    
                else:
                    print ("Input Unsuccessful [1]: Postcode must contain 2 or 3 digits. Please try again")
            
            else:
                 print('Input Unsuccessful [2]: Invalid Position of letters')
          
                    
           
                          
    return p_code
      