"""
The main game loop and major functions live here
"""

import json
import os
import sys
import pathlib
import string

from newGame import *

from loadGame import *
from roomFunctions import *
from textParser import*

from getInfo import *
from updateItems import *
from exploredFlag import *

from textParser import *
from currentRoom import *

from actions import *

os.system('cls')

def playGame(): 

    # Main game loop
    print(u"\u001b[31m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@%@%\u001b[0m")
    print(u"\u001b[31m@@@@@@@@@@%@@@@@@@@@@%##******##%@@@@@@@@@@@@@@%@@@@@@@@@%%##**##@@@@@@@@@@@@@@@@@@@@@@%%@@@\u001b[0m")
    print(u"\u001b[31m@@@@@@@@@@@@@@@@@%#*+++======+++++*#%@@@@@@%%@@@@@@@@@@%###%%%%%#*#@@@@@@@@@@@@@@@@@@@%%%@@@\u001b[0m")
    print(u"\u001b[31m@@@@@%%@@@@@@@%**+++++++===++++****++**#@@%@@@@@@@@@@@%%%*++=+*#%@%#%@@@@@@@@@@@@@@@@@@%@@@@\u001b[0m")
    print(u"\u001b[31m@@@@@@@@@%%@%**++++=++====++++++++**+++++#%%@%%%%%@@@@%+:....::---*@#*@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[31m@@@@@@@@@@%***++==========++====+++++*+=+++%%%%%%%%%%%-:. ...::-===*%**@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[31m@@@@@@@@@%***+++=====+++++++++==++++++++++++#%%@@@%%@*--==-:-=+++=+*%*=%@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[31m@@@@@@@@%***+++++==++++++++++++==++++++++++++%@@@@@%@==++++:=*+***++*#+@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[31m@@@@@@%@#**++++++++++++++++**++++++++++***+++#@@@@@@%=::::--+=--===+***@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[31m%@@@@@@%##*+++++*******++++***++++++***++***+*@@@@@@%=-:-:***+=-=+++***%@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[31m@@@@@@@@#****+*******#**********++*+**********%@@@@@@+==-=+++*+++++===*@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[31m@@@@@@@@%##*****##**###***####***********#####%@@@@@@+=-=+*+***+=++=*#@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[31m@@@@@@@@@%##***#########*****#######***#######@@%%@@@#+=-::--===+***@@@@@@@@@@@@@@@@@%@@@@@@\u001b[0m")
    print(u"\u001b[31m%%%%@@@@@%##################***############%#%%@@@@@@@%#########%%#+%%@@@@@@@@@@@@@@@@%@@%@@\u001b[0m")
    print(u"\u001b[31m@@@%%@@@@@%%%###########################%#%%%@@@@@@@%%%#+%@@@@@%*+++%#*%@@@@@@@@@@@%@@@@@%%%\u001b[0m")
    print(u"\u001b[31m@@@@@@%%%@@@%%%%#######################%%%%%@@@@%@@@%@@@=+#@@%#+==+%%#+=*##%@@@@%@%%%%%@@@@%\u001b[0m")
    print(u"\u001b[31m@@@@@%%%%%@@@@@%%%%%%%%%%%%%%%####%%%%%%%%%%@@@@%%%#%@@@++#%##*++*@@*+****+=-==+*%%%%%%%@@@@\u001b[0m")
    print(u"\u001b[31m%%%%%%%%%%%%@@@@@%%%%%%%%%%%%%%%%%%%%%%%@%%%@%%#+==+%@@@%--==--=+@@#+++++=+**++=-::-===*%@%@\u001b[0m")
    print(u"\u001b[31m%%%%%%%%%%%%%%%@@@@@@@@%%%%%%%%%%%%%@@@%%%%#*=-----=+@@@@*:.   =@@*==+**++*+++*+=-------%%%%\u001b[0m")
    print(u"\u001b[31m%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@%%%%#---::----=-+@@@@@@*. -%@%-===-==---=========++=*%%%\u001b[0m")
    print(u"\u001b[31m%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@%%%%%%%%---:::---==-%@%%%@@%%%@@@+=====----=+=====+=++=--%%%\u001b[0m")
    print(u"\u001b[31m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-=-:::::-=-+@@%%%@@@@@@%#-===+----==++==++=+++*+**%%\u001b[0m")
    print(r"___________.____     ________    _______         ________ ________   ___________  _________ ")
    print(r"\_   _____/|    |    \_____  \   \      \       /  _____/ \_____  \  \_   _____/ /   _____/ ") 
    print(r" |    __)_ |    |     /   |   \  /   |   \     /   \  ___  /   |   \  |    __)_  \_____  \  ")
    print(r" |        \|    |___ /    |    \/    |    \    \    \_\  \/    |    \ |        \ /        \ ")
    print(r"/_______  /|_______ \\_______  /\____|__  /     \______  /\_______  //_______  //_______  / ")
    print(r"        \/         \/        \/         \/             \/         \/         \/         \/  ")
    print(r"          ___________________          _____      _____  __________   _________             ")
    print(r"          \__    ___/\_____  \        /     \    /  _  \ \______   \ /   _____/             ") 
    print(r"            |    |    /   |   \      /  \ /  \  /  /_\  \ |       _/ \_____  \              ")
    print(r"            |    |   /    |    \    /    Y    \/    |    \|    |   \ /        \             ")
    print(r"            |____|   \_______  /    \____|__  /\____|__  /|____|_  //_______  /             ")
    print(r"                             \/             \/         \/        \/         \/              ")
    print("\n")

    # Create a text parser instance to get user's choice
    textparser = TextParser()

    # Input variable created, text color set to green and input prompt displayed
    choice = textparser.commandParser("\u001b[32mType in what you'd like to do: New Game, Load Game or Quit >>> ")
    # Text color set back to white
    print("\u001b[37m")
    
    if choice == "newgame":  # new game
        print("\u001b[32mYou chose to start a new game!\u001b[37m\n")
        newGame()

    elif choice == "loadgame":
        # set active path to the save name that the user enters.
        loadGame()
    
    elif choice == "quit":
        # end game
        exitGame()

    else:
        # this covers invalid choices
        print("\n\u001b[32mAlthough creative, that's not an option. Here we go again!\u001b[37m\n")
        playGame()


def newGame():
    createDirectory()  # function from newGame.py
    path = r"saved_games\tempUserData"
    r1_wilderHouse(path)


def loadGame():
    # Loads saved game data
    path = r"saved_games"
    newDirectoryPath = loadGameSave(path)  # path to the chosen save directory.
    currentRoom = getCurrentRoom(newDirectoryPath)

    if currentRoom == "r1_wilderHouse":
        r1_wilderHouse(newDirectoryPath)
    
    elif currentRoom == "r2_teslaRide":
        r2_teslaRide(newDirectoryPath)
    
    elif currentRoom == "r3_grimesHouse":
        r3_grimesHouse(newDirectoryPath)

    elif currentRoom == "r4_rdLab":
        r4_rdLab(newDirectoryPath)
        
    elif currentRoom == "r5_spaceXHQ":
        r5_spaceXHQ(newDirectoryPath)
        
    elif currentRoom == "r6_spaceForceBase":
        r6_spaceForceBase(newDirectoryPath)
        
    elif currentRoom == "r7_launchPad":
        r7_launchPad(newDirectoryPath)
        
    elif currentRoom == "r8_spaceShuttle":
        r8_spaceShuttle(newDirectoryPath)
        
    elif currentRoom == "r9_moonBase":
        r9_moonBase(newDirectoryPath)
        
    elif currentRoom == "r10_moonRover":
        r10_moonRover(newDirectoryPath)
        
    elif currentRoom == "r11_moonPeople":
        r11_moonPeople(newDirectoryPath)
        
    elif currentRoom == "r12_marsBase":
        r12_marsBase(newDirectoryPath)
        
    elif currentRoom == "r13_marsRover":
        r13_marsRover(newDirectoryPath)
        
    elif currentRoom == "r14_marsFace":
        r14_marsFace(newDirectoryPath)
        
    elif currentRoom == "r15_marsPyramid":
        r15_marsPyramid(newDirectoryPath)
            
        
def saveGame(path):
    # Saves current game data
    saveNewGame(path)


def exitGame():
    # put this in a function so it can be called at any point.
    exit("\u001b[32mGoodbye!\u001b[37m\n")  # end game  


def startRoom(newDirectoryPath):
    currentRoom = getCurrentRoom(newDirectoryPath)
    
    if currentRoom == "r1_wilderHouse":
        r1_wilderHouse(newDirectoryPath)
    
    elif currentRoom == "r2_teslaRide":
        r2_teslaRide(newDirectoryPath)
    
    elif currentRoom == "r3_grimesHouse":
        r3_grimesHouse(newDirectoryPath)

    elif currentRoom == "r4_rdLab":
        r4_rdLab(newDirectoryPath)
        
    elif currentRoom == "r5_spaceXHQ":
        r5_spaceXHQ(newDirectoryPath)
        
    elif currentRoom == "r6_spaceForceBase":
        r6_spaceForceBase(newDirectoryPath)
        
    elif currentRoom == "r7_launchPad":
        r7_launchPad(newDirectoryPath)
        
    elif currentRoom == "r8_spaceShuttle":
        r8_spaceShuttle(newDirectoryPath)
        
    elif currentRoom == "r9_moonBase":
        r9_moonBase(newDirectoryPath)
        
    elif currentRoom == "r10_moonRover":
        r10_moonRover(newDirectoryPath)
        
    elif currentRoom == "r11_moonPeople":
        r11_moonPeople(newDirectoryPath)
        
    elif currentRoom == "r12_marsBase":
        r12_marsBase(newDirectoryPath)
        
    elif currentRoom == "r13_marsRover":
        r13_marsRover(newDirectoryPath)
        
    elif currentRoom == "r14_marsFace":
        r14_marsFace(newDirectoryPath)
        
    elif currentRoom == "r15_marsPyramid":
        r15_marsPyramid(newDirectoryPath)



"""----------------------Save New Game----------------------"""
def saveNewGame(currentPath):
    """
    CurrentPath holds path to current save. Is needed for overwriting saves.
    Call this when saving a new game. 
    Dependent on "tempUserData" directory existing.
    """
    if currentPath == r"saved_games\tempUserData":
        # if current game IS named tempuserdata
        saveName = str(input("\u001b[32mWhat would you like to name your save file? >>> "))
        print("\u001b[37m")
        path = "saved_games"
            
        if saveName == "tempUserData":  # can't have it named the default cause it'll break "start new game"
            print("Exiting savegame as 'tempUserData' is a forbidden filename for this process.")
            print("Enter savegame command again to restart process using a different filename.\n")

        else:
            savePath = str(os.path.join(path, saveName))  # joins the path with included backslash
            print("Your current game", saveName, "has been saved.")
            print("\u001b[32m\nNow back to the show!")
            print("\u001b[37m")
            os.rename(currentPath, savePath)  # source, destination
            startRoom(savePath)  # takes new save name, sets as path, and recalls the game in that save.
            
    else:
        # if game name is NOT named tempUserData            
        NewCurrentPath = os.path.basename(currentPath)
            
        path = "saved_games"
        saveName = NewCurrentPath
            
        savePath = str(os.path.join(path, saveName))  # joins the path with included backslash
        print("Your current game", saveName, "has been saved.")
        print("\u001b[32m\nNow back to the show!")
        print("\u001b[37m")
        os.rename(currentPath, savePath)  # source, destination
        startRoom(savePath)  # takes new save name, sets as path, and recalls the game in that save.
    pass


"""----------------------In Game Menu----------------------"""
def inGameMenu(path):
    # Main game loop
    print("\n")
    print("          ----------")
    print("          |  Menu  |")
    print("          ----------")
    print("1: Back to Game")
    print("2: Main Menu")
    print("3: Save Game")
    print("4: Quit Game")

    choice = input()

    if choice == "1":  # Back to Game
        pass  # this should stop function call and return back to the current game loop

    elif choice == "2":  # Main Menu
        playGame()

    elif choice == "3":  # Save Game
        saveGame(path)

    elif choice == "4":  # Quit Game
        exitGame()

    else:
        print("Please choose an available option.")
        inGameMenu()



"""--------------------------------------------------------------------Rooms------------------------------------------------------------------"""
def r1_wilderHouse(path):
    """
    Features: Oompa Loompa, Key Holder
    Objects: Dogecoin, Tesla Key

    Plot: This is Gene Wilder's fomer home, which is where Elon now lives. There is an Oompa Loompa
          butler that Elon can take a Dogecoin from. There is also a Key Holder on the wall that
          holds his Tesla Key, which he can take.
    """
    
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@*+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@+..+%@*=%@@@@@@@@@@@@@@@@@@@@@%####%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*%@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@+::-=::+*#@@@@@@@@@@@@@@@@%%#*+**##%%@@@@@@@@@@@@@@@@@@@@@@%#@@@+.. #@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@%=:::--=+#@%@@@@@@@@@@%#########%%%@@@@@@@@@@@@@@@@@@@@@%-=#=:.. =@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@*=.:-#++@%@@@@@@@@#####*+++***##%%%@@@@@@@@@@@@@@@@@%- :...:-*@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@=+.*%+#@@@@@@@@%**+#**=--=+****##@@@@@@@@@@@@@@@@%=--%-=+*%@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@*=*:%%@@@@@@@@@%####%*=**%#*###%*%@@@@@@@@@@@@@@@**-+#:%%@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@#%%%%%%@@@@@@%%#*#%@#*++****%%%%%%%@@@@@@@@@@@@@%###%%%@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@##%%%%%@@@@#####%%%##*****#%%%%#%%%@@@@@@@@@@@%##%%%@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@@##%%%%@#*******#%%#%%%#@@@@@@@@@@@%##%%%@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@%#%%%%%%@@@@%%%@@%##******##%#%%%@@@@@@@@@@@%###%%%@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@@@%##%-#:-##++#%####%%%@@@@@@@%%####%%%@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@%%%%%%@@@@@@@@*--==+%#.:%%+%%*::-%%%%%%####%%%%%@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@%%+:-=#%#*%@%%%*::-%%%%%%#%%%%%%@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@%%%%*::-*%%%%%%%#::=%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@@@%%%%%%-::=#%%%%%#:-+%@%@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%=.::+%%%%*--+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%###%%%%+..:-#%%=--*@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%#####%%%#:.::+%---#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%#######%%%%=:::---=%@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#########%%%%+:::--+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######%%%%%%%%#::--#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%#%%%%%%%%%%=::--=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print("\n")

    roomPath = r"\rooms\r1_wilderHouse.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
        
    # Update current room in elon.json
    currentRoom = r"r1_wilderHouse"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    loopFlag = True
    while loopFlag == True: 
           
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")

        # Talk to Oompa Loompa
        elif choice in ('talkoompaloompa', 'oompaloompa'):
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            if "dogeCoin" in inventory:
                print("Oompa Loompa Doopety Dee, why don't you give something to me?")
            else:
                print("He proceeds to break out in song.")
                print("'Oompa Loompa Doompety Doo, I've got a very nice Dogecoin for you!'")
                print("He then offers you the Dogecoin.")
                        
        # Go to the Tesla
        elif choice in ('east', 'goeast', 'gotesla', 'tesla'):
            # check if Tesla key is in inventory
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            if "teslaKey" in inventory:
                r2_teslaRide(path)
                loopFlag = False
            else:
                print("You need the Tesla key first.")
        
        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()

        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")


