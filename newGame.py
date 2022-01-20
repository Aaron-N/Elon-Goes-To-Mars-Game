import os
import shutil
from game import *

def createDirectory():
    """
    This function creates a new directory, "tempUserData"
    It then copies base game json files into this directory.

    Returns:
        "path" Holds path for current userdata json objects.
    """

    try:
        # make temp new user directory
        # New directory name
        directory = "tempUserData"  # profile is stored as temp data until saved or overwritted with new game.

        # directory path
        parent_dir = "elon_goes_to_mars_game\TextAdventureGame\saved_games"
        
        # path
        path = os.path.join(parent_dir, directory)
        
        # create the directory
        os.mkdir(path)
        # print("--Message for Testing-- Directory '% s' created" % directory)
    
    except OSError:  # if tempUserData already exists from old start, overwrite with new files
        copyFiles()  # overwrite existing files

    copyFiles()  # copy files if no exception occurs


def copyFiles():
    """
    copies game_json_files to tempUserDirectory
    """
    # copy game json files to new temp directory
    root_src_dir = r"game_json_files"  # source
    root_dst_dir = r"saved_games\tempUserData"  # destination

    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_dir)
            

def activePath():
    """
    return tempUserData as the active
    """    
    path = r"saved_games\tempUserData"
    return path



createDirectory()
