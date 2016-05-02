#!/usr/bin/python3.4

import sys
import os

if len(sys.argv) < 2:
    print("Please give a mode (show, create, add, remove)")
    sys.exit(0)

def getLists():
    file = open("Lists.lst", "r")
    lists =  [x.rstrip("\n") for x in file]
    return lists

def printIndexed(list):
    counter = 0
    for x in list:
        counter += 1
        print(str(counter) + ":", x.rstrip("\n"))

mode = sys.argv[1]

if mode == "create":
    name = input("New list name: ")
    file = open(name + ".lst", "w")
    file.close()
    file = open("Lists.lst", "a")
    file.write(name + "\n")
    file.close()
    
elif mode == "show":
    if len(sys.argv) < 3:
        printIndexed(getLists())
    else:
        name = sys.argv[2]
        file = open(name + ".lst", "r")
        printIndexed(file)
elif mode == "add":
    if len(sys.argv) < 4:
        print("usage: noteur add <name> <data>")
        sys.exit(0)
    name = sys.argv[2]
    data = " ".join(sys.argv[3:])
    file = open(name + ".lst", "a")
    file.write(data + "\n")
    file.close()
elif mode == "remove":
    if len(sys.argv) < 3:
        print("Usage: noteur remove <list> id")
        sys.exit(0)
    elif len(sys.argv) < 4:
        name = sys.argv[2]
        if input("Confirm removal of " + name + " by typing 'Confirm': ") == "Confirm":
           os.remove(name + ".lst")
           print("Removed")
        else:
           print("Aborted")
    elif len(sys.argv) < 5:
        name = sys.argv[2]
        id = int(sys.argv[3]) - 1
        file = open(name + ".lst", "r")
        content = [x for x in file]
        if input("Confirm removal of '" + content[id]  + "' from " + name + " by typing 'Confirm': ") == "Confirm":
            file.close()
            file = open(name + ".lst", "w")
            del content[id]
            for x in content:
                file.write(x)
            file.close()
            print("Removed")
        else:
            print("Aborted")

        