def r2_teslaRide(path):
    """
    Features: GPS, Ludicrous Mode
    Objects: None

    Plot: This is Elon's transportation between his house, Grimes's House and SpaceX Headquarters.
          He needs the Tesla Key to use it. He needs to have the GPS turned on to go anywhere because
          he has a horrible sense of direction. He can also use the car's Ludicrous Mode just because.
    """
    
    print(u"\u001b[40;1m                                                                        .................:\u001b[0m")
    print(u"\u001b[40;1m                                                                               ...........\u001b[0m")
    print(u"\u001b[40;1m                                                                                         .\u001b[0m")
    print(u"\u001b[40;1m                                             .....::::::::::::::::..                     .\u001b[0m")
    print(u"\u001b[40;1m               ..                    ..::--==++==+++***#*+*++********+-:.                .\u001b[0m")
    print(u"\u001b[40;1m.     .::.:..::::::..:..:....... ..:-======+*#++*#**##**#%#####%%#######*+=---::.........:\u001b[0m")
    print(u"\u001b[40;1m:.......................:::::...-=+++*****##%####%%#**%%%%%%%%%%%%#########==:::.::::-----\u001b[0m")
    print(u"\u001b[40;1m................ .....  .:.:-=++*****######%%%#%%%**%%%%%%%%%#%%%#*******+++++=::::::::::-\u001b[0m")
    print(u"\u001b[40;1m......... .....:--::.......:--====+++**####%%%%%%=*##************#########**#**+++.......:\u001b[0m")
    print(u"\u001b[40;1m...........:=*+=:....:--=++++=--==++*#%%%%%%%%%%%%%%%%%%%%%%%%###%%#######*####*-=:.......\u001b[0m")
    print(u"\u001b[40;1m........ :--:::-=+**##%%#+=====-==*%%%%%%%%%#####%%%%%%%####*************#%##%%@%=........\u001b[0m")
    print(u"\u001b[40;1m......:-=+**#########*===+++++*%%%%%%%%#*#%@@@###**************************%=-:-=#........\u001b[0m")
    print(u"\u001b[40;1m......-+*#########%%#####%%%%%%%%%%%#+-=----*%@*++************#####***+++*##+===-=........\u001b[0m")
    print(u"\u001b[40;1m......-+***####%%%%%%%%%%%%%%%%%%%%+-------=:+@%++*********########*******%#==++=.........\u001b[0m")
    print(u"\u001b[40;1m......-*++++***#####%%########%%%%#-===++--=-:%%+++*******#####%%%%@@@@@@@@@*+=+#*+=-:...:\u001b[0m")
    print(u"\u001b[40;1m......:#@@@@@@%%%%%%%%%%%%%%%%%%#%+=++=*++==--%%**##%%%%@@@@@@@@@@@@@@@@@@%%%#**+==-:....:\u001b[0m")
    print(u"\u001b[40;1m........-+*%%@@@@@@@%%%%%%%%%%%%#@#=====+=+=-*@@@@@@@@@@@@@@@%%%%%###*++==-:.............:\u001b[0m")
    print(u"\u001b[40;1m.......*#%%@@@@@@@@@@@%%%%%@@%%%%@@*-=*++=--#@@@@@%%%%%%###*++=--:.......................:\u001b[0m")
    print(u"\u001b[40;1m........-=*#%%%%%@@@@@@@@@@@@@@@@@@@%**++*#%%%###*++=--::................................:\u001b[0m")
    print(u"\u001b[40;1m    ..:::: :+-........=###%%%%%%%%%###**++=--::..........................................:\u001b[0m")
    print("\n")
    
    roomPath = r"\rooms\r2_teslaRide.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # Update current room in elon.json
    currentRoom = r"r2_teslaRide"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance for the room
    textparser = TextParser()

    gpsOnFlag = False
    ludicrousModeFlag = False
    loopFlag = True
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")
        
        # Go to Grimes's House
        elif choice in ('north', 'gonorth', 'gogrimeshouse', 'grimeshouse'):
            if gpsOnFlag is True:
                print("You select Grimes's House on the GPS the Tesla starts driving.\n")   
                r3_grimesHouse(path)
                loopFlag = False
            else:
                print("You need to use the GPS. You don't know how to get there because the car always drives.")
        
        # Go to SpaceX Headquarters
        elif choice in ('south', 'gosouth', 'gospacexheadquarters', 'spacexheadquarters'):
            if gpsOnFlag is True:
                print("You select SpaceX Headquarters on the GPS the Tesla starts driving.\n")  
                r5_spaceXHQ(path)
                loopFlag = False
            else:
                print("You need to use the GPS. You don't know how to get there because the car always drives.")

        # Go to Gene Wilder's House    
        elif choice in ('west', 'gowest', 'gogenewilderhouse', 'genewilderhouse'): 
            if gpsOnFlag is True:
                print("You select Gene Wilder's House on the GPS the Tesla starts driving.\n")  
                r1_wilderHouse(path)    
                loopFlag = False
            else:
                print("You need to use the GPS. You don't know how to get there because the car always drives.")

        # Use Ludicrous Mode
        elif choice in ('ludicrousmode','ludicrousmode','useludicrousmode', 'pushbutton'):
            if ludicrousModeFlag is True:
                print("No way dude, we're not doing that again, I didn't bring a third pair of pants with me.")
            else:
                ludicrousModeFlag = True
                print("Last time you did this you got a speeding ticket that you still haven't paid.")
                print("But what the heck.")
                print("LUDICROUS SPEED! GOOOOOOOO!!!!!!!!")
                print("You push the button.\n")
                
                print(u"\u001b[44;1m  .=#@@@@@@#-    :*@@@#:  :%@@+  +@@- :@@= :@@- =@@- .@@%:  +@@@=   :*@@@@#=.     -*%@@@@@\u001b[0m")
                print(u"\u001b[44;1m      :+%@@@@@*:   .+@@@#.  +@@#  *@@. #@* :@@. %@*  %@%. :%@@+   -#@@@%+.    .=#@@@@@@@@*\u001b[0m")
                print(u"\u001b[44;1m*=:      .=*@@@@@+:   =%@@*. :%@#. *@* -@% :@% :@%  #@*  +@@*.  =%@@@+:    -+%@@@@@@#+-.  \u001b[0m")
                print(u"\u001b[44;1m@@@@%*=.     :+#@@@%+:  -#@@+  =@%: *@- %@ :@* *@: #@+ :%@#. .+@@@*:   :=#@@@@@%*=:       \u001b[0m")
                print(u"\u001b[44;1m@@@@@@@@@#+-     -*@@@%=. .*@@+ .%@- #@ -@-:@= @* #@- +@%: :#@@#-   -*@@@@@#+-        .-+#\u001b[0m")
                print(u"\u001b[44;1m  :-+*%@@@@@@%*=:   :=#@@#=..+%@= +@+.%* %+:@.=@ *@-:%%- -#@#=. :=#@@@%*=:     .:-+#%@@@@@\u001b[0m")
                print(u"\u001b[44;1m        .-=*%@@@@@#+-.  -*%@#- -#%-.#*.@-=#:@ %-+%.=@=.=%%+. -*@@@#+-     :=+#@@@@@@@@@@@%\u001b[0m")
                print(u"\u001b[44;1m#*+=-:.       .:=+#@@@%*=: .=#@*-:*#-+#:%:%:#-#-#:#*:+%+::=#@%*=:  .:=*#@@@@@@@@%#*+=-:.  \u001b[0m")
                print(u"\u001b[44;1m@@@@@@@@@%#*+=-:.    .-+*%@%*=:-+#*-+*=*-**=+#=*+*=**-=*%#=:..-+*%@@@@%#*+=-:.            \u001b[0m")
                print(u"\u001b[44;1m++**##%%@@@@@@@@@@@%#*+=-:..-=*##+==++++*++**+*+++++**=--+#%@%#*+=:.         .::--==+**##%\u001b[0m")
                print(u"\u001b[44;1m            ..::--==++**##%%%#**+++*+=**********+**+=++==--:::--=++**##%%@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[44;1m                   ...........::--=++*++**%@@##*+===++**##***********************+++++++++\u001b[0m")
                print(u"\u001b[44;1m@@@@@@@@@@@@@@@@@@@@@@@@%%##*++==++**+++**#%%#*****+=++***+++==--::...                    \u001b[0m")
                print(u"\u001b[44;1m@@@@@@%%##**+==--::.    :-=+*##*+=++++*+****+**+*=*+++*+=-::-=+*#%@@@@@@@@%%##***++==--:::\u001b[0m")
                print(u"\u001b[44;1m:..            .:=+*#%@@@#*=:.-+##==*+=*++*#+=**=*+=**=:-+%@#*=-.   .:-=+*#%@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[44;1m      .:=+*#%@@@@@@#*=:. :=*%%+-:+#=-#=+++-%-#++++-#*-=#%+-.:=*%@@%*+-:.      .:-=+*#%@@@@\u001b[0m")
                print(u"\u001b[44;1m+*#%@@@@@@@@@#+=:    :+#@@#=..=%%-.*%:**:@.@ @:%==@--%#-.=%@#=. .-+#@@@@@#*=-.          .:\u001b[0m")
                print(u"\u001b[44;1m@@@@@@@#*=:.    .-*%@@@*-  -#@#-.+@+.##.%+-@ %*:@-:%*.=%%= :+%@%*-.  .-+#@@@@@@%*+-:      \u001b[0m")
                print(u"\u001b[44;1m%#+=:       :+#@@@@#=:  -*@@*. =@%..%% *@.=@ +@.=@-.#@- =%@*: .+%@@%+:    :=+%@@@@@@@@#*=-\u001b[0m")
                print(u"\u001b[44;1m       .-*%@@@@@*-   .+@@@+. =@@+ -@@.:@# *@ :@+ %@- *@#. =@@#-  :+@@@@#=.     :=*@@@@@@@@\u001b[0m")
                print(u"\u001b[44;1m   :=*%@@@@@%+:   .=%@@%=  :#@%: -@@: %@: %@  @@ .@@: +@@= .+@@%=   :*@@@@%*-.     .-+#@@@\u001b[0m")
                print(u"\u001b[44;1m+#@@@@@@@*=.    -#@@@%-  .*@@+  =@@: =@%  @@  #@= -@@. -@@#.  *@@@*.   :*@@@@@%+:       .-\u001b[0m")
                print(u"\u001b[44;1m@@@@@%+-     :*@@@@*:  .*@@@-  +@@- .@@= :@@. +@%  *@%. .%@@=  .#@@@#:    -#@@@@@@*=.     \u001b[0m")
                print("\nYou come to a screeching halt, somehow still in one piece, but who knows where.")
                print("Help me GPS, you're my only hope.")
        
        # Use GPS
        elif choice in ('usegps', 'gps'):
            if gpsOnFlag is True:
                print("It displays the same three locations it can take you to:")
                print("Go North to Grimes's House")
                print("Go West to Gene Wilder's House")
                print("Go South to the SpaceX Headquarters")
            else:
                print("You turn on the GPS. It displays three locations it can take you to:")
                print("Go North to Grimes's House")
                print("Go West to Gene Wilder's House")
                print("Go South to the SpaceX Headquarters")
                gpsOnFlag = True

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look       
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()

        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")

 
def r3_grimesHouse(path):
    """
    Features: Grimes, Safe
    Objects: Mixtape, Doge hat
    
    Plot: Elon visits Grimes to collect items for his trip to Mars. Grimes tell him she
          put his things in the safe because their child kept chewing on them. He can take
          Doge hat, ID and mixtape he gave her a long time ago from the safe.
    """
    
    print(u"\u001b[40;1m           -+#################################################################+-          \u001b[0m")
    print(u"\u001b[40;1m         *#**###################################################################:.        \u001b[0m")
    print(u"\u001b[40;1m        .####+..  .          .                                             =##**=:        \u001b[0m")
    print(u"\u001b[40;1m        .###...   .  .....................................................   ###=:        \u001b[0m")
    print(u"\u001b[40;1m        .### .    .  .....................................................   *##=:        \u001b[0m")
    print(u"\u001b[40;1m        .### .....:  .....................................................   ###=:        \u001b[0m")
    print(u"\u001b[40;1m        .###                                   ..: :-::   :*=                ###=:        \u001b[0m")
    print(u"\u001b[40;1m        .###::::::::::::::.:::::-::::::::::::::::::::::::::::::::::::::::::::###=:        \u001b[0m")
    print(u"\u001b[40;1m        .#######################################################################=:        \u001b[0m")
    print(u"\u001b[40;1m        .###===========#%%-. : :*%###++++++++       ####*=. .:-#%+===========###=:        \u001b[0m")
    print(u"\u001b[40;1m        .###**#*******+%@:      :%###++++++++.     :##%#.      :%#+*********+###=:        \u001b[0m")
    print(u"\u001b[40;1m        .###==+++======%%=      :%%##########*******##%%:      -@*+++++++++++###=:        \u001b[0m")
    print(u"\u001b[40;1m        .###+**+*++++*++#%+::.:+%@%%%%%%%%%##%%%#########=:  :+%#++++++++++++###=:        \u001b[0m")
    print(u"\u001b[40;1m        .#######################################################################=:        \u001b[0m")
    print(u"\u001b[40;1m        .###==------=====================-=---===--=========================-###=:        \u001b[0m")
    print(u"\u001b[40;1m        .###==------=-===-=================-=================================###=:        \u001b[0m")
    print(u"\u001b[40;1m        .###==-----=====---==================================================###=:        \u001b[0m")
    print(u"\u001b[40;1m        .####****************************************************************###=:        \u001b[0m")
    print(u"\u001b[40;1m        .###########%###########################################################=:        \u001b[0m")
    print(u"\u001b[40;1m        .###########%################%#%############################%###########=:        \u001b[0m")
    print(u"\u001b[40;1m        .##########%%##############%###%########################################=:        \u001b[0m")
    print(u"\u001b[40;1m        .##########@%#####=*%%##%:.##################::+%##%#+*%################=:        \u001b[0m")
    print(u"\u001b[40;1m        .=########%%######  ####%+-##################=-+###%=  *################=:        \u001b[0m")
    print(u"\u001b[40;1m         .=+*****************************************************************+=-.         \u001b[0m")
    print("\n")

    roomPath = r"\rooms\r3_grimesHouse.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r3_grimesHouse"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    loopFlag = True
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")
        
        # Talk to Grimes
        elif choice in ('talkgrimes', 'grimes'):
            print("You say hello.")
            print("'Hi, Elon', she replies. You can tell she's distracted.")
            print("'I'm like SO into this book right now so I can't talk.'")
            print("'I put your Doge hat and ID in the safe because Ash kept chewing on them.'")
            print("'So THAT'S how you say his name!' you think to yourself.")
            print("'Oh I put that stupid mixtape you made me 3 years ago in there too. God I hate nu-metal so much.'")

        # Open Safe
        elif choice in ('opensafe', 'safe'):
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            print("You open the safe.")
            if ('dogeHat' in inventory) and ('ID' in inventory) and ('mixtape' in inventory):
                print("The safe is empty.")
            elif ('dogeHat' in inventory) and ('ID' in inventory) and ('mixtape' not in inventory):
                print("You see the mixtape inside.")
            elif ('dogeHat' in inventory) and ('ID' not in inventory) and ('mixtape' not in inventory):
                print("You see the ID and mixtape inside.")
            elif ('dogeHat' not in inventory) and ('ID' in inventory) and ('mixtape' in inventory):
                print("You see the Doge hat inside.")
            elif ('dogeHat' not in inventory) and ('ID' in inventory) and ('mixtape' not in inventory):
                print("You see the Doge hat and mixtape inside.")
            elif ('dogeHat' in inventory) and ('ID' not in inventory) and ('mixtape' in inventory):
                print("You see the ID inside.")
            else:
                print("You see the Doge hat, ID and mixtape inside.")
       
        # Go to Tesla
        elif choice in ('south', 'gosouth', 'gotesla', 'tesla'):
            # check if Tesla key is in inventory
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            if "teslaKey" in inventory:
                r2_teslaRide(path)
                loopFlag = False
            else:
                print("You need the Tesla key first.")  

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()

        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")            
   

def r4_rdLab(path):
    """
    Features: Spacesuit Rack, Lead Scientist, Chief Engineer
    Objects: Spacesuit, Launch Codes
    
    Plot: Elon visits the SpaceX Research & Development Labs. He talks to the Lead Scientist and she tells
          him his Spacesuit is on the Spacesuit Rack, which he can take. He then talks to the Chief Engineer,
          and he tells him he has the Launch Codes, which he takes.  
    """
    
    print(u"\u001b[40;1m                                        ..:-=====-::.                                     \u001b[0m")
    print(u"\u001b[40;1m                                      :+*#%%@@@@%%%%#+-:.                                 \u001b[0m")
    print(u"\u001b[40;1m                                    .=*#%@@@@@=  :@@@@%#=:                                \u001b[0m")
    print(u"\u001b[40;1m                                   .+*#%@@@@@@.  -@@@@@%#+:                               \u001b[0m")
    print(u"\u001b[40;1m                                   =*###**#@@@%#%@@@@@@@%#*-                              \u001b[0m")
    print(u"\u001b[40;1m                                  .*###%*+=+@@%@@@@@@@@@%%**:.                            \u001b[0m")
    print(u"\u001b[40;1m                                  -*##@@#**%@@@@@@@@***#*%##=-                            \u001b[0m")
    print(u"\u001b[40;1m                                  =+##@@***%@@@@@@@@#***+###*+.                           \u001b[0m")
    print(u"\u001b[40;1m                                  -**@@@@%@@@@@@@@@@@@@@%%%##*=                           \u001b[0m")
    print(u"\u001b[40;1m                                  .**@@@@@@@@@@@@@@@@@@@@%%%*.-                           \u001b[0m")
    print(u"\u001b[40;1m                                   =%@@@@@@@@@@@@@@@@@%%%##*+..                           \u001b[0m")
    print(u"\u001b[40;1m                                    +#%%%@@@@%%%%%%%%%##**###=                            \u001b[0m")
    print(u"\u001b[40;1m                                    -#####*###%%%%%##%%#####*-                            \u001b[0m")
    print(u"\u001b[40;1m          :=:                 .:---=*%%%%%%%%%%%%%%%@%@%%#**=.....                        \u001b[0m")
    print(u"\u001b[40;1m         -==               :-==+=++=+#%%%%%%%%%%%@@%%#*++====+=====-:.         --.        \u001b[0m")
    print(u"\u001b[40;1m   -=--::++=              =++++***+++++**###***+*++++++++=+++++++++++=+.       -=-        \u001b[0m")
    print(u"\u001b[40;1m  -+++*#*+++.            +*++++****+++++++++++=-++++=++=++++++++++++=++=       =++.:...   \u001b[0m")
    print(u"\u001b[40;1m .***%%%#++*+           -=++******+++=====+++*+++=++=---==-=++**++++++=+:     -==*+++**-  \u001b[0m")
    print(u"\u001b[40;1m -#####%+++**-         -*++=+++##**+=++====+=-=+===++++===++****++++==+*=.   .++**%####*  \u001b[0m")
    print(u"\u001b[40;1m  *%%%#+++*##*=      .--===++**#*++=+*+-=+=++=++++++++++++********+++==*++.  ++=*######*  \u001b[0m")
    print(u"\u001b[40;1m   .-+###%#%##*=-.   :=+*+*****#***+**++++++=-+===++====++**##%%++==+==+++= :**+*****##=  \u001b[0m")
    print(u"\u001b[40;1m      :%%@@%%##**=.-*###########*#**********--+======---++###%#**++++**++*+:+****#%%%#-   \u001b[0m")
    print(u"\u001b[40;1m       .+@@%%@@###=++%#**+***#%%**##****++**==+++++++--++***#%***++*****#=+*#####%%-      \u001b[0m")
    print(u"\u001b[40;1m         .+%%%%%%###*+#%#%@@@@%%+**##**++**+-=+++++****###*####%##*+**#*+*##%%%@@%-       \u001b[0m")
    print("\n")

    roomPath = r"\rooms\r4_rdLab.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message
    
    # update current room in elon.json
    currentRoom = r"r4_rdLab"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    scientistApproachedFlag = False
    suitTakenFlag = False
    launchCodesTakenFlag = False
    loopFlag = True
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")
        
        # Talk to Scientist
        elif choice in ('talkleadscientist', 'talkscientist'):
            if scientistApproachedFlag is False:
                print("You approach the Lead Scientist and greet her.")
                print("How's it going, Elon? Are you excitied for the mission?' shes asks.")
                print("'Oh yeah, most definitely. I'm just gathering up what I need now.' you reply.")
                print("'Perfect timing!' she says 'Your spacesuit is ready and hanging on the spacesuit rack.'")
                scientistApproachedFlag = True
            else:
                print("'Have fun on the mission, I'm jealous I'm not going too!' she says.")
                print("Don't forget to grab your spacesuit!")

        # Go to Spacesuit Rack
        elif choice in ('gospacesuitrack'):
            if scientistApproachedFlag is False:
                print("You walk up to the spacesuit rack, but you see the Lead Scientist trying to get your attention.")
            elif suitTakenFlag is False:
                print("You walk up to the spacesuit rack. You assume the shiny silver one")
                print("with 'ELON' written in huge sparkly letters across the chest is yours.")
                take('takespacesuit', path, path + roomPath)
                suitTakenFlag = True
            else:
                print("You walk up to the spacesuit rack, but you already have yours, so you walk away.")
        
        # Talk to Engineer
        elif choice in ('talkchiefengineer', 'talkengineer'):
            if launchCodesTakenFlag is False:
                print("You approach the Chief Engineer and greet him.")
                print("Hey, Elon, nice to see you!' he says.")
                print("'The shuttle is prepped and ready for liftoff!'")
                print("'The Launch Team just dropped off the launch codes, would you like them now?'")
                take('takelaunchcodes', path, path + roomPath)
                launchCodesTakenFlag = True
            else:
                print("'I let the Launch Team know you have the launch codes. They're ready when you are!' he says.")
        
        # Go to SpaceX Headquarters
        elif choice in ('north', 'gonorth', 'gospacexheadquarters', 'spacexheadquarters'): 
            print("You start walking back to SpaceX Headquarters.\n")  
            r5_spaceXHQ(path)
            loopFlag = False

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()

        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?") 

   
def r5_spaceXHQ(path):
    """
    Features: Mission Control Navigation Terminal, Restricted Door, Transporter
    Objects: Milky Way Galaxy Navigation Map 
    
    Plot: Use the Mission Control Navigation Terminal to get the Milky Way Galaxy Navigation Map
          needed to get to Mars. Elon can access the Restricted Door with his ID to get to the
          Transporter where he can teleport to the secret Space Force Base.
    """
    
    print(u"\u001b[44;1m                                                                             .::----::::..\u001b[0m")
    print(u"\u001b[44;1m                                                                   .:==+****+=:.          \u001b[0m")
    print(u"\u001b[44;1m                                                          .:-+*#%@%#+=:.                  \u001b[0m")
    print(u"\u001b[44;1m                                                   .:=+#%@@@%*+-:                         \u001b[0m")
    print(u"\u001b[44;1m                                             .:=*#@@@@@#+=:                               \u001b[0m")
    print(u"\u001b[44;1m                                        .-+#@@@@@@%+-.                                    \u001b[0m")
    print(u"\u001b[44;1m .:::::::::::                      .-+#@@@@@@@#=:                                         \u001b[0m")
    print(u"\u001b[44;1m =%@@@@@@@@@@%+.               :=#@@@@@@@@*=.                                             \u001b[0m")
    print(u"\u001b[44;1m   .+@@@@@@@@@@@#-         :+#@@@@@@@@#=.                                                 \u001b[0m")
    print(u"\u001b[44;1m      -*@@@@@@@@@@@*   :=#@@@@@@@@%+:                                                     \u001b[0m")
    print(u"\u001b[44;1m         =#@@@@@#+:.-*@@@@@@@@@#=.                                                        \u001b[0m")
    print(u"\u001b[44;1m           .+*- .=#@@@@@@@@@#=.                                                           \u001b[0m")
    print(u"\u001b[44;1m             .=#@@@@@@@@@%=.-                                                             \u001b[0m")
    print(u"\u001b[44;1m           =#@@@@@@@@@@+.:*@@@*:                                                          \u001b[0m")
    print(u"\u001b[44;1m        -*@@@@@@@@@@*: -%@@@@@@@@+.                                                       \u001b[0m")
    print(u"\u001b[44;1m     .+%@@@@@@@@@%+.  .+@@@@@@@@@@@%=                                                     \u001b[0m")
    print(u"\u001b[44;1m   :*@@@@@@@@@@%-        :*@@@@@@@@@@@#-                                                  \u001b[0m")
    print(u"\u001b[44;1m :#@@@@@@@@@@#:             -#@@@@@@@@@@@*:                                               \u001b[0m")
    print(u"\u001b[44;1m=@@@@@@@@@@*.                 .=%@@@@@@@@@@%.                                             \u001b[0m")
    print("\n")

    roomPath = r"\rooms\r5_spaceXHQ.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r5_spaceXHQ"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    loopFlag = True
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")
        
        # Go to Navigation Terminal
        elif choice in ('gonavigationterminal', 'navigationterminal'): 
            print("You walk up to the Mission Control Navigation Terminal.")
            print("What a sweet machine. Just think of how many Dogecoins you could mine with this.")
            print("You see a disk with 'Milky Way Galaxy Navigation Map' written on it sitting on the console.")
        
        # Open Restricted Door
        # Restricted Door requires ID to get in because it contains acces to the secret telporter room
        elif choice in ('openrestricteddoor', 'opendoor', 'useidopenrestricteddoor', 'useidopendoor'):
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            if "dilithiumCrystals" in inventory:
                print("You saw everything and bribed the guard once already, so you decide to not risk it again.")
            else:
                print("You approach the mysterious door.")
                print("The scanner's robotic voice announces 'You are attempting to enter a restricted area.'")
                print("'Please scan your ID for access.'")
                if "ID" in inventory:
                    print("You hold your ID up to the scanner and the door opens.")
                    print("You walk inside and see what looks just like the Transporter from the USS Enterprise.")
                    print("You ask a lone technician wearing a strangely familiar-looking red shirt what this is.")
                    print("'It's the Transporter, Captain!' he responds.")
                else:
                    print("You don't have your ID with you, so you walk away from the door.")

        # Use Transporter to teleport to the Space Force Base
        elif choice in ('usetransporter','useteleporter' , 'gotransporter', 'goteleporter', 'transporter', 'teleporter'): 
            print("You enter the Transporter.")
            print("'Where does thing go?' you ask the technician.")
            print("To the Space Force Base, Captain!' he replies.")
            print("'Well then, beam me up, Scotty!' you shout!")
            print("'My name is Kowalski, Captain!' he yells back.")
            print("You feel a strange sensation as you start to dematerialize...\n")
            r6_spaceForceBase(path)
            loopFlag = False
        
        # Go to Tesla
        elif choice in ('north', 'gonorth', 'gotesla', 'tesla'):
            # check if Tesla key is in inventory
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            if "teslaKey" in inventory:
                print("You head back to the Tesla.\n")
                r2_teslaRide(path)
                loopFlag = False
            else:
                print("You need the Tesla key first.")

        # Go to R & D Lab
        elif choice in ('south', 'gosouth', 'gor&dlab', 'r&dlab'):
            print("You head to the R & D Lab.\n")
            r4_rdLab(path)
            loopFlag = False

        # Go to Launch Pad
        elif choice in ('east', 'goeast', 'golaunchpad', 'launchpad'):
            print("You head to the Launch Pad.\n")
            r7_launchPad(path)
            loopFlag = False

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()

        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")


