#!/usr/bin/python3


# Script Name: Signature-based Malware Detection Pt. 2 of 3
# Author: Shay Crane
# Date of last revision: 11/15/2022
# Purpose: continue development of your own basic antivirus tool in Python.
#               by generating a given file's hash. 

from sys import platform
import os
from os.path import join
import hashlib




# Define functions:

# Determines OS and then runs the associated function:
def lookupfile():

    print("Checking OS...")
    print(platform)
    if platform=="Linux":
       linuxsearch()
    elif platform=="Windows":
       print("The OS is: ")
       print(platform)
       windowssearch()
    else:
       choice=input("Cannot detect OS.\nEnter 1 for any Linux distribution:\nEnter 2 for any Windows version:\nOr to exit, enter 3: ")
       if choice=="1":
           linuxsearch()
       elif choice=="2":
           windowssearch()
       else:
           print("Exiting...")
           quit


# Linux search
def linuxsearch():
   filename=input("File Search...\nEnter name of file:  ")
   filepath=input("Enter the file path in which to search for ")
   fileschecked=0
   for root, dirs, files in os.walk(filepath):
       for file in files:
           fileschecked+=1
           if file==filename:
               print(str(fileschecked)+" files were searched, and your file was located at: "+root+"/"+filename)
               print("Raven is the BEST.")


# Windows search
def windowssearch():
   filename=input("File Search...\nEnter name of file:  ")
   filepath=input("Enter the file path in which to search for ")
   fileschecked=0
   for root, dirs, files in os.walk(filepath):
       for file in files:
           fileschecked+=1
           if file==filename:
               print(str(fileschecked)+" files were searched, and your file was located at: "+root+"/"+filename)
               print("Raven is the BEST.")

# timestamp function
def timestamp():


# hashing function
def hashfile(filename):
    h=hashlib.sha256()
    with open(filename, 'rb') as file:
        block=0
        while block !=b'':
            block=file.read(1024)
            h.update(block)
            print(h)

    return h.hexdigest()

# substitute the file name as the parameter
message=hash_file("test.txt")
print(message)



# Main
lookupfile()



# Requirements
# Continue developing your Python malware detection tool.

# Alter your search code to recursively scan each file and folder 
#              in the user input directory path and print it to the screen.
#
#   For each file scanned within the scope of your search directory:
#       Generate the file’s MD5 hash using Hashlib.
#       Assign the MD5 hash to a variable.
#       Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.
#   
# TIP: You may need to bring in additional Python modules to complete today’s objective.

# The script should be tested to execute successfully in Python3.

