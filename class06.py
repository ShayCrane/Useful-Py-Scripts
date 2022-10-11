# !/usr/bin/python3


# Script Name: Encrypt a File
# Author: Shay Crane
# Date of last revision: 10/10/2022
# Purpose: a Python script that encrypts a single file

# This script is not complete

# import libraries
from cryptography.fernet import Fernet

from os.path import exists

# Declare Variables
user_choice="y"
key_exists=exists(key_file_path)

file_exists = os.path.exists('key.key')


# define function to generate key
def write_key(): 
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file.write(key)

# define function to load key
def load_key(): 
    return open("key.key", "rb").read()


def ask_user(): # define function
# a menu for user input
# that will run in the next While loop
print("Choose from the following options: ")
print("1. encrypt file  2. decrypt file  3. encrypt a message  4. decrypt a message  - Type n to exit")
chosen = input(int("Enter number corresponding to chosen option: ")) # declare variable from user input

        
    def encrypt_file(): #1 define function
    # ask user for file path input
    # encrypt file contents
    # show msg that it completed OR print contens of file
    
     def decrypt_file(): #2 define function
    # ask user for msg input
    # decrypts the msg
    # prints msg to screen
   
    def encrypt_message(): #3 define function
    # ask user for msg input
    # encrypts the msg
    # prints msg to screen
    
    def decrypt_message(): #4 define function
    # ask user for msg input
    # decrypts the msg
    # prints msg to screen
    
    # n = exit
    if option = n 
    then exit 

# reads status from "key_exists"


# call function
key = load_key()
print("Key is " + str(key.decode('utf-8')))

message = "This message will self-destruct in 10 seconds.  10... 9...".encode()
print("Plaintext is " + str(message.decode('utf-8')))
write_key() # call function;  generates a key, saves it to a file
    # each option produces a key in a variable
    # feed the variable to the While loop


    # While loop reads key variable
While True
ask_user() 
While chosen 
decrypt_message()
encrypt_file()
else decrypt_file()
encrypt_message()

