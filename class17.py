#!/usr/bin/python3


# Script Name: Automated Brute Force Wordlist Tool Pt. 2
# Author: Shay Crane
# Date of last revision: 10/24/2022
# Purpose:  continue the development of a custom tool that performs
#           brute force attacks to better understand the types of
#           automation employed by malicious hackers. 



#import libraries
import time
import getpass
import sys
from tkinter.messagebox import YES
from pexpect import pxssh


#define functions
#print menu
def menu():
    print("For Offensive, Dictionary Iterator, enter 1.")
    print("For Defensive, Password Recognition, enter 2.")
    print("To exit, enter 9.")
    choice=input("Enter your choice: ")

    if choice=="1":
        iterator()
    elif choice=="2":
        password_check()
    else: 
        sys.exit 


#ssh on remote server
def sshtoremote():
    session=pxssh.pxssh()
    host=input("Provide an IP address: ")
    username=input("Provide a username: ")
    pwd=getpass.getpass(prompt='Enter a password: ')
    try:
        session.login(host,username,pwd)
        session.sendline('uptime')
        session.prompt()
        print(session.before) #prints everything before the prompt
        session.sendline('whoami')
        session.prompt()
        print(session.before)
        session.logout()
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)
#       if success==0:
        searchfile()

#search file for user input string
def searchfile():
    path=input("Enter your dictionary's filepath:\n")
    file=open(path)
    line=file.readline()
    while line:
        line=line.rstrip()
        word=line
        print(word)
        time.sleep(1)
        line=file.readline()
    file.close()

#iterator
def iterator():
    sshtoremote()

    searchfile()
    menu()


#password check
def password_check():
    pwrd=getpass.getpass("Enter your password or string: ", stream=None)
    filetwo=input("Enter the file path location of your wordlist: ")
#thanks to https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/ 
#for providing an example to work from for this next part of my script: 
    with open(filetwo) as filetwo:
        content=filetwo.read()
        if pwrd in content:
            print("Your password has been found in your wordlist.")
        else: 
            print("{pwrd} was not found in your wordlist")
            menu()

#main
#call menu function
menu()