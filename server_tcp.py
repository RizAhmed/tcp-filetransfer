#------------------------------------------------------------------------------
# SOURCE: server_tcp.py
# 
# PROGRAM: COMP 7005 TCP File Transfer Server
#
# FUNCTIONS: Python Socket Package
# DATE: October 4, 2015
#
# DESIGNER: Rizwan Ahmed
# PROGRAMMER: Rizwan Ahmed
#
# NOTES:
#  
# This is the server-side implementation of the assignment. This module will
# accept connections from clients, receive commands, and handle any file
# transfers.
#------------------------------------------------------------------------------
import socket
import sys
import os.path
import operator

serverPort = 7005
#create socket object for server
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort)) #socket is bound to localhost and port 7005

serverSocket.listen(2) #accepting up to 2 incoming connections

print ('Server listening...')
print (socket.gethostbyname(socket.gethostname()))

while True:

    #return value of accept() is assigned to socket object
    #and address bound to that socket
    connectionSocket, addr = serverSocket.accept()
    
    #connection established with client
    print ('Got connection from', addr)

    #waiting for GET or SEND command from client
    print ('Awaiting command from client...')
    client_request = connectionSocket.recv(1024)
    #convert from byte object so we can read as string
    request_str = client_request.decode("utf-8")


    #server receives GET command from client and reads from file to be sent back
    #to client after they input the filename
    if request_str == 'GET':
        print('Received GET command from client. Waiting for filename.')

        client_request = connectionSocket.recv(1024)        


        file_name = client_request.decode("utf-8")

        f = open(file_name, "rb")
        print('Sending file...')
        l = f.read(1024)
        while(l):
            connectionSocket.send(l)
            l = f.read(1024)
        f.close()
        print('Done sending')

    #server receives SEND command from client and creates file to be received
    #by the client
    elif request_str == 'SEND':
        print('Received SEND command from client. Awaitng filename')
        client_request = connectionSocket.recv(1024)
        file_name = client_request.decode("utf-8")

        f = open(file_name, "wb")
        print('Receiving file from client..')
        l = connectionSocket.recv(1024)
        while(l):
            f.write(l)
            l = connectionSocket.recv(1024)
        f.close()
        print('Done receiving file')

    connectionSocket.close()