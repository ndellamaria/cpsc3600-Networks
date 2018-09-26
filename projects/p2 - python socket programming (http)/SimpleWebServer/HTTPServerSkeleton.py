# Student name: Natalie DellaMaria
# CID: C15251277

#import socket module
from socket import *
import os               # To read the last modified time
import datetime         # To format the last modified time
import sys              # In order to terminate the program

# Prepare a sever socket
# Complete this code
serverPort = 90
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)

        # Find the filename of the requested file
        filename = message.split()[1]
       
        # Open and read the file
        f = open(filename[1:])
        outputdata = f.read()

        # Find the date the file was last modified
        statbuf = os.stat(filename[1:])
        last_modified = datetime.datetime.fromtimestamp(
            int(statbuf.st_mtime)
        ).strftime("%A, %d %b %Y %p") #Complete this code

        #Send one HTTP header line into socket
        # Complete this code
        connectionSocket.send(("HTTP/1.1 200 OK Last Modified: 7\r\n\r\n").encode('utf-8'))
        #connectionSocket.send(("Last Modified: {}\r\n".format(last_modified)).encode('utf-8'))

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('utf-8'))
        connectionSocket.send("\r\n".encode('utf-8'))

        # Close client socket
        #Complete this code
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Complete this code
        connectionSocket.send(("HTTP/1.0 404 Not Found\r\n\r\n").encode('utf-8'))

        #Close client socket
        connectionSocket.close()
        #Complete this code
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data