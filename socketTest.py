# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:00:38 2021
This is a client
@author: xngu0004
"""

import socket
from time import sleep

def sendRandomColors(HOST, PORT, data):
    s = socket.socket()          
              
    # connect to the server on local computer 
    s.connect((HOST, PORT))
    s.send((
        str(data) + ","+ 
        str(255-data) + ","+ 
        str(data) + ","+ 
        str(255-data)).encode())
    s.close()

if __name__ == "__main__":
    HOST, PORT = socket.gethostname(), 11000
    
    for i in range(255):
        if(i % 10 == 0):
            sendRandomColors(HOST, PORT, i)
            sleep(1)
