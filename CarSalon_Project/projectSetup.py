#!/usr/bin/python3
import sqlite3
import filecmp
import os
import subprocess

os.system("python3 manage.py makemigrations")
os.system("python3 manage.py migrate")
os.system("python3 manage.py loaddata data")
os.system("python3 manage.py runserver")


# commandsToExecute =(["python3","manage.py","makemigrations"],["python3","manage.py","migrate"],["python3","manage.py","loaddata data"],["python3","manage.py","runserver"])

# # Command sended to console
# for commandToExecute in commandsToExecute:
    
#     process = subprocess.Popen(commandToExecute)
    

    
    