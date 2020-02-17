#!/usr/bin/python3
import sqlite3
import filecmp
import os
import subprocess

os.system("python3 manage.py makemigrations CarSalon_App")
os.system("python3 manage.py migrate CarSalon_App")
os.system("python3 manage.py makemigrations")
os.system("python3 manage.py migrate")
os.system("python3 manage.py loaddata data")
os.system("python3 manage.py runserver")



