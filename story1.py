from Getters import *

def Story1 (debug = False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendName1 = getWord("Enter a name:", debug)
    sport1 = getSport("Enter a sport that you can play:", debug)
    Food1 = getWord("Enter your favorite food: ")
    Topic1 = getWord("Enter an interest of yours: ")
    sport2 = getSport2("Enter another sport: ")
    out = "\n"
    out += "One day me and my friend " + friendName1
    out += " were out playing " + sport1
    out += ". After a few minutes we got hungry and my mom made us " + Food1
    out += ". The food was super good and me and my friend had fun talking about " + Topic1
    out += " and " + sport2
    out +=
    return out
