import json

def writeJSON(tempDict, flagPath):
    """
    write data back to json file
    """
    with open(flagPath, 'w') as outfile:
        json.dump(tempDict, outfile)


def flagTrue(tempDict, flagPath):
    """
    Changes status of explored flag to true
    """
    tempDict["explored"] = "true"
    writeJSON(tempDict, flagPath)


def flagFalse(tempDict, flagPath):
    """
    Changes status of explored flag to false
    """
    tempDict["explored"] = "false"
    writeJSON(tempDict, flagPath)


def updateFlag(flag, flagPath):
    """
    Main function to call.
    
    flag:  should be boolean, true/false. Should be lowercase of 
        what you want it to be changed to.
    
    flagPath:  is the path to the flag that you want to change.
    """

    # load json data and save to data to a local dictionary
    # Opening JSON file
    with open(flagPath, 'r') as openfile:

        # Reading from json file
        json_object = json.load(openfile)

    # copy json data to tempDict so that we can append the lists
    tempDict = {}  
    tempDict.update(json_object)

    if flag == "true":
        flagTrue(tempDict, flagPath)

    elif flag == "false":
        flagFalse(tempDict, flagPath)
        

# #testing
# flag = "False"
# flagPath = "room1.json"

# updateItems(flag, flagPath)