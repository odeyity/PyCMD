import os

# Declare initial variables
filePath = ""
newDir = os.getcwd()
debug = False
print("Microsoft Windows [Version 10.0.19043.928]")
print("(c) Microsoft Corporation. All rights reserved.")
print()
while True:
    if filePath == "":
        command = input(os.path.normpath(os.getcwd() + "\\" + filePath) + ">")
    else:
        command = input(os.path.normpath(filePath) + ">")
    if debug == True:
        print("Command:", command)
        print("Supposed path?", os.getcwd() + "\\" + str(command).split(" ", -1)[-1])
    runCommand = "cmd /c " + command
    os.system(runCommand)

   # CD COMMAND
    
    if "cd" in command:
        if filePath == "":
            listdir = os.getcwd()
        else:
            listdir = filePath
        
        if ".." in command:
            if os.path.split(filePath)[len(os.path.split(filePath)) - 2] != os.getcwd():
                newDir = os.path.split(filePath)[len(os.path.split(filePath)) - 2]
            else:
                newDir = ""
        elif str(command).split(" ", -1)[-1] in os.listdir(listdir):
            oldDir = newDir
            if filePath == "":  
                newDir = oldDir + str(command).split(" ", 1)[1]
            else:
                newDir = str(command).split(" ", 1)[1]
        else:
            print("This directory does not exist.")
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
        filePath = os.getcwd()

# DEBUG COMMAND
    if "debug" in command:
        print("Debug mode enabled.")
        debug = True

    
 
    
    
