from Getters import *

def Story1 (debug = False):
    if debug: print("Story1 Function")
    
    friendName1 = getWord("Enter a name:", debug)
    
    
    out = ""
    out += "One day me and my friend " + friendName1
    
    
    return out
