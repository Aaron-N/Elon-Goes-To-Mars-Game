import os
from game import *
from getInfo import *

def loadGameSave(path):
    print("\u001b[32mYou chose to load a game!\n\u001b[0m")
    print("-- Below is a list of your available saves --")
    saves = os.listdir(path)
    
    # display all available saves. Excludes, "tempUserData"
    # if tempUserData exists, delete. Else, skip.
    if "tempUserData" in saves:
        saves.remove("tempUserData")
    
    for i in saves:
        print(i)
    
    choice = str(input("\u001b[32m\nWhich do you want to load? "))
    print("\u001b[37m")

    if choice in saves:
        # need to make this set the new save path to pass back to game.py
        print("You chose to load save", choice)
        print("Save loaded, welcome back!\n")
        print("\u001b[32mWe now return you to your regularly scheduled text-based adventure game, already in progress...\n\u001b[0m")


        newDirectoryPath = str(os.path.join(path, choice))  # saves the path to the game to be loaded.
        
        return newDirectoryPath  # used for passing into the load game call


def getCurrentRoom(newDirectoryPath):
    """
    gets and returns current room info for selected save
    """
    # need get current room info
    elonJSON = r"\elon\elon.json"
    currentRoomPath = str(newDirectoryPath + elonJSON)
    
    # get current room info\
    currentRoom = getInfo(currentRoomPath, "currentRoom")
    
    return currentRoom
