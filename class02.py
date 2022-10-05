#!/usr/bin/python3


# Script Name: Psutil
# Author: Shay Crane
# Date of last revision: 09/14/2022
# Purpose: a Python script that creates an uptime sensor tool and uses ICMP packets to evaluate if hosts on the LAN are up or down.

# The script must:

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
# For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

# I found some helpful advice at the following link:  
# https://stackoverflow.com/questions/26468640/python-function-to-test-ping

# from pythonping import ping 

# importing libraries
import datetime
import time 
import os



# defining function
def check_ping():
    print(os.system('ping -c 1 10.0.0.227 '))
    ping_status = 0
# infinite while loop
while True:
    check_ping()
    print("Current date and time: ")
    now = datetime.datetime.now()
    print(str((now)))
    print("Start : %s" % time.ctime()) 
    time.sleep(2)
    print("End : %s" % time.ctime())
       

