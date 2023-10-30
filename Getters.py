def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        option = input("Please select an option ")
        option = option.lower()
        
        if (option == "q" or 
            option == "quit" or 
            option == "x" or 
            option == "exit"):
                option = "q"
                goodInput = True
                
        elif (option == "1" or 
            option == "story1" or 
            option == "one" or 
            option == "story 1"):
                option = "1"
                goodInput = True
            
        else:
            print( "Please make a valid choice")
            
    return option
    
    
def getWord(prompt, debug = False):
    if debug: print("getMenuOption Function")

    goodInput = False

    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't cuss")
       
            
    return word

def isSwear(word, debug = False):
    if debug: print("in isSwear Function", word)
    if word in swearList:
        return True
    else:
        return False
    
    
swearList = ["fuck",
            "shit",
            "ass",
            "damn",
            "bitch",
            "cock",
            "dick",
            "pussy",
            "cunt",
            "fag",
            ]