def r6_spaceForceBase(path):
    """
    Features: Space Force Soldier, Fuel Depot
    Objects: Dilithium Crystals
    
    Plot: This is the secret Space Force Base where Elon can get Dilithium Crystals for the
          Shuttle propulsion system if he can make it past the Space Force Guard,
          which he can do if he has the Dogedog hat. He teleports back to SpaceX Headquarters when he is
          done.
    """

    print(u"\u001b[35;1m                                          `:,`.                                           \u001b[0m")
    print(u"\u001b[35;1m                                        .;I^'`^,,'                                        \u001b[0m")
    print(u"\u001b[35;1m                                      ;i^`,;;;;;'. ..`''`                                 \u001b[0m")
    print(u"\u001b[35;1m                                    '~,^`';;;;;,,''    ^''                                \u001b[0m")
    print(u"\u001b[35;1m                                   ;!^``'^^^'^',,:;..... -         .:>I;`.                \u001b[0m")
    print(u"\u001b[35;1m                             '``  ,'```^':;;;;;;;;;' ... :'      .;<^',^.^,`              \u001b[0m")
    print(u"\u001b[35;1m                       '^':I;,''i 'l'^^^`'lII;;;;;;;......;     ^+'`';;;,' .''`           \u001b[0m")
    print(u"\u001b[35;1m                 ''':!;,^``^,::`'i ].^^^^`iiiiiiii!!`.''. ~   `>'^`,;;;;;;^  .',,'        \u001b[0m")
    print(u"\u001b[35;1m                l'``````^,;;;;;' '>',`^^^`![]?-_+~<>;.```'`''`<,^^`'':,,,''''`   `,       \u001b[0m")
    print(u"\u001b[35;1m               ','^^^``^^',;;;;:. '>}.^^^^,)11}}}}}}[''```.{'````'',,,::;;;;' ... (       \u001b[0m")
    print(u"\u001b[35;1m              'l'^^^``;;;:,^^^':'  `\,I!!I,'^:)}}}}}}:.^^^',^`^^^':;;;;;;;;;` ... _       \u001b[0m")
    print(u"\u001b[35;1m             '+'^^^^`l!;;;;;;;::,,;I:'^`^':;,'')}}}}}[.`^^`.i'^^^`:i!!lI;;;;' ... ;'      \u001b[0m")
    print(u"\u001b[35;1m            ._'^^^^`i>i>l;;;;I]```````':;;;;;` '{]]]]]''^^,'-:III:!?_++_++i!;.'.. ^'      \u001b[0m")
    print(u"\u001b[35;1m            -'`^^^`i}}->i>l;;]``^^^'`^^':;;;;,  ^){{{1?.^^]'^`'. .  .....'~+i.'``'',      \u001b[0m")
    print(u"\u001b[35;1m           +``^^^`;1)11}->i>?''^^^`^;;;:'^^^':. .^{il;;'.'!`,;;;:'`'.   .. '{.'```.1      \u001b[0m")
    print(u"\u001b[35;1m          <^`^^'^I<^`^,:;l;!<:IllI,!l;;;;;;;:'   '`-i~i^^-,`,I;;;;,^^'. .....;,^``.{      \u001b[0m")
    print(u"\u001b[35;1m         I,'^^'!:^,:^,^,^',^,,',',I!lilIIIII;'.`'`'+><,,,?ll,:l<~;i!III^^'^'` `>'^.i'     \u001b[0m")
    print(u"\u001b[35;1m        'I'^,i,^`'',^^`,`,;II;I;,';__il>lI;;`'.''.:+i;:i:'^^'^`^''::;;i+>``'`''.:l',:     \u001b[0m")
    print(u"\u001b[35;1m       .|`:l^'^^^^^`^,;;;^^:;;;;` :1}[_>i>l^.... `]__;^'`^^^^^`'`^^^^^^^^,+`'```''l,_     \u001b[0m")
    print(u"\u001b[35;1m       '?l``^^^^``,!!>;;;;:^^;;,  :1}}}[_>,.`'..`?:^'`^^^^^``':;`';;;;;;,'<+`.````',1.    \u001b[0m")
    print(u"\u001b[35;1m     `+,``^^^^`^I[}-i>!;;;;;,`'.  :1}}}}}!.'`::,`'^^^^^``',;<I;;;'^;;;;:' )}};.`^^^`'<;   \u001b[0m")
    print(u"\u001b[35;1m   'i^'^^^^^`'<}}}}}+!<I;;;;;^. ..:}}}}}-'::'``^^^^^``'l]}-i>l;;;;,`:;;. `)}}}]^.`^^^'^?' \u001b[0m")
    print(u"\u001b[35;1m  {,'^^^^``:?-[}}}}}]>ii;;:`....  :{?]}[`?``^^^^^``'l[}}}}[<ii;;;;;:`'.  I}[]]]]+''^'.'~' \u001b[0m")
    print(u"\u001b[35;1m  f::;:^~???{1?]}}}}}?^'.'... .,+;;>?{,.?;:;,^>??]1{-}}}}}}-i>l;''. ..  ')[[]??i,:>'^^;,  \u001b[0m")
    print("\n")

    roomPath = r"\rooms\r6_spaceForceBase.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r6_spaceForceBase"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    soldierWarningFlag = False
    loopFlag = True
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")
        
        # Talk to Guard
        # Bribe him with the Dogedog hat so he'll let you pass so you can get Dilithium Crystals from the Fuel Depot
        elif choice in ('talkguard'):
            if soldierWarningFlag is False:
                soldierWarningFlag = True
                print("The guard rushes toward you and screams 'Halt! Who goes there?!'")
                print("'Hey, you know you're not supposed to be up here, right?!'")
                print("'Especially when we're receiving dilithium crystal shipments from Theta Zeta!'")
                print("'Hey before you go, did you happen to see what Dogecoins were at today before you came up?' he asks.")
                print("'Dilithium crystals are what power warp drives' you think to yourself.")
                print("You could definitely use them for the Shuttle to get to Mars quicker.")
                inventory = getInfo(path + r"\elon\inventory.json", "objects")
                if "dogeHat" in inventory:
                    print("Maybe you can bribe him? You hand the guard your Doge hat.")
                    print("'NO WAY, AWESOME!' he exclaims. 'I never saw you' he says,\nand walks back to his post with his new hat on.")
                    inventoryPath = (path + r"\elon\inventory.json")
                    updateItems("remove", "dogeHat", "initial", inventoryPath)
                else:
                    print("Ok, seriously! Go back to the Transporter! If I see you again, it's GAME OVER!")
            else:
                print("'I warned you!' the guard screams!")
                print("He fires his blaster at you and everything goes dark.")
                print("(He wasn't lying.")
                print("\n")                              
                print(u"\u001b[31m    @@@@@@@@@@%%%%%%%%%%%%@@@@@@%%%%%%%%%%%@@@@@%%%%@@@@@@@%%%%@@%%%%%%%%%%%%%%%%@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@%%            %%@@%%           %%@@%    %%@@@%     @@                @@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@@@@@    %@@    %@@@@@@    %@%      %%       @@%    @@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@%%%%%%%%@@@    %@@@@@@    %@%    %%   %     @@%    %%%%%%%%@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@        %@@    %@@@@@@    %@%    @@% %@%    @@%            %@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@@@@@%   %@@               %@%    @@@@@@%    @@%    @@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@@@@@    %@@    %@@@@@@    %@%    @@@@@@%    @@     @@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@%          %@@@@    %@@@@@@    %@%    @@@@@@%    @@                @@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@          %@@@@%   %@@@@@@%   %@@               @@%            %@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    %%%%%%%  %%@@    %@@@@@@    %@@%   %%%%%%%%%%%@@%    %%%%%%%  %%@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@    %@@@@@@    %@@%   @@@@@@@@@@@@@%    @@@@@@%    @@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@%%   %@@@%%   %%@@%            @@@@%    %%%%%%%   %@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@@@%    @%    @@@@@%   @@@@@@@@@@@@@%             @@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@@@@@%      @@@@@@@    %@@@@@@@@@@@@%    @@@@%    @@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@%           @@@@@@@@@@@  @@@@@@@@@               @@%    @@@@@@%    @@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
                print("\n")
                exitGame()


        # Go to the Fuel Depot
        elif choice in ('gofueldepot', 'fueldepot'):
            print("You arrive at the Fuel Depot.")
            print("Those definitely were crates that you saw, brimming with big pink crystals.")
            print("There are so many, no one would ever notice if a few were missing.")

        # Use Transporter to go back to SpaceX Headquarters
        elif choice in ('usetransporter'):
            print("You return to the Transporter, step inside and push the button to return to SpaceX Headquarters.\n") 
            r5_spaceXHQ(path)
            loopFlag = False

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()

        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")



def r7_launchPad(path):
    """
    Features: Fuel Tank, Shuttle Door
    Objects: None
    
    Plot: This is the Launch Pad for the Shuttle. Elon can access the Shuttle Fuel Tank here to put
          Dilithium Crystals into the Fuel Tank. He can then open the Shuttle Door if he has his ID.
    """
    
    print(u"\u001b[40;1m..........................................................................................\u001b[0m")
    print(u"\u001b[40;1m..........................................................................................\u001b[0m")
    print(u"\u001b[40;1m................................................-*-.......................................\u001b[0m")
    print(u"\u001b[40;1m...................:...........................=%#*=......................................\u001b[0m")
    print(u"\u001b[40;1m...................:..........................:%%%#*:.....................................\u001b[0m")
    print(u"\u001b[40;1m...................:.........................:-%%%##-.....................................\u001b[0m")
    print(u"\u001b[40;1m..................::........................:-=%%%#*-: ...................................\u001b[0m")
    print(u"\u001b[40;1m..................::........................+=*%#%*:=-:...................................\u001b[0m")
    print(u"\u001b[40;1m..............::::==:.......................=-+#%#-:.-:...................................\u001b[0m")
    print(u"\u001b[40;1m..............:=***+++-.....................==*%%+--.::...................................\u001b[0m")
    print(u"\u001b[40;1m................*##***===:..................==*%%=-:.:....................................\u001b[0m")
    print(u"\u001b[40;1m................*###*+=+-:..................==*%#=-:.::...................................\u001b[0m")
    print(u"\u001b[40;1m.............:.:*++++=::....................==#%+=-:.::...................................\u001b[0m")
    print(u"\u001b[40;1m..........=++=++*##*#**-....................==#%+=-:..:...................................\u001b[0m")
    print(u"\u001b[40;1m.........-+*#*+#####*+=-....................=+*==+--. ....................................\u001b[0m")
    print(u"\u001b[40;1m.........:=****######+=----.................+=--=+-:....::................................\u001b[0m")
    print(u"\u001b[40;1m.......::-=+=*=######=-=**-................+==**++---.--::-:..............................\u001b[0m")
    print(u"\u001b[40;1m.......--+*#*++*#*-+-++=++-................=#*#*#+=++:-+**++-.............................\u001b[0m")
    print(u"\u001b[40;1m......:==+**==**=--+=*=-....................*###%%@@###**#*-..............................\u001b[0m")
    print(u"\u001b[40;1m.....:=***#*++**--+--*+:.............:.:-.::#*##*#%%%##***+---............................\u001b[0m")
    print(u"\u001b[40;1m......+:+*###%##--=+**=::........-=*#%##%%%%%%%@%##%%%##%%%%###*****:.....................\u001b[0m")
    print(u"\u001b[40;1m.::..-=:-++#*@@%#+=###*--::....:%%%%%%#%%%%%%%%##%%%%@@%%%%%###**#**-.....................\u001b[0m")
    print(u"\u001b[40;1m.:...=-:=++++%%%%%%%#*=-:......-%%%%%%%@%%@@@@@@@@@@@@@@@@%@%%%%%%#%=.....................\u001b[0m")
    print(u"\u001b[40;1m:::::=.:-=+-:--#@@@@%%-::......=%%%%@@@@%%@@@%%%@%@@@@%@@@%%%@*+=--:......................\u001b[0m")
    print(u"\u001b[40;1m::::===-=+=-:--#%@@@%#--------------*@@@@@@@@@@%@@@@%@@@@%%#%@+::.........................\u001b[0m")
    print(u"\u001b[40;1m:++-*+****+=-==#@%%%##=+=---------+@@@%%#%#%#*++++**%%%%%%%@%%%%#::.::..::-::::::::::::::-\u001b[0m")
    print(u"\u001b[40;1m-%#***+++=-++++=++=-:::---****#**+=--:::::::::::::::::::::::::::::-::-----------=--------=\u001b[0m")
    print("\n")

    roomPath = r"\rooms\r7_launchPad.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r7_launchPad"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    loopFlag = True
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")
        
        # Open the Shuttle Fuel Tank
        elif choice in ('openfueltank', 'fueltank'):
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            print("You open the fuel tank access hatch and unscrew the cap and look inside.")
            if "dilithiumCrystals" in inventory:
                print("You can put the dilithium crystals in here.")
            else:
                print("You don't have anything to put in here, so you close everything back up.")

        # Put dilithium crystals into fuel tank
        elif choice in ('putcrystalsintotank', 'putcrystalsintofueltank'):
            print("You put the dilithium crystals into the fuel tank, tighten the cap and close the hatch.")
            inventoryPath = (path + r"\elon\inventory.json")
            updateItems("remove", "dilithiumCrystals", "initial", inventoryPath)

        # Open Shuttle Door
        # Need to have ID to open it
        elif choice in ('openshuttledoor', 'opendoor'): 
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            print("You shuffle through your bag and try to find your ID.")
            if "ID" in inventory:
                print("You find it, scan it, and the shuttle door opens and you head inside.\n")
                r8_spaceShuttle(path)
                loopFlag = False
            else:
                print("You can't open the door because you don't have your ID. NO ID, NO ENTRY.")

        # Go back to SpaceX Headquarters
        elif choice in ('west', 'gowest', 'gospacexheadquarters', 'spacexheadquarters'):
            print("You start heading back to SpaceX Headquarters.\n")
            r5_spaceXHQ(path)
            loopFlag = False

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()
        
        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")

                                   
def r8_spaceShuttle(path):
    """
    Features: Barf, Shuttle Main Computer
    Objects: None
    
    Plot: This is the spacecraft Elon uses to navigate the stars with a half-Man half-Dog co-pilot named
          Barf. Barf tells Elon to enter the Launch Codes into the Main Computer so they can take off from
          Earth. Once in Earth orbit, Elon has to load the Solar System Navigation Map into the Main Computer,
          and then they can blast towards the Moon, Mars, or return to Earth.
    
    """
    
    print(u"\u001b[40;1m                                                                              .:---==---:.\u001b[0m")
    print(u"\u001b[40;1m                                                                .=----:.  :---.   .-:+  --\u001b[0m")
    print(u"\u001b[40;1m                                                               +@#:....-+-.      .:-=  .= \u001b[0m")
    print(u"\u001b[40;1m           :::::=-----------:.                               .#@+..... .+       ::=-   +  \u001b[0m")
    print(u"\u001b[40;1m        .--  +=:          .::.:---------:.                  -@%-...:.  .+      -.+:   =.  \u001b[0m")
    print(u"\u001b[40;1m   :=+==+  .+-..........:-.         .:....:::::::--::::. .:*@+::.:::...:=     :.+-:::=.   \u001b[0m")
    print(u"\u001b[40;1m +%#=:.==   -          -. ...:...::=:.         ::.     .:*@#-:::::::...:=   .::=..  -:    \u001b[0m")
    print(u"\u001b[40;1m-%#-+..-%-  -         :          .:  ...:.:.::=:.       =@+::------:...:= ...:=..  :-     \u001b[0m")
    print(u"\u001b[40;1m *%++::..   -         :          -          :.   .......%*-=-------::..-*++++-.....=      \u001b[0m")
    print(u"\u001b[40;1m  :*@#*+=-..-..       :         :.          :           +******#***+++%%%%%#%%=...=       \u001b[0m")
    print(u"\u001b[40;1m    .=#@@%-...-..-=..==:-.      -          -          .=         :*%:*###%%#%%@#+*#**=    \u001b[0m")
    print(u"\u001b[40;1m        :=**=-::::....:--. :=..-+.. ..     -          +         =%%%:-###%%%%%%##%##%%+   \u001b[0m")
    print(u"\u001b[40;1m            .-=+*====+*%#=-:::.... .=:=-. .. .        *....    :%%%==:=#%#=++####%##%%+   \u001b[0m")
    print(u"\u001b[40;1m                 :---:...:-=======+*###*-...  . .   . -+-:.....-%%%%%%#==*+ .-#+**###=    \u001b[0m")
    print(u"\u001b[40;1m                     .----.        ..:-=======--::.....:=++=-::-%%%%%+  :+##%%#*+         \u001b[0m")
    print(u"\u001b[40;1m                          :-=-:  ::         ..:-=====-:....:-=+=*##%%.  ##*######=        \u001b[0m")
    print(u"\u001b[40;1m                              .--*@@%#+.             .--==--:.....:=%* .=*##%*###-        \u001b[0m")
    print(u"\u001b[40;1m                                   :+%@@#.             :.:-=+++=-:..:#%**#:.-=+=:         \u001b[0m")
    print(u"\u001b[40;1m                                      =@@*           .:=-:..:--++++===%%#.                \u001b[0m")
    print(u"\u001b[40;1m                                       -@@:         .-=%+::-::+-..::-+=.                  \u001b[0m")
    print(u"\u001b[40;1m                                        #@*         :*##*:-.-*:....:-.                    \u001b[0m")
    print(u"\u001b[40;1m                                        :@@-         -==-:.++:....-:                      \u001b[0m")
    print(u"\u001b[40;1m                                         +@%.         .::-+-....--                        \u001b[0m")
    print(u"\u001b[40;1m                                          %@=         -.-=-::.=-                          \u001b[0m")
    print(u"\u001b[40;1m                                          =@#.      .::+:  .+=                            \u001b[0m")
    print(u"\u001b[40;1m                                           %@-     :.-+.  -=.                             \u001b[0m")
    print(u"\u001b[40;1m                                           :@%+: .::+-  :-.                               \u001b[0m")
    print(u"\u001b[40;1m                                            .+%@+::=. .-.                                 \u001b[0m")
    print(u"\u001b[40;1m                                               :::::-:                                    \u001b[0m")
    print("\n")

    roomPath = r"\rooms\r8_spaceShuttle.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r8_spaceShuttle"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    loopFlag = True
    navigationMapEnteredFlag = False
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")

        # Talk to Barf
        elif choice in ('talkbarf'):  
            print("You officially introduce yourself to Barf.")
            print("'Hello Commander, nice to finally meet you in real life!' he says as his tail wags.")
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            if "spaceSuit" in inventory:
                print("'And that's a killer spacesuit you have there, bro. Oops, I mean Sir!'")
            else:
                print("'I recommend a spacesuit for this trip, Sir, but that is just me.'")
            print("'As soon as you enter the Launch Codes into the Main Computer we can get this party started!'")

        # Enter Launch Codes into the Shuttle Main Computer
        elif choice in ('uselaunchcodes', 'enterlaunchcodesintomaincomputer'):
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            if "launchCodes" in inventory:
                print("You enter the Launch Codes into the Main Computer.")
                print("You and Barf strap in and the countdown begins.")
                print("10-9-8-7-6-5-4-3-2-1-LIFTOFF.")
                print("You are pressed back into the pilot seat as the Shuttle hurtles upward.")
                print("As you look out the cockpit window, the sky quickly changes from blue to black,")
                print("and in what seems like an instant, the Shuttle is in Earth orbit.")
                print("'Alright sir, time to load that Navigation Map into the Main Computer!' Barf says.")
            else:
                print("You don't have the Launch Codes, so you can't launch yet.")

        # Use Milky Way Galaxy Navigation Map with Shuttle Main Computer
        elif choice in ('loadmapintomaincomputer', 'loadnavigationmapintomaincomputer'):
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            if "solarSystemNavMap" in inventory:
                navigationMapEnteredFlag = True
                print("You load the Milky Way Galaxy Navigation Map into the Shuttle Main Computer.")
                print("'Looks like the Moon and Mars are the closest destinations to us, Sir' Barfs states.")
                print("'Or we can go back to Earth, if you forgot to turn off your curling iron or something.")
                print("'Where to, Sir?'")
            else:
                print("Barf says 'Umm... we need a Milk Way Galaxy Navigation Map to do that, Sir'")
                print("'We need to go back to Earth for that.'")

        # Go to the Moon
        elif choice in ('north', 'gonorth', 'gomoon'):
            if navigationMapEnteredFlag is True:
                print("Barf sets the main engines to 110% power and the shuttle blasts towards the Moon.\n")
                r9_moonBase(path)
                loopFlag = False
            else:
                print("You need to load the map Barf mentioned into the Main Computer first.")

        # Go to Mars
        elif choice in ('south', 'gosouth', 'gomars'):
            if navigationMapEnteredFlag is True:
                print("Barf sets the main engines to 110% power and the shuttle blasts towards Mars.\n")
                r12_marsBase(path)
                loopFlag = False
            else:
                print("You need to load the map Barf mentioned into the Main Computer first.")

        # Go to Earth
            print("Barf begins the re-entry sequence and the shuttle heads back to Earth\n.")
            r7_launchPad(path)
            loopFlag = False

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()
        
        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")
                                                   
                                   
def r9_moonBase(path):
    """
    Features: Moon Base Airlock, Apollo 15 Lunar Lander
    Objects: None
    
    Plot: Elon visits the Moon Base on the Dark Side of the Moon. He can leave the Moon Base Airlock and head
          to the Apollo 15 Lunar Lander, but he better be wearing his Spacesuit. The Apollo 15 Moon Rover can
          be accessed from here as well. He can also return to the Shuttle.
    """

    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+=+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=.--:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-:-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+*#@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%--#==::=:      :#@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%= .=:    :.:..     :#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@: -+++  . ::::::...  =#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:==-- .. :-::....:: =*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:.....     +.......+.=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+==:     :=====:-      ..-*##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+-.     .=::..:=-     .:=#=..=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.  :-.    :=:   -%%%#-.   -%@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+#@@@*%: =:     .:=. -#: .=   ...*@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.##%@+##*+-----=-:=+*#   -- ....:#@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.*@@%-..=+%***+#*@@@@*+-=@- :.:*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@# +****+==:....:+=====+++=#: :+*+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@%%#**=+%*%*+*======++++%*#++#%#**%@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@%+##%####*==+*+=*+====+++++++++++#@@%#%=%@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@=@@%#####*=-+===++=====++++++++++###%@@%-@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@=%@@###%##*--==+-=+++=-++++****+++=**@@@@%-@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@=%@**@#####============-=+++===++++#=+**@@@#-@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@+++-***%%%*++-++=-======+=+++===++++**+===#@@#-@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@#%%@@@@@@@+=*#=*+=-=:-*###+%%%%@@@@@@@@@#+=*++*+=@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@%****=#=*=**=-=++=%@@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@%#*+##@@@@@@@@@@@###=+%%%%##%##%@@@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*%#**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%+*#%@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%*%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print(u"\u001b[40;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*++++**%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
    print("\n")

    roomPath = r"\rooms\r9_moonBase.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r9_moonBase"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    loopFlag = True
    airlockFlag = False
    suitOnFlag = False
    while loopFlag == True:

        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")

        # Put on Spacesuit
        elif choice in ('usespacesuit', 'wearspacesuit'):
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            if "spaceSuit" in inventory:
                print("You slip into you spacesuit for your Moon travels.")
                suitOnFlag = True
            else:
                print("You forgot to bring your spacesuit. I wouldn't go outside if I were you.")

        # Open Moon Base Airlock
        # You better have your Space Suit on or it's gonna suck
        elif choice in ('openmoonbaseairlock', 'usemoonbaseairlock'):
            # IF NO SUIT ON, DEATH...GAME OVER
            if suitOnFlag is False:
                print("The shuttle airlock hisses and opens.")
                print("'This is not good, I can't breath...I think I missed something important...")
                print("You quickly lose consciousness.")
                print("\n")
                print(u"\u001b[31m    @@@@@@@@@@%%%%%%%%%%%%@@@@@@%%%%%%%%%%%@@@@@%%%%@@@@@@@%%%%@@%%%%%%%%%%%%%%%%@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@%%            %%@@%%           %%@@%    %%@@@%     @@                @@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@@@@@    %@@    %@@@@@@    %@%      %%       @@%    @@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@%%%%%%%%@@@    %@@@@@@    %@%    %%   %     @@%    %%%%%%%%@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@        %@@    %@@@@@@    %@%    @@% %@%    @@%            %@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@@@@@%   %@@               %@%    @@@@@@%    @@%    @@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@@@@@    %@@    %@@@@@@    %@%    @@@@@@%    @@     @@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@%          %@@@@    %@@@@@@    %@%    @@@@@@%    @@                @@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@          %@@@@%   %@@@@@@%   %@@               @@%            %@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    %%%%%%%  %%@@    %@@@@@@    %@@%   %%%%%%%%%%%@@%    %%%%%%%  %%@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@    %@@@@@@    %@@%   @@@@@@@@@@@@@%    @@@@@@%    @@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@%%   %@@@%%   %%@@%            @@@@%    %%%%%%%   %@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@@@%    @%    @@@@@%   @@@@@@@@@@@@@%             @@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@@@@@%      @@@@@@@    %@@@@@@@@@@@@%    @@@@%    @@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@%           @@@@@@@@@@@  @@@@@@@@@               @@%    @@@@@@%    @@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
                print("\n")
                exitGame()
            else:
                print("The airlock hisses and opens.")
                airlockFlag = True
        
        # Go to Lunar Lander
        elif choice in ('golunarlander', 'golander'):
            if airlockFlag is True:
                print("You walk to the Lunar Lander.")
                print("Gear the mission left behind is strewn all over the place.")
                print("You'd almost swear it had been picked through with how messy it is.")
                print("Amongst the astronaut footprints on the ground you see many smaller footprints.")
                print("Whoever made these wasn't wearing standard issue astronaut boots.")
            else:
                print("You need to open the Moon Base airlock first. Don't forget to suit up.")

        # Go to Moon Rover
        elif choice in ('north', 'gonorth', 'gomoonrover', 'moonrover'):
            if airlockFlag is True:
                print("You proceed to the Moon Rover.\n")
                r10_moonRover(path)
                loopFlag = False
            else:
                print("You need to open the Moon Base airlock first. Don't forget to suit up.")

        # Go to Shuttle  
        elif choice in ('south', 'gosouth','goshuttle', 'shuttle'):
            r8_spaceShuttle(path)
            suitOnFlag = False
            loopFlag = False

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()
        
        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")
                   

def r10_moonRover(path):
    """
    Features: Apollo Rover Battery, Apollo Moon Map
    Objects: None
    
    Plot: Elon can drive around on the Moon with a Moon Rover left behind by an Apollo mision. He has
          has to connect the battery first, because it is disconnected. There in an Apollo Moon Map on
          the Rover seat, he has to open the map to see what is around. The map has a mystery location
          circled on it that he can drive to. He can also return to the Moon Base.
    """
    
    print(u"\u001b[40;1m                     .-:                                                                  \u001b[0m")
    print(u"\u001b[40;1m                      .:   ..:::::::.                                                     \u001b[0m")
    print(u"\u001b[40;1m                       .:....::::::.                                                      \u001b[0m")
    print(u"\u001b[40;1m                  ......::...::::-.                                                       \u001b[0m")
    print(u"\u001b[40;1m                 ..:.....::.::-=-                                                         \u001b[0m")
    print(u"\u001b[40;1m               ......:::::-===-.                                                          \u001b[0m")
    print(u"\u001b[40;1m              .....:::--==-++.                                                            \u001b[0m")
    print(u"\u001b[40;1m                           .--                                                            \u001b[0m")
    print(u"\u001b[40;1m                             -:.                                                          \u001b[0m")
    print(u"\u001b[40;1m                              :     :::=-.                                                \u001b[0m")
    print(u"\u001b[40;1m                              :     --=-:.                 ...                            \u001b[0m")
    print(u"\u001b[40;1m                              :   -==++=--:.   ...........::-:        .                   \u001b[0m")
    print(u"\u001b[40;1m                              ==: .*****---::  :=--===+:: ::-:.......-...                 \u001b[0m")
    print(u"\u001b[40;1m                              :..  +####+-+===.-========: -==-----+.-+-   .               \u001b[0m")
    print(u"\u001b[40;1m   :+======.                  :..  +.=***=*--:-++=======..==---------+:.  .               \u001b[0m")
    print(u"\u001b[40;1m   :-=+::....                 .. .. ==--*=**=:---=#***++++======-----+:.. .               \u001b[0m")
    print(u"\u001b[40;1m    :#=      ..                : :.-:-.:-=*#*-.:::==+****+-+#**+++==-=-::::....           \u001b[0m")
    print(u"\u001b[40;1m     *=        ..    .          ::--=--=*:+%:---=-=====-:-:-=+***#:==*+**+##=-=--:--.     \u001b[0m")
    print(u"\u001b[40;1m     :+=:.      .:::---=-       : :-===-*:+#%+**+***+=-:....:::::-+===--=--==+==#%%%%:    \u001b[0m")
    print(u"\u001b[40;1m     -=++*+---=+==---====::.   .::-+*****-+##++#%@%%#####*++=----==+==::--+:+++######*    \u001b[0m")
    print(u"\u001b[40;1m      -*==+-=*####+=+========++=-::-=++**-=*#+=**#%%%######*=-=====++=-=#*#+**%##***=#:   \u001b[0m")
    print(u"\u001b[40;1m     :++=++*+#%%%%##*+=======-:::::--==+*=-=+++++*###%%%###*==++----:---==*#*%%%#--+-#:   \u001b[0m")
    print(u"\u001b[40;1m   .:+*++=-=-===+#%%#**+===+**+-------==+==++++++++++++***+=--::         .:##@%%+=:-=#    \u001b[0m")
    print(u"\u001b[40;1m   .===-===--====+*####*##*###*=-----=***+---==+++===--::::                #@%%%=-:-#:    \u001b[0m")
    print(u"\u001b[40;1m    -====-========++=-----=+*##=======+*****+=::--::::..                   -%%%%#+*#-     \u001b[0m")
    print(u"\u001b[40;1m     +%#+===---:---=+*@*+----=*+=====+#+=+#%@@@@%+..                        -*#%%#*-      \u001b[0m")
    print(u"\u001b[40;1m      =%@@%*+===++=*##@%#*=+==++==++++=*%%%##%%%%%#.                                      \u001b[0m")
    print(u"\u001b[40;1m       .=*%%@%*=++*#%#****=====++*#+-+%%#**#%##%###+                                      \u001b[0m")
    print(u"\u001b[40;1m       :--====--::::--==++==+*#%@#*=*@%#####***+*%#*                                      \u001b[0m")
    print(u"\u001b[40;1m                         ::=*##*##*#@%%%%#=--=**=*%*                                      \u001b[0m")
    print(u"\u001b[40;1m                                :**@%%%%#---:-=*-+%+                                      \u001b[0m")
    print(u"\u001b[40;1m                                =*%@%%%#=-=+:-==-##:                                      \u001b[0m")
    print(u"\u001b[40;1m                                :+%%%%%#=-=-:--:*%+                                       \u001b[0m")
    print(u"\u001b[40;1m                                 -%%%%%#+---:::*%+                                        \u001b[0m")
    print(u"\u001b[40;1m                                  =%%%%%#*+++#%#=                                         \u001b[0m")
    print(u"\u001b[40;1m                                   :+#%%%%%%%#*=                                          \u001b[0m")
    print(u"\u001b[40;1m                                      **#**+=                                             \u001b[0m")
    print("\n")

    roomPath = r"\rooms\r10_moonRover.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r10_moonRover"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    roverBatteryConnectedFlag = False
    moonMapOpenFlag = False
    loopFlag = True
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")
        
        # Connect Apollo Rover Battery
        elif choice in ('connectbattery', 'usebattery'):
            print("You bend over and connect the dangling wire to the battery again, and the rover powers up.")
            roverBatteryConnectedFlag = True

        # Open Apollo Moon Map
        elif choice in ('openmoonmap', 'openmap'):
            print("You unfold the map.")
            print("On it you see the Moon Base location, and another location circled in red with")
            print("the word 'INCREDIBLE!!!' written over it, where the mysterious object is.")
            moonMapOpenFlag = True

        # Go East to Object
        elif choice in ('east', 'goeast', 'goobject', 'object'):
            if roverBatteryConnectedFlag is False:
                print("The rover has no power because the battery isn't connected.")
            elif moonMapOpenFlag is False:
                print("You should open the map so you can navigate safely first.")
            else:
                print("You begin driving the rover towards the object in the distance.\n")
                r11_moonPeople(path)
                loopFlag = False

       # Go to the Moon Base
        elif choice in ('north', 'gonorth', 'gomoonbase'):
            if roverBatteryConnectedFlag is False:
                print("The rover has no power because the battery isn't connected.")
            elif moonMapOpenFlag is False:
                print("You should open the map so you can navigate safely first.")
            else:
                print("You begin driving the rover towards the Moon Base.\n")
                r9_moonBase(path)
                loopFlag = False

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()
        
        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")


def r11_moonPeople(path):
    """
    Features: Doge Statue, Little Green Man
    Objects: None
    
    Plot: Elon drives the Moon Rover to the mysterious object, where he discovers it is a statue of the
    dog on a Dogecoin. If he puts a Dogecoin in the circular hole in the chest of the statue, a 3-eyed
    Little Green Man just like the one in Toy Story appears that he can talk to. When he is done he
    returns to the Moon Rover.
    """
    
    print(u"\u001b[40;1m                                    -:.                                                   \u001b[0m")
    print(u"\u001b[40;1m                                    :-:                                                   \u001b[0m")
    print(u"\u001b[40;1m                                      ..                                                  \u001b[0m")
    print(u"\u001b[40;1m                                       :                                                  \u001b[0m")
    print(u"\u001b[40;1m                                       .:                                                 \u001b[0m")
    print(u"\u001b[40;1m                                       .-.                        ::                      \u001b[0m")
    print(u"\u001b[40;1m                                       :--:::::::::...           ::=                      \u001b[0m")
    print(u"\u001b[40;1m                                  .::-----:--------::::::...    ::-=                      \u001b[0m")
    print(u"\u001b[40;1m                              .:--==-::...:---=-...  .:-::::::.::--=.                     \u001b[0m")
    print(u"\u001b[40;1m                           .:---=+=-:.-#=  .----::%#   .-:::::-:----                      \u001b[0m")
    print(u"\u001b[40;1m                .:       -=-::::====-::=:..:-----::.. ...::::::-----                      \u001b[0m")
    print(u"\u001b[40;1m                .=-     ==:::*+.====---:::---:::::::::::::::::------                      \u001b[0m")
    print(u"\u001b[40;1m                 .==:  -+=-::==-===----------::::::::::::---:--===-.         ...          \u001b[0m")
    print(u"\u001b[40;1m                   +++=++==---======----------::::::::-------===.         .:--:-.         \u001b[0m")
    print(u"\u001b[40;1m                   .**+++++++=========+*#%%%%###*+=-----=====++.         :----=:          \u001b[0m")
    print(u"\u001b[40;1m                    :**++++++++++=+*#%@@@@@@#*=-========+++++*#=     .:--::::--::::::...  \u001b[0m")
    print(u"\u001b[40;1m         -:.         -**+*++++++++++++*****++=+++++++++++**#####:-=+*+=----------=-------:\u001b[0m")
    print(u"\u001b[40;1m         ==--:        :-=******++++++++++++++++++*******##%###%#******==--------=++=---:: \u001b[0m")
    print(u"\u001b[40;1m         -+=---.         -#***********************###%%#########*#####*++===--------:.    \u001b[0m")
    print(u"\u001b[40;1m .:-----=====----=+******#%%%%%###############%%%%%###*####*+*#####%%%#=========+==---:   \u001b[0m")
    print(u"\u001b[40;1m-++==========----=++++++**#%%%%%%%%%%%%%%%%%###########*++++++*####%*-            ..:.    \u001b[0m")
    print(u"\u001b[40;1m  .::-++======--=+*******###%%%%%%%%%%%%%%%%#####*****++++++*+*###+:                      \u001b[0m")
    print(u"\u001b[40;1m  .:==========++==+**###%%%##########******************+++++++***                         \u001b[0m")
    print(u"\u001b[40;1m  =+=+==-:::::.        :-+*#####*******************##+*+++++++***-                        \u001b[0m")
    print(u"\u001b[40;1m                           #####*********************#*++*++****#*                        \u001b[0m")
    print(u"\u001b[40;1m                          .%%#####***************************##%%#                        \u001b[0m")
    print(u"\u001b[40;1m                          .%@%%%%%######%%%%%############*%%%%%%%-                        \u001b[0m")
    print(u"\u001b[40;1m                           =%@@@%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*.                        \u001b[0m")
    print(u"\u001b[40;1m                            #%%%%%%%%%%%%@%%%%%%%%%%%%####******+                         \u001b[0m")
    print(u"\u001b[40;1m                            :####################***************-                         \u001b[0m")
    print(u"\u001b[40;1m                             +%######*******#******************+                          \u001b[0m")
    print(u"\u001b[40;1m                             -%%###********######**************:                          \u001b[0m")
    print(u"\u001b[40;1m                         -#%%%@%%%%###******##%%%##*******##%%%%%#=                       \u001b[0m")
    print(u"\u001b[40;1m                       -#%%%%%%%%%%%%%#######%%%%%####%%%%%%%%%%%%%#-                     \u001b[0m")
    print(u"\u001b[40;1m                       #%%%%%%%%%%%%%%%%%%%%%##@@@@@@@@@%%%%%%*#%%%%#-                    \u001b[0m")
    print(u"\u001b[40;1m                       .=+*#######**++==-:.     .:=+*#%%%%%%%%#*%%%#+.                    \u001b[0m")
    print("\n")

    roomPath = r"\rooms\r11_moonPeople.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r11_moonPeople"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    loopFlag = True
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")
        
        # Use Dogecoin on Statue
        elif choice in ('usedogecoinonstatue', 'usedogecoin', 'statue', 'insertdogecoinintostatue'): 
            print("You place the Dogecoin in the circular hole in its chest.")
            print("Its tail starts to wag and its eyes begin to glow.")
            print("You see a bright flash of green light to your right.")
            print("You quickly turn and look.")
            print("Lo and behold, a little green man with three eyes is staring back at you.")

        # Talk to Little Green Man
        elif choice in ('talklittlegreenman', 'littlegreenman'):
            print("You greet the little green man.")
            print("'YOU HAVE BEEN CHOSEN!' he says excitedly.")
            print("'Wait, what? What does that mean?' you ask.")
            print("'YOU HAVE BEEN CHOSEN!!!' he repeats.")
            print("'I don't understand what this means!' you reply.")
            print("'YOU HAVE BEEN CHOSEN!!!!! YOU HAVE BEEN CHOSEN!!!!!'")
            print("You realize this is all that he can say, so you stop.")
            
        # Go to Moon Roover
        elif choice in ('west', 'gowest', 'gomoonrover', 'moonrover'):
            print("You head back towards the Moon Rover.\n")
            r10_moonRover(path)
            loopFlag = False

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()
        
        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")
    

def r12_marsBase(path):
    """
    Features: Mars Base Airlock, Mars Base Headquarters
    Objects: None
    
    Plot: Elon lands at the Mars Base. He can leave the Mars Base airlock and head out if he is
          wearing his spacesuit. He can explore Base Headquarters and head to the Mars Rover. 
    
    """
    
    print(u"\u001b[31m=====--------:::::::::..............:::::::::---------=============+++++++++++************\u001b[0m")
    print(u"\u001b[31m========-------:::::::::..........::::::::---------==========++++++++++++++++*************\u001b[0m")
    print(u"\u001b[31m++========-------:::::::..........::::::---------==========+++++++++++++++++++++**********\u001b[0m")
    print(u"\u001b[31m++++=======-------::::::.........:::::--------==========+++++++*****####******************\u001b[0m")
    print(u"\u001b[31m++++++======-------::::::........::::--------====+++*****#################################\u001b[0m")
    print(u"\u001b[31m+++***********++=+*=-::::..  ...::---===++***#############################################\u001b[0m")
    print(u"\u001b[31m###########******###+++==-----==+++**********##*################**********################\u001b[0m")
    print(u"\u001b[31m############****##***++++++==++++++************************************###################\u001b[0m")
    print(u"\u001b[31m#############***%*+++****++++++++*********************************########################\u001b[0m")
    print(u"\u001b[31m##########******#*==+*********#************************************#################%%%%%%\u001b[0m")
    print(u"\u001b[31m*****************+---******++*++***************########***************##############%%%%%%\u001b[0m")
    print(u"\u001b[31m#####*==########++-::##****++-:=+*****###########***+==------==+++++****########*####%%%%%\u001b[0m")
    print(u"\u001b[31m%%%%%%##%%%%%%%#==:.:##******:.=+*##%%%%%%%%%%%#=**=:----===-:-=+++****#########*#%%%%%%%%\u001b[0m")
    print(u"\u001b[31m%%%%%%%%%%%#####:-:..+***###=..:-====+*##**##%%##*##**####**##*******+=++*####%%%%%%%%%%%%\u001b[0m")
    print(u"\u001b[31m%%%%%%%#########.-. .*##############***####%%%%%%%%%####**++*##**####**##%%%%%%%%%%%%%%%%%\u001b[0m")
    print(u"\u001b[31m%%%#############.-.  *#########%%%%%%%%#####%%%%%%%%%%%%%%%%###%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[0m")
    print(u"\u001b[31m%%############%+=:.  +**#########%%%%%%%%%%##*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[0m")
    print(u"\u001b[31m############%%+ #=.  :+**#########%%%%%%%%%%%#***###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[0m")
    print(u"\u001b[31m***########%%*..#=.  .-+**#####****##%%%%%%%%%%%#***##%##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[0m")
    print(u"\u001b[31m**###########-:+%*-:--.-=+******++--=*##%%%%%#*#%%##**++*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[0m")
    print(u"\u001b[31m%%%%%%############*********#######%%%%%%%%%%%%%%%%%%%%%%%########%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[0m")
    print(u"\u001b[31m%%%%%%%%%%%%%##%%%%%%#####%%%%%%%%%%%%%%%@@@@@@@@@%%%%%%%%%%#*****++++#%@@@@%%%%%%%%%%%%%%\u001b[0m")
    print(u"\u001b[31m%%%%%%%%%%%%%%%%%%%%%%%#####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%####%#####%%%%%%%%%%%%@%%%%\u001b[0m")
    print(u"\u001b[31m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###%###*****##%%%%%%%%%\u001b[0m")
    print("\n")

    roomPath = r"\rooms\r12_marsBase.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r12_marsBase"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    loopFlag = True
    airlockFlag = False
    suitOnFlag = False
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")
        
        # Put on Space Suit
        elif choice in ('usespacesuit', 'wearspacesuit'):
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            if "spaceSuit" in inventory:
                print("You slip into your spacesuit for your Mars travels.")
                suitOnFlag = True
            else:
                print("You forgot to bring your spacesuit. I wouldn't go outside if I were you.")

        # Open Mars Base Airlock
        # You better have your Spacesuit on or it's gonna suck
        elif choice in ('openmarsbaseairlock'):
            # IF NO SUIT ON, DEATH...GAME OVER
            if suitOnFlag is False:
                print("The airlock hisses and opens.")
                print("'This is not good, I can't breath...I think I missed something important...")
                print("You quickly lose consciousness.")
                print("\n")
                print(u"\u001b[31m    @@@@@@@@@@%%%%%%%%%%%%@@@@@@%%%%%%%%%%%@@@@@%%%%@@@@@@@%%%%@@%%%%%%%%%%%%%%%%@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@%%            %%@@%%           %%@@%    %%@@@%     @@                @@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@@@@@    %@@    %@@@@@@    %@%      %%       @@%    @@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@%%%%%%%%@@@    %@@@@@@    %@%    %%   %     @@%    %%%%%%%%@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@        %@@    %@@@@@@    %@%    @@% %@%    @@%            %@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@@@@@%   %@@               %@%    @@@@@@%    @@%    @@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@     @@@@@@    %@@    %@@@@@@    %@%    @@@@@@%    @@     @@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@%          %@@@@    %@@@@@@    %@%    @@@@@@%    @@                @@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@          %@@@@%   %@@@@@@%   %@@               @@%            %@@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    %%%%%%%  %%@@    %@@@@@@    %@@%   %%%%%%%%%%%@@%    %%%%%%%  %%@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@    %@@@@@@    %@@%   @@@@@@@@@@@@@%    @@@@@@%    @@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@%%   %@@@%%   %%@@%            @@@@%    %%%%%%%   %@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@@@%    @%    @@@@@%   @@@@@@@@@@@@@%             @@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@%    @@@@@@%    @@@@@@%      @@@@@@@    %@@@@@@@@@@@@%    @@@@%    @@@@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@%           @@@@@@@@@@@  @@@@@@@@@               @@%    @@@@@@%    @@@@@@@@@\u001b[0m")
                print(u"\u001b[31m    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
                print("\n")
                exitGame()
            else:
                print("The airlock hisses and opens.")
                airlockFlag = True

        # Enter Mars Base Headquarters
        elif choice in ('entermarsbaseheadquarters'):
            if airlockFlag is True:
                print("You enter the building.")
                print("It's swarming with construction droids and looks a few days from being done,")
                print("those dilithium crystals DID get you here a little quicker!")
                print("You suddenly realize you're the first human to step inside this place.")
                print("Aren't you supposed to cut a ribbon or throw a shovel load of dirt or something?")
                print("Too bad we couldn't afford what Lucasfilms asked for to let us add R2D2 and C-3P0")
                print("to this scene, or we totally would've had them make a cameo appearance right now.")
                print("You head back outside.")
            else:
                print("You need to open the airlock first. Don't forget to suit up.")

        # Go to Shuttle
        elif choice in ('north', 'gonorth', 'goshuttle', 'shuttle'):
            print("You re-enter the Mars Base airlock and return to the Shuttle cockpit.")
            print("Barf welcomes you back as you take off your spacesuit.")
            print("You blast off back into space.\n")
            r8_spaceShuttle(path)
            suitOnFlag = False
            loopFlag = False

        # Go to Mars Rover
        elif choice in ('south', 'gosouth', 'gomarsrover', 'rover'):
            if airlockFlag is True:
                print("You proceed to the Mars Rover.\n")
                r13_marsRover(path)
                loopFlag = False
            else:
                print("You need to open the airlock first. Don't forget to suit up.")

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)
                
        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()

        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")        


def r13_marsRover(path):
    """
    Features: Mars Rover Ludicrous Mode, Mars GPS
    Objects: None
    
    Plot: Elon gets to the Mars Rover. He has to turn on the Mars Rover so the GPS can drive him
          to the Mars Pyramid or the Face of Mars. He can also use Ludicrous Mode on the Mars Rover.
          He can also take the Mars Rover back to Mars Base.
    """

    print(u"\u001b[31m                         .:::..............          ...                                  \u001b[0m")
    print(u"\u001b[31m                     .-===:--------==================+++==-.                              \u001b[0m")
    print(u"\u001b[31m                 .:===-====-------------------================:.                          \u001b[0m")
    print(u"\u001b[31m                .*+-----====--==------------===-==---===-----====-:.                      \u001b[0m")
    print(u"\u001b[31m               .+*---=--=====--==------===========---====-----=====+=-..                  \u001b[0m")
    print(u"\u001b[31m              .:---------=====---------------------==-===------=========:.                \u001b[0m")
    print(u"\u001b[31m        ------==------::::::::::-::::::::::::::::--------------------------::             \u001b[0m")
    print(u"\u001b[31m        =+++++++++++++++++++=======....:::::::::::::::------------------------+           \u001b[0m")
    print(u"\u001b[31m       ====+*+++++++++++++*******+=-:::.................................::::-=#           \u001b[0m")
    print(u"\u001b[31m        #%%##*++++++++++++%%%%%##*+-==------========+++++******************#%%%           \u001b[0m")
    print(u"\u001b[31m        *%%###*+++++++++++%%%%%###+===-----=+++++++++++*************########%%#           \u001b[0m")
    print(u"\u001b[31m        +######++++++++++*%##%%%###===-----=+++++++++++************########%%%#           \u001b[0m")
    print(u"\u001b[31m        *####%##*+**++++*%%%%%%%%%%*+++++++***********##########%%%%%%%%%%%%%%%%          \u001b[0m")
    print(u"\u001b[31m       =#####%%%########%%%%%%%%%%%%%%##############%%%%%%%%%@@@@@@@@@@@@@@@@@@%          \u001b[0m")
    print(u"\u001b[31m+++=--=+#%%###%%%%######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@%%********#\u001b[0m")
    print(u"\u001b[31m====-==+#%%###%%#*#####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@%%%%*++*#****\u001b[0m")
    print(u"\u001b[31m=======+#%%%%%%%*+=====#%%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@%%%%++++++*+*\u001b[0m")
    print(u"\u001b[31m========#%%%%%%%++*****#%%%%%%%@%%%%%%%%#%%@%%%%#+++++++++++++++%@@@@@@@@@@@%%%%*++*******\u001b[0m")
    print(u"\u001b[31m==+++++++***********####%%%%@%%%%%%%%%%%%%%%%%%%#################%@@@@@@@@@@%%%#**********\u001b[0m")
    print(u"\u001b[31m=====+++++++++++++++++++*#%%%%@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##%%%%%%%%%%%######**#****\u001b[0m")
    print(u"\u001b[31m=+++++++++++++++++++++++++++***********+++++++++++++++++*+++++++++++**********************\u001b[0m")
    print(u"\u001b[31m+=+++++++++=++==+=+=+============+=+=============+======+=++++++++++++++++++++++++********\u001b[0m")
    print("\n")

    roomPath = r"\rooms\r13_marsRover.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r13_marsRover"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    roverOnFlag = False
    ludicrousModeFlag = False
    loopFlag = True
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")
        
        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")

        # Start the Rover and use GPS
        elif choice in ('startmarsrover', 'drivemarsrover'):
            if roverOnFlag is True:
                print("The rover is already running, tell the GPS where you want to go.")
            else:
                roverOnFlag = True
                print("The rover starts up.")
                print("It looks there is enough battery power for Ludicrous Mode.")
                print("The GPS displays three locations it can take you to:")
                print("Go North to the Mars Base")
                print("Go West to the Face of Mars")
                print("Go East to the Pyramid")

        # Use Mars Ludicrous Mode
        elif choice in ('usemarsludicrousmode'):
            if ludicrousModeFlag is False:
                ludicrousModeFlag = True
                print("You are pressed into the seat as the rover quickly accelerates.")
                print("\n")
                print(u"\u001b[41;1m==========================================================================================\u001b[0m")
                print(u"\u001b[33;1m         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%\u001b[0m")
                print(u"\u001b[33;1m         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%\u001b[0m")
                print(u"\u001b[33;1m         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%\u001b[0m")
                print(u"\u001b[31m%%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         \u001b[0m")
                print(u"\u001b[31m%%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         \u001b[0m")
                print(u"\u001b[31m%%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         \u001b[0m")
                print(u"\u001b[43;1m==========================================================================================\u001b[0m")
                print(u"\u001b[31m         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%\u001b[0m")
                print(u"\u001b[31m         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%\u001b[0m")
                print(u"\u001b[31m         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%\u001b[0m")
                print(u"\u001b[33;1m%%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         \u001b[0m")
                print(u"\u001b[33;1m%%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         \u001b[0m")
                print(u"\u001b[33;1m%%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         %%%%%%%%%         \u001b[0m")
                print(u"\u001b[41;1m==========================================================================================\u001b[0m")
                print("\n")
                print("WHOAH YOU JUST WENT TO PLAID AND SET THE MARTIAN LAND SPEED RECORD!!!")
                print("You come to a screeching halt as the battery power protector kicks in.")
                print("The GPS displays three locations it can take you to:")
                print("Go North to the Mars Base")
                print("Go West to the Face of Mars")
                print("Go East to the Pyramid")
            else:
                print("You don't have enough battery power to use Ludicrous Mode again.")

        # Go to Mars Base
        elif choice in ('north', 'gonorth', 'gomarsbase', 'marsbase'):
            if roverOnFlag is False:
                print("You need to start the rover so the GPS can drive you there safely.")
            else:
                print("The rover drives toward Mars Base.\n")
                r12_marsBase(path)
                loopFlag = False

        # Go to the Face of Mars
        elif choice in ('west', 'gowest', 'gofacemars', 'facemars'):
            if roverOnFlag is False:
                print("You need to start the rover so the GPS can drive you there safely.")
            else:
                print("The rover drives toward the Face of Mars.\n")
                r14_marsFace(path)
                loopFlag = False

        # Go to the Mars Pyramid
        elif choice in ('east', 'goeast', 'gomarspyramid', 'gopyramid', 'pyramid'):
            if roverOnFlag is False:
                print("You need to start the rover so the GPS can drive you there safely.")
            else:
                print("The rover drives toward the Pyramid.\n")
                r15_marsPyramid(path)
                loopFlag = False

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)
                
        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()

        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")


def r14_marsFace(path):
    """
    Features: Face Entrance, Martian
    Objects:  Red Pill
    
    Plot: Elon arrives at the Face of Mars. Once he opens the Face Entrance, he can enter and talk
          to the Martian inside and get the Red Pill from him. If he has the Blue Pill from the Mars
          Pyramid, the Martian will tell Elon he has to either eat the Red Pill to have the truth
          revealed to him, or eat the Blue Pill to forget everything that has happened. If he eats the
          Red Pill, the Martian takes Elon to The Creator, who reveals to Elon that he is a clone, and
          the game is completed and ends. If Elon eats the Blue Pill, he blacks out and reappears back
          in his house on Earth and a new game is started.
    """

    print(u"\u001b[31m,,,,,,,,,,,,,,,,,*@#S?++;;;::::::::::,,,,,,,::,,,,,,,::::::::::;;;++?S#@*,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,+@S?*++;;;;;;;:::,,,,,,,,,,,,,,,,,,,,,,:::;;;;;;;++*?S@+,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,;#%?**+++;;;+++++;:,,,,,,,,,,,,,,,,,,:;+++++;;;+++**?%#;,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,:S%**++******??%??*;::,,,,,,,,,,,,::+*??%??******++**%S:,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,:S%*++**++;;;:::::;;;;:::,,,,,,:::;;;;:::::;;;++**++*%S:,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,;?S%*+++;;;;;;;+++;;;:;;;::,,,,::;;;:;;;+++;;;;;;;+++*%S?;,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,;?S%*+++;;++**;?%%?:;+;;+;:,,,,:;+;;+;:?%%?;**++;;+++*%S?;,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,;%%*++++++**+;;++;:;;::+;;::::;;+::;;:;++;;+**++++++*%%;,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,:?%*++;;++;;;;::::::::;;;;::::;;;;::::::::;;;;++;;++*%?:,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,+?**+;;;;;::::::::::;;;;;::::;;;;;::::::::::;;;;;+**?+,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,+*?*+;;:::::::::::::;;;;;;::;;;;;;:::::::::::::;;+*?*+,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,;??*+;;:::::::::,:::;;;+;;::;;+;;;:::,:::::::::;;+*??;,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,+?*+;;:::::::::::::;++++;::;++++;:::::::::::::;;+*?+,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,+?*+;;;:::::::::,::+;;+;::::;+;;+::,:::::::::;;;+*?+,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,;?*+;;;;:::::::,,::;;+%+::::+%+;;::,,,::::::;;;;+*?;,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,.+*++;;;;::::::,,::;;;;+;;;;+;;;;::,,::::::;;;;++*+.,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,.;*++;;;;;::::::::::::;;::::;;::::::::::::;;;;;++*;.,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,.;*++;;;;;;::::::::::::::::::::::::::::::;;;;;;++*;.,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,,,*++;;;;;;;;;;;;;;::::::::::::::;;;;;;;;;;;;;;++*,,,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,,.;*+;;;;;::;++++++++**********++++++++;::;;;;;+*;.,,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,,,,+*+;;;;:::;;;+*???**+****+**???*+;;;:::;;;;+*+,,,,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,,,.,;*++;;;:::::;;;;++;;;;;;;;++;;;;:::::;;;++*;,.,,,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,,,,..:++;;;;:::::;:::;;;;++;;;;:::;:::::;;;;++:..,,,,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,,,,,..,+%*;;;;::::;;::::;;;;;;::::;;::::;;;;*%+,..,,,,,,,,,,,,,,,,,,,,,,\u001b[0m")
    print(u"\u001b[31m,,,,,,,,,,,,,,,,,,....:+S@#%?*+;;::::::::::::::::::::::::;;+*?%#@S+:....,,,,,,,,,,,,,,,,,,\u001b[0m")
    print("\n")

    roomPath = r"\rooms\r14_marsFace.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r14_marsFace"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    loopFlag = True
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")
        
        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")

        # Open Entrance
        elif choice in ('gofaceentrance', 'openfaceentrance'):
            print("You approach the entrance.")
            print("You place your hand in the outline on the wall.\nThe entrance opens up and you step inside.")
            print("You see a Martian. He does not appear to be Marvin, though. Bummer.")

        # Talk to Martian
        elif choice in ('talkmartian'):
            inventory = getInfo(path + r"\elon\inventory.json", "objects")
            print("'Greetings Earthling', the Martian says to you.")
            print("'You have traveled far, much farther than any of your kind have before.'")
            if 'bluePill' in inventory:
                print("'I see you have found the blue pill. Very good.'")
                print("'I have a red pill for you as well.'")
                take('takeredpill', path, path + roomPath)
                print("'You have a very important decision to make now.'")
                print("'Eat the blue pill and remain ignorant...'")
                print("'Or eat the red pill to learn the ultimate truth.'")
                print("'The choice is yours to make.'")
            else:
                print("If you retrieve the blue pill from the pyramid, I will allow you to")
                print("make a very important decision when you return.")

        # Eat Red Pill
        elif choice in ('eatredpill'):
            print("'Now that you have taken the red pill, it is time to reveal the truth' the Martian says.")
            print("'The Creator approaches!' he exclaims, and points behind you.")
            print("You turn around and are utterly confused. The Creator is the spitting image of...")
            print("YOU!")
            print("'Hello Elon, it is a pleasure to finally meet you!' he says in a voice identical to yours.")
            print("'Many millenia ago we visited Earth and planted a seed in an emerald mine in a place Earthlings")
            print("refer to as Pretoria, South Africa in the hopes of creating a great civilization to rule.")
            print("'This seed hatched on June 28, 1971. Yes, you are that seed, Elon. You are a clone.'")
            print("'Just like Boba Fett, although not nearly as talented or effective or anything.'")
            print("Your mouth drops open.")
            print("'Unfortunately all Earth civilization has done during your time is get good at making memes,")
            print("invent the McRib, create invisible money that doesn't exist and launch cars into space.'")
            print("'Because of this we have pulled the plug on the experiment and you are free to evolve on your own.'")
            print("'I...I don't...I don't know what to say' you stammer awkwardly.")
            print("'That's fine, Elon, I have to go unload my Dogecoins anyway, Shiba Inu is so hot right now!!!'")
            print("The Creator and the Martian disappear in a puff of green smoke and echoing laughter.")
            print("All you can do is sigh.")
            print("Maybe you should have just stuck to selling flamethrowers?")
            print("\n")
            print(u"\u001b[44;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
            print(u"\u001b[46;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
            print(u"\u001b[42;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
            print(u"\u001b[43;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
            print(u"\u001b[41;1m@@@@---%@%---@@@-------*@@*--+@@@%---@@@@@@@@@@@@@*--+@@@%---@@@---------%*--+@@@%---@@@@@\u001b[0m")
            print(u"\u001b[41;1m@@@@...#@#...%+..-@@@#...%+..-@@@#...%@@@@@@@@@@@@+..-@@@#...%@@@@@...%@@@+....+##...%@@@@\u001b[0m")
            print(u"\u001b[41;1m@@@@*- -=- -*@+  -@@@#   %+  -@@@#   %@@@@@@@@@@@@+  -@=+#   %@@@@@.  %@@@+     .-   %@@@@\u001b[0m")
            print(u"\u001b[41;1m@@@@@@%...%@@@*..=@@@#...@*..=@@@#...@@@@@@@@@@@@@*..:::::...@@@@@@:..%@@@*..-%:.....@@@@@\u001b[0m")
            print(u"\u001b[41;1m@@@@@@@. .@@@@#= :***= :=@#= :***= :=@@@@@@@@@@@@@+  :=%*-  .%@@***...+**@+  -@@*-  .%@@@@\u001b[0m")
            print(u"\u001b[43;1m@@@@@@@###@@@@@@#######%@@@@#######%@@@@@@@@@@@@@@%##%@@@@###@@@#########@%##%@@@@###@@@@@\u001b[0m")
            print(u"\u001b[42;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
            print(u"\u001b[46;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
            print(u"\u001b[44;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[0m")
            print("\n")
            # Then the game ends
            exitGame()

        # Eat Blue Pill
        elif choice in ('eatbluebill'):
            print("You eat the blue pill. Your body tingles and the Martian quickly starts to fade away...")
            print("'Where am I?', you wonder...")
            newGame()
              
        # Go to the Mars Rover
        elif choice in ('goeast', 'gomarsrover', 'gorover', 'marsrover', 'rover'):
            print("You head back to the Mars Rover.\n")
            r13_marsRover(path)
            loopFlag = False

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)
            
        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()

        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")
            

def r15_marsPyramid(path):
    """
    Features: Pyramid Entrance Tape Player, Pyramid Entrance, Altar
    Objects: Blue Pill
    
    Plot: Elon arrives at the Mars Pyramid. He goes to the locked Pyramid Entrance, but if
          he puts the Mixtape into the slot next to the door it will unlock and open. Once
          inside the Mars Pyramid he discovers an Altar with the Blue Pill on it, which he
          can take. He will need this to complete the Face of Mars encounter. He then heads
          back to the Mars Rover.
    """

    print(u"\u001b[31m                                           .:.                                            \u001b[0m")
    print(u"\u001b[31m                                         :++==-                                           \u001b[0m")
    print(u"\u001b[31m                                       .+**+--++:                                         \u001b[0m")
    print(u"\u001b[31m                                     .=###++-=++==:                                       \u001b[0m")
    print(u"\u001b[31m                                   :+**+***=-=====---                                     \u001b[0m")
    print(u"\u001b[31m                                 .+#*##****+-+++===+*+:                                   \u001b[0m")
    print(u"\u001b[31m                               :*########%%###**++******-                                 \u001b[0m")
    print(u"\u001b[31m                             -***##########++++++++++++***-                               \u001b[0m")
    print(u"\u001b[31m:::::::::::::::::::::::::::=*****########**+++++++++++++++++-:........:..::...............\u001b[0m")
    print(u"\u001b[31m-:==-::::::::::::::::::::+*****#######****+=++++++++++++++++++=-:-:-----------------------\u001b[0m")
    print(u"\u001b[31m=-::::::::::::::::::::-+******############=++++++++++++++*+++++=-:::::::::::-:::::::------\u001b[0m")
    print(u"\u001b[31m--------------------=*###***############%*+=++++==++++++++++++==++------------------------\u001b[0m")
    print(u"\u001b[31m------------------=*#####**######%%#####%%++++++++++*++++++++++=+++*=---------------------\u001b[0m")
    print(u"\u001b[31m--------=-------=*#########%%%##%#######%*****+++*++*****+**+*++******+-------------------\u001b[0m")
    print(u"\u001b[31m--------------+*###########%############%*****+**++++**+******+++******#=-----------------\u001b[0m")
    print(u"\u001b[31m=======-----+#%%#######%%%#############%#****++++***********##*********###+----------:----\u001b[0m")
    print(u"\u001b[31m++++=====+#%%%%%%####%%%############%%%%#******++*******#*******###*****#*##*=-----=------\u001b[0m")
    print(u"\u001b[31m--:::::-*%%%%#%#%##%###%##%##########%%%#*##**********************************+=--======-=\u001b[0m")
    print(u"\u001b[31m-----:+%%%%%%%##%%####################%%#********++*********+*****###*++********-:::------\u001b[0m")
    print(u"\u001b[31m.:.-*%%%%%#####%%##%%%##%############%%##***#*********#************##*********+***+::::-::\u001b[0m")
    print(u"\u001b[31m:-*%%%%%%%###%#####%%%%%%%%%#%######%%%##***********************##*####+**********##+-::::\u001b[0m")
    print(u"\u001b[31m*####%#%##%######%%%%###%%%###%###%%%@%##****************#****##****#**#*************#=-.:\u001b[0m")
    print(u"\u001b[31m********##########%%#%###%##%%%%##%%%%##*******#****#***#*********************++*+++++++=:\u001b[0m")
    print(u"\u001b[31m****#*********#**#########%##%####%%%%%#*+******#*#******++++*++++++++=++++=-=-=-:.:::::::\u001b[0m")
    print(u"\u001b[31m*******************##**############%%%#**+*++*****+**=-====----:::--:--::::::--=-:::::::::\u001b[0m")
    print("\n")

    roomPath = r"\rooms\r15_marsPyramid.json"
    objectPath = r"\objects"
    rooms(path, roomPath)  # displays room name, checks visited flag, and displays long or short message.
    
    # update current room in elon.json
    currentRoom = r"r15_marsPyramid"
    charRoomPath = r"\elon"
    updateCurrentRoom(path + charRoomPath, currentRoom)
    
    # Create text parser instance
    textparser = TextParser()

    entranceOpenFlag = False
    loopFlag = True
    while loopFlag == True:
        
        # Input variable created, text color set to green and input prompt displayed
        choice = textparser.commandParser("\n\u001b[32m>>> ")
        # Text color set back to white
        print("\u001b[37m")

        # If no command entered, display prompt for a command
        if choice in (''):
            print("You didn't say anything, please give me a command.")
        
        # Insert mixtape to unlock the entrance
        elif choice in ('putmixtapeintoslot', 'insertmixtapeintoslot', 'usemixtapeondoor'):
            if entranceOpenFlag is False:
                entranceOpenFlag = True
                print("You insert the mixtape into the slot and those fiery jams seem to unlock the door.")
                print("You enter the pyramid.")
                print("Weird music is playing but you don't know from where it comes.")
                print("In the middle of the chamber you see an ancient altar.")
                print("You see a small blue object floating just over it, illuminated by a spotlight.")
            else:
                print("The entrance is already open and the slot has mysteriously vanished.")

        # Open Pyramid entrance
        elif choice in ('pushdoor', 'opendoor' , 'pushentrancedoor', 'openentrance'):
            if entranceOpenFlag is False:
                print("You push on the heavy stone door but it won't budge.")
                print("You see a slot about the size of a cassette tape next to it.")
            else:
                print("You push on the heavy stone door and it slides open.")
     
        # Go to the Mars Rover
        elif choice in ('gowest', 'gomarsrover', 'gorover', 'marsrover', 'rover'):
            print("You walk back towards the rover.\n")
            r13_marsRover(path)
            loopFlag = False

        # Take
        elif (choice.startswith('take')) is True:
            take(choice, path, path + roomPath)

        # Drop
        elif (choice.startswith('drop')) is True:
            drop(choice, path, path + roomPath)

        # Look at
        elif (choice.startswith('lookat')) is True:
            lookat(choice, path)

        # Help
        elif choice in ('help'):
            help()

        # Inventory
        elif choice in ('inventory'):
            showInventory(path)

        # Look
        elif choice in ('look'):
            look(path + roomPath)

        # Load game
        elif choice in ('loadgame'):
            loadGame()

        # Save game
        elif choice in ('savegame'):
            saveGame(path)

        # Quit game
        elif choice in ('quit'):
            exitGame()

        # If unrecognized command is entered
        else:
            print("I don't understand your command, can you rephrase it?")


if __name__ == "__main__":
    # Play Elon Go To Mars!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    playGame()
