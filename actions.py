from getInfo import *
from updateItems import *
from exploredFlag import *
from roomFunctions import *
from parserVocabulary import *
from currentRoom import *
from game import *

# Normal object name to object filename dictionary for 'take', 'drop' and 'lookat' commands
normalNameToFilenameDictionary = {"bluepill":"bluePill", "dilithiumcrystals":"dilithiumCrystals",
                                  "dogecoin":"dogeCoin", "id":"ID", "launchcodes":"launchCodes",
                                  "key":"teslaKey", "mixtape":"mixtape", "redpill":"redPill",
                                  "rocketfuel":"rocketFuel", "navigationmap":"solarSystemNavMap",
                                  "spacesuit":"spaceSuit", "teslakey":"teslaKey", "hat":"dogeHat",
                                  "crystals":"dilithiumCrystals"}

# Object filename to normal object name dictionary for 'take', 'drop' and 'lookat' commands
filenameToNormalNameDictionary = {"bluePill":"blue pill", "dilithiumCrystals":"dilithium crystals",
                                  "dogeCoin":"Dogecoin", "ID":"ID", "launchCodes":"launch codes",
                                  "mixtape":"mixtape", "redPill":"red pill", "rocketFuel":"rocket fuel",
                                  "solarSystemNavMap":"navigation map",
                                  "spaceSuit":"spacesuit", "teslaKey":"Tesla key", "dogeHat":"Doge hat",}

# Normal feature name to feature filename dictionary for 'lookat' command
featureNameToFilenameDictionary = {"keyholder":"keyHolder", "oompa":"oompa", "oompaloompa":"oompa",
                                   "gps":"gps", "ludicrousmode":"ludicrisMode", "grimes":"grimes",
                                   "safe":"safe", "scientist":"labScientist", "spacesuitrack":"suitRack",
                                   "engineer":"labEngineer", "statue":"dogeStatue", "littlegreenman":"littleGreenMan",
                                   "faceentrance":"faceEntrance", "martian":"martian", 
                                   "navigationterminal":"navigationTerminal", "restricteddoor":"restrictedDoor",
                                   "transporter":"transporter", "guard":"spaceForceGuard", "fueldepot":"fuelDepot",
                                   "fueltank":"fuelTank", "shuttledoor":"shuttleDoor", "barf":"talktoBarf", 
                                   "maincomputer":"shuttleMainComputer", "moonbaseairlock":"shuttleAirlock",
                                   "lunarlander":"lunarLander", "battery":"moonRoverBattery", "moonmap":"moonMap",
                                   "marsbaseairlock":"marsAirlock", "marsbaseheadquarters":"marsBaseHeadquarters",
                                   "marsludicrousmode":"marsLudicris", "marsgps":"marsGps",
                                   "pyramidentrance":"pyramidEntrance", "altar":"altar"}


# Help
def help():
    print("I understand these verbs:")
    print("connect, drop, eat, enter, go, help, insert, inventory, load, loadgame,")
    print("look, look at, open, put, quit, savegame, start, take, talk, use, wear")

# Look
def look(roompath):
    print(getInfo(roompath, "longMessage"))
    droppedObjects = getInfo(roompath, "droppedObjects")
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

# Show inventory
def showInventory(path):
        inventory = getInfo(path + r"\elon\inventory.json", "objects")
        if len(inventory) == 0:
            print("You don't have anything.")
        else:
            print("You have:")
            stuff = ""
            count = 0
            for item in inventory:
                name = filenameToNormalNameDictionary.get(item)
                count += 1
                stuff = stuff + name
                if count < (len(inventory)):
                    stuff = stuff + ", "
                if count == (len(inventory)):
                    stuff = stuff
            print(stuff)

# Take
def take(choice, path, roomPath):
    if choice == "take":
        print('Take what?')
    else:
        target = choice.replace("take","")
        if target in parserVocabulary.objects:

            # Convert parsed object name to it's object filename using dictionary
            object = normalNameToFilenameDictionary.get(target)

            # Create inventory path and object lists
            inventoryPath = (path + r"\elon\inventory.json")
            objectsList = getInfo(roomPath, "objects")
            droppedObjectsList = getInfo(roomPath, "droppedObjects")
         
            # If object is in room "objects" list
            if object in objectsList:
                # Run updateItems function to add object to inventory
                updateItems("add", object, "initial", inventoryPath)
                # Run updateItems function to remove object from room "objects"
                updateItems("remove", object, "initial", roomPath)
                # Tell user object has been added to inventory
                takenObject = filenameToNormalNameDictionary.get(object)
                print("You take the " + takenObject + ".")

            # Else If object is in room "droppedObjects" list
            elif object in droppedObjectsList:
                # Run updateItems function to add object to inventory
                updateItems("add", object, "initial", inventoryPath)
                # Run updateItems function to remove object from room "droppedObjects"
                updateItems("remove", object, "dropped", roomPath)
                # Tell user object has been added to inventory
                takenDroppedObject = filenameToNormalNameDictionary.get(object)
                print("You take the " + takenDroppedObject + ".")

            # Else
            else:
                # Tell User that object isn't here
                print("That isn't here, you can't take it.")

        else:
            print("I don't understand your command, can you rephrase it?")

# Drop
def drop(choice, path, roomPath):
    # If a thing to drop is not specified
    if choice == "drop":
        print("Drop what?")
    else:
        target = choice.replace("drop","")
        # If the the object is a valid object
        if target in parserVocabulary.objects:

            # Convert parsed object name to it's object filename using dictionary
            object = normalNameToFilenameDictionary.get(target)

            # Create inventory path and object lists
            inventoryPath = (path + r"\elon\inventory.json")
            inventoryList = getInfo(inventoryPath, "objects")

            # If object in Inventory
            if object in inventoryList:
                # Run updateItems function to remove object from inventory
                updateItems("remove", object, "initial", inventoryPath)
                # Run updateItems function to add object to room "droppedObjects"
                updateItems("add", object, "dropped", roomPath)
                # Tell user object has been dropped
                droppedObject = filenameToNormalNameDictionary.get(object)
                print("You drop the " + droppedObject + ".")
            else:
                print("You don't have that to drop.")

        else:
            print("I don't understand your command, can you rephrase it?")

# Look at
def lookat(choice, path):
    # If a thing to look at is not specified
    if choice == 'lookat':
        print("Look at what?")
    else:
        # Remove 'lookat' from string so only object or feature name remains
        thing = choice.replace("lookat","")

        # If thing is an object
        if thing in parserVocabulary.objects:
            # Convert parsed object name to it's object filename using dictionary
            object = normalNameToFilenameDictionary.get(thing)
            # Create string of path to object JSON in objects folder
            objectPath = "\\" + "objects" + "\\" + object + ".json"
            # Create current game full path to object JSON 
            fullPath = path + objectPath
            # Display object description
            print(getInfo(fullPath, "description"))
        
            # If thing is a feature
        elif thing in parserVocabulary.features:
            # Convert parsed feature name to it's feature filename using dictionary
            feature = featureNameToFilenameDictionary.get(thing)
            # Create string of path to feature JSON in features folder
            featurePath = "\\" + "features" + "\\" + feature + ".json"
            # Create current game full path to feature JSON 
            fullPath = path + featurePath
            # Display feature description
            print(getInfo(fullPath, "description"))
        
            # If thing is not a valid thing
        else:
            print("I don't understand your command, can you rephrase it?")

       