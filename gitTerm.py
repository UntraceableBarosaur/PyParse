import os
import sys


username   =  "UntraceableBarosaur"
password   =   str(input("Input password UntraceableBarosaur"))


branch      =   "UntraceableBarosaur/PyParse.git"
changedFilePath  = "gitTerm.py"

clone       =   "git clone https://github.com/"+branch
clonePath   =   "/Users/Owen/Desktop"

pushpullPath     =   "/Users/Owen/Desktop/PyParse"
pull        =   "git pull https://github.com/"+branch
add         =   "git add ."
commit      =   "git commit -m" + changedFilePath
push        =   "git push --all https://github.com/"+branch

def gitPull():
    os.chdir(pushpullPath) # Specifying the path where the cloned project has to be copied
    try:
        os.system(pull) # Pulling
    except RuntimeError:
        print("Pulling Failed")
    print("Pulling Successful")

def gitClone():
    os.chdir(clonePath) # Specifying the path where the cloned project has to be copied
    try:
        os.system(clone) # Cloning
    except RuntimeError:
        print("Cloning Failed")
    print("Cloning Successful")

def gitPush():
    os.chdir(pushpullPath) # Specifying the path where the cloned project has to be copied
    try:
        os.system(add) # Adding
    except RuntimeError:
        print("Adding Failed")
    try:
        os.system(commit) # Commit the files
    except RuntimeError:
        print("Commiting Failed")
    try:
        os.system(push) # Pushing
    except RuntimeError:
        print("Pushing Failed")
    print("Pushing Successful")


gitPush()
