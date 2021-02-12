#################################
#
# Lotto number generator for 
# the norwegian lottery system
#
# Created by: Jan Brekke
# Website: https://www.digitalbrekke.com
#
#################################

import time
import random
from os import system, name

def clear(): 
  
    # Windows terminal
    if name == 'nt': 
        _ = system('cls') 
  
    # Linux terminal
    else: 
        _ = system('clear') 

clear()

while True :
    print("\n\n")
    print("*"*56)
    print("\n")
    print("           --DigitalBrekke--")
    print("         Lotto Number Generator\n")
    print("Choose an which lottery system you need numbers for\n")
    print("       1 :: Lotto")
    print("       2 :: Viking Lotto")
    print("       3 :: EuroJackpot\n")
    print("*"*56)
    print("       9 :: Exit\n")
    print("*"*56)


    # The command that actually ask for a number
    action = input('Option:  ')

    def lottogen():
        clear()
        print("\n\t** Lets generate some winning numbers! **\n")
        
        def lotto():
            import random
            integer = []
            

            for number in range(0,8):
                if number not in integer:
                    integer.append(random.randint(1,34))
            return integer
        
        numInput = int(input("How many number lines do you need? "))
        clear()
        print("*** Here are your winning numbers! ***\n\n")
        for i in range(0, numInput):
            print ("\t", *lotto())
        input("\n\n\nPress ENTER to get back to the menu")
        clear()
    clear()

    def vikinglottogen():
        #print("vikinglotto")

        clear()
        print("\n\t** Lets generate some winning numbers! **\n")
        
        def vikinglotto():
            import random
            integer = []
            
            for number in range(0,6):
                integer.append(random.randint(1,48))
            return integer

        def vikinglottotillegg():
            import random
            tilleggnr = []

            for number2 in range(0,1):
                tilleggnr.append(random.randint(1,8))
            return tilleggnr
        
        numInput = int(input("How many number lines do you need? "))
        clear()
        print("*** Here are your winning numbers! ***\n\n")
        for i in range(0, numInput):
            print ("\t", *vikinglotto(), "\tViking Number: ", *vikinglottotillegg())
        input("\n\n\nPress ENTER to get back to the menu")
        clear()
    clear()

    def eurojackpotgen():
        #print("EuroJackpot")

        clear()
        print("\n\t** Lets generate some winning numbers! **\n")
        
        def eurojackpot():
            import random
            integer = []
            

            for number in range(0,5):
                integer.append(random.randint(1,50))
            return integer
        
        def eurojackpottillegg():
            import random
            tilleggnr = []

            for number2 in range(0,2):
                tilleggnr.append(random.randint(1,10))
            return tilleggnr
        
        numInput = int(input("How many number lines do you need? "))
        clear()
        print("*** Here are your winning numbers! ***\n\n")
        for i in range(0, numInput):
            print ("\t", *eurojackpot(), "     ", "\tStar Number: ", *eurojackpottillegg())
        input("\n\n\nPress ENTER to get back to the menu")
        clear()
    clear()

    choice = {'1': lottogen, '2': vikinglottogen, '3': eurojackpotgen }

    # The exit command since the script is  running in a while loop
    # Yes! I know pressing any other key would also kill it :P
    # but it's nice to have it in there
    if action == '9':
        print("\n\nSee you around!")
        break

    choice[action]()
