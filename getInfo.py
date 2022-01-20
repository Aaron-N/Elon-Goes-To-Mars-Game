import json

# use this file to get info for each room/feature/inventory/item

def getInfo(path, topic):
    """
    path is path to json file to get info from
    
    topic is what to get data on. e.g. - "name", "displayName", "objects", etc.
    """

    # load json data and save to data to a local dictionary
    # Opening JSON file
    with open(path, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        return(json_object[topic])

    


# testing
# path = r"saved_games\tempUserData\rooms\r1_wilderHouse.json"
# topic = "objects"

# getInfo(path, topic)
