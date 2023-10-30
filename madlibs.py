from screens import *
from Getters import *
from story1 import *


def Madlibs (debug = False):
    if debug: print("Welcome to debug")
    
    print(TitleScreen(debug)) 
    input("Press enter to continue.")
    
    done = False
    
    while not done:
        print(MainMenu(debug))
        choice = getMenuOption(debug)
        
        if choice == "q":
            exit();
            
        elif choice == "1":
            print(Story1(debug))
            input("Press enter to continue.")


Madlibs(True)
