import json

def writeJSON(tempDict, path):
    # Write data back to json file
    with open(path, 'w') as outfile:
        json.dump(tempDict, outfile)


def addItem(item, category, tempDict, path):
    # Add item to 'droppedObjects'
    if category == "dropped":
        tempDict["droppedObjects"].append(item)
        writeJSON(tempDict, path)
    # Add item to 'objects'
    else:
        tempDict["objects"].append(item)
        writeJSON(tempDict, path)

 
def removeItem(item, category, tempDict, path):
    # Remove item from 'droppedObjects'
    if category == "dropped":
        tempDict["droppedObjects"].remove(item)
        writeJSON(tempDict, path)
    # Remove item from 'objects'
    else:
        tempDict["objects"].remove(item)
        writeJSON(tempDict, path)
 

def updateItems(command, item, category, itemPath):
    """
    This is the main function to call to add or remove objects from room and inventory JSON files
    
    command is a string passed in from user, either 'add' or 'remove'
    
    item is the item that needs to be removed from inventory or rooms

    category is a string that specifies if item is initial object in room or an object
    that Elon dropped there, so the function know whether to look in 'objects' or 'droppedObjects'
    
    itemPath represents the path to the JSON that needs to be updated. - e.g. 'example.json'
    """

    # load json data and save to data to a local dictionary
    # Opening JSON file
    
    path = itemPath
    type = category
    
    with open(path, 'r') as openfile:

        # Reading from json file
        json_object = json.load(openfile)

    # copy json data to tempDict so that we can append the lists
    tempDict = {}  
    tempDict.update(json_object)

    if command == "remove":
        removeItem(item, type, tempDict, path)
    
    elif command == "add":
        addItem(item, type, tempDict, path)
        
        
          
# #testing
# itemPath = r"saved_games\tempUserData\elon\inventory.json"
# command = "add"
# item = "dogeCoin"

# updateItems(command, item, itemPath)
