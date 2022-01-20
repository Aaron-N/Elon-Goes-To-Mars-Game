import os
from getInfo import *
from updateItems import *
from exploredFlag import *

# Object filename to normal object name dictionary for 'take', 'drop' and 'lookat' commands
filenameToNormalNameDictionary = {"bluePill":"blue pill", "dilithiumCrystals":"dilithium crystals",
                                  "dogeCoin":"Dogecoin", "ID":"ID", "launchCodes":"launch codes",
                                  "mixtape":"mixtape", "redPill":"red pill", "rocketFuel":"rocket fuel",
                                  "solarSystemNavMap":"Solar System navigation map",
                                  "spaceSuit":"spacesuit", "teslaKey":"Tesla key", "dogeHat":"Dogedog hat"}

def infoUpdater(path, fullPath, roomPath, objectPath):
    """
    Just eliminated repetitive code.
    Responsible for updating flags, objects, rooms, and inventory.
    """
    objectList = getInfo(fullPath, "objects")  # check if the feature has any objects in it.
    
    if len(objectList) >= 1:  # if there are objects in the feature
        print("The objects that this", getInfo(fullPath, "displayName"), "has are:")
        for object in objectList:
            print(object)

        print("What do you want to do?")
        choice = str(input())  

        if choice in objectList:
            # displays objects description
            objectPath = str(os.path.join(objectPath, choice))
            objectPath = (path + objectPath + ".json")
            objectInfo = getInfo(objectPath, "description")
            print(objectInfo)
        
            print("You take the", choice, "and put it in your inventory.")
            
            # add object to inventory
            # call update items and add object to inventory
            inventoryPath = (path + r"\elon\inventory.json")
            command = "add"
            item = choice
            updateItems(command, item, inventoryPath)               
            
            # remove object from feature
            # call update items and remove object from feature.json at "fullPath"
            command = "remove"
            item = choice
            updateItems(command, item, fullPath)                
            
            # remove object from room
            # call update items and remove dogecoin from r1_wilderHouse objects
            roomPath = (path + roomPath)
            command = "remove"
            item = choice
            updateItems(command, item, roomPath)
            
        else:
            print("You decide not to take anything.")

    if len(objectList) <= 0:  # if there are no more objects in the feature
        print("The", getInfo(fullPath, "displayName"), "has nothing more for you.")


# features
def features(path, featurePath, roomPath, objectPath):
    """
    "path" is save directory path. e.g. r"saved_games\tempUserData"
    "featurePath" path to feture in correct save slot
    "roomPath" is path to room file being accessed within save. e.g. r"\rooms\r1_wilderHouse.json"
    "objectPath" is path to object that is being interacted with
    """
    fullPath = path + featurePath
    
    explored = getInfo(fullPath, "explored")
    
    if explored == "false": # feature not visited before
        print("You approach the", getInfo(fullPath, "displayName"))  # print the features displayName
        print(getInfo(fullPath, "description"))  # print the features description
        updateFlag("true", fullPath)  # change explored flag to true

        infoUpdater(path, fullPath, roomPath, objectPath)


    if explored == "true":  # feature visited before
        print("You approach the", getInfo(fullPath, "displayName"))  # print the features displayName
        print(getInfo(fullPath, "shortDescription"))  # print the features short description

        infoUpdater(path, fullPath, roomPath, objectPath)
    

# rooms
def rooms(path, roomPath):
    """
    Only call this function for updating json files in "\rooms"
    
    "path" is save directory path. e.g. r"saved_games\tempUserData"
    "roomPath" is path to room file being accessed within save. e.g. r"\rooms\r1_wilderHouse.json"
    """
    fullPath = path + roomPath
    
    # display room name
    displayName = getInfo(fullPath, "displayName")
    print("You arrive at", displayName + ".")
    
    # checks if the room has been visited or not.
    explored = getInfo(fullPath, "explored")  # retrieves current state of explored
    
    if explored == "false":
        # update flag and print long message since first time entering room.
        updateFlag("true", fullPath)
        
        longMessage = getInfo(fullPath, "longMessage")
        print(longMessage)
    
    elif explored == "true":
        # print short message since revisiting room.
        shortMessage = getInfo(fullPath, "shortMessage")
        print(shortMessage)
        # If objects in droppedObjects, display them
        droppedObjects = getInfo(fullPath, "droppedObjects")
        if len(droppedObjects) > 0:
            stuff = ""
            count = 0
            for item in droppedObjects:
                name = filenameToNormalNameDictionary.get(item)
                count += 1
                stuff = stuff + name
                if count < (len(droppedObjects)):
                    stuff = stuff + ", "
                if count == (len(droppedObjects)):
                    stuff = stuff
            print("\nYou also see what you dropped here:")
            print(stuff)