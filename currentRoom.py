import json
import os

def updateCurrentRoom(charRoomPath, currentRoom):
    # charRoomPath = elon in whatever the needed directory is.
    # currentRoom = current room
    
    charPath = r"elon.json"
    path = str(os.path.join(charRoomPath, charPath))
    
    with open(path, 'r') as openfile:

        # Reading from json file
        json_object = json.load(openfile)

    # copy json data to tempDict so that we can append the lists
    tempDict = {}  
    tempDict.update(json_object)

    # update the current room in elon.json
    tempDict["currentRoom"] = str(currentRoom)
    
    # write data back to elon.json file
    with open(path, 'w') as outfile:
        json.dump(tempDict, outfile)
    