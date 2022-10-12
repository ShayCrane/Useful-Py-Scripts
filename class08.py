#!/usr/bin/python3


# Script Name: Add a Note
# Author: Shay Crane
# Date of last revision: 10/12/2022
# Purpose: an exercise to simulate a ransomware attack: 
#          - a final update to the class06.py script
#          - that adds an option giving us the ability to add a ransomware note 
#          - that is visible to the Windows user, after the data is encrypted.

# Requirements
# Add a feature capability to your Python encryption tool to:

    # Optional if possible: Alter the desktop wallpaper on a Windows PC with a ransomware message
    # Create a popup window on a Windows PC with a ransomware message

# Make this feature optional. In the user menu prompt, add this as a ransomware simulation option.

# Stretch Goals (Optional Objectives)
# Add additional features that draw the computer user’s attention to the ransomware message.


# redefine ask_user() function (class06.py) to include more options

# install pyautogui library
import pyautogui
import sys

# define ransom-note function
def ransom_note():
    pyautogui.password('You have been hacked!\nEnter passkey to get your files back\nCancel to lose all your files forever', 'Hack Announcement Service', 'Submit Passkey')

# define user_choice function to demonstrate 
# how ransom_note function fits into the larger script
def ask_user():
    user_choice = input('pretend all the options from previous scripts are also here\n Enter 10 to simulate ransomware attack: ')
    
    if (user_choice == '10'): 
        ransom_note()
    else: 
        sys.exit()

# Main
# invoke the ask_user function
ask_user()

