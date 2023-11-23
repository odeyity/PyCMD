import os

# Declare initial variables
filePath = ""
drive = "H:/"
newDir = drive
debug = False
listdir = drive
print("Microsoft Windows [Version 10.0.19043.928]")
print("(c) Microsoft Corporation. All rights reserved.")
print()
while True:
    if filePath == "":
        command = input(os.path.normpath(drive + "\\" + filePath) + ">")
    else:
        command = input(os.path.normpath(filePath) + ">")
    if debug == True:
        print("Command:", command)
        print("Supposed path?", drive + "\\" + str(command).split(" ", -1)[-1])

# CD SYSTEM COMMAND
    if "start" in command:
        runCommand = "cmd /c " + os.path.normpath(filePath + "\\" + command.split(" ", -1)[1])
    else:
        runCommand = "cmd /c " + command

# RUNS SYSTEM COMMAND
    if debug == True:
        print(runCommand)
    os.system(runCommand)

# CD COMMAND
    if "cd" in command:
        if filePath == "":
            listdir = drive
        else:
            listdir = filePath
        
        if ".." in command:
            if os.path.split(filePath)[len(os.path.split(filePath)) - 2] != drive:
                newDir = os.path.split(filePath)[len(os.path.split(filePath)) - 2]
            else:
                newDir = ""
            filePath = newDir
            

        elif os.path.exists(os.path.normpath(listdir + "\\" + str(command).split(" ", -1)[-1])) == True:
            oldDir = newDir
            if filePath == "":  
                newDir = oldDir + str(command).split(" ", 1)[1]
            else:
                newDir = str(command).split(" ", 1)[1]
        if ".." not in command:
            if debug == True:
                print("Old filepath:", filePath)
            filePath = os.path.normpath(filePath + "\\" + newDir)
            first_char = filePath[0]
            if filePath[0] == os.path.normpath("\\"):
                filePath = filePath.lstrip(first_char)
            if debug == True:
                print("New dir:", newDir)
                print("New filepath", filePath)
        else:
            print("This directory does not exist.")



    elif filePath == "":
        filePath = drive

# DEBUG COMMAND
    if "debug" in command:
        print("-----------------------------------------")
        print("'debug' is recognised as a PyCMD command.")
        print("-----------------------------------------")
        print("PyCMD> Debug mode enabled.")
        debug = True

# LIST DIRECTORY COMMAND
    if "listdir" in command:
        print("-------------------------------------------")
        print("'listdir' is recognised as a PyCMD command.")
        print("-------------------------------------------")
        print(os.listdir(filePath))

# CHANGE DRIVE COMMAND
    if "drive" in command:
        if os.path.exists(os.path.normpath(command.split(" ", -1)[1].upper())) == True:
            if debug == True:
                print("Drive", os.path.normpath(command.split(" ", -1)[1].upper()),  "exists.")
            drive = os.path.normpath(command.split(" ", -1)[1].upper() + "\\")
            filePath = ""
        else:
            print("Drive", os.path.normpath(command.split(" ", -1)[1].upper())  , "does not exist.")


# DOCS COMMAND
    if "docs" in command or "ccmds" in command:
        print("---------------------")
        print("PyCMD Custom Commands")
        print("---------------------")
        print()
        print()
        print("        Debug         |  Prints out verbose text on commands          |  debug")
        print("    List Directory    |  Lists the files in the current dir           |  listdir")
        print("     Change Drive     |  Changes the drive (WIP)                      |  drive [Volume Letter]")
        print(" Custom Commands/Help |  Shows documentation for custom cmds or help  |  ccmds")
        print("                                                                      |  docs")
    

    
 
    
    
