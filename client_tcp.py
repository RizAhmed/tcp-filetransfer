#------------------------------------------------------------------------------
# SOURCE: client_tcp.py
# 
# PROGRAM: COMP 7005 TCP File Transfer Client 
#
# FUNCTIONS: Python Socket Package
# DATE: October 4, 2015
#
# DESIGNER: Rizwan Ahmed
# PROGRAMMER: Rizwan Ahmed
#
# NOTES:
#  
# This is the client-side implementation of the assignment. This module will
# connect to a user-specified server, send commands, and handle any file
# transfers
#------------------------------------------------------------------------------
import socket
import sys

#hardcoded before moving on to user input ignore this
# serverName = 'localhost'
# serverPort = 7000

serverName = input('Enter server IP: ')
serverPort = int(input('Enter port number: '))


#in this loop, sockets open and close for each request the client makes
while True:

    #create socket object for client
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clientSocket.connect((serverName,serverPort))
    print('Connected to server.')

    sentence = input('Enter a GET or SEND command:')

    clientSocket.send(sentence.encode('utf-8'))

    fileName = input('\nEnter name of file: ')

    clientSocket.send(fileName.encode('utf-8'))
    if sentence == 'GET':
        f = open(fileName, "wb")
        print('Receiving file..')
        l = clientSocket.recv(1024)
        while (l):
            f.write(l)
            l = clientSocket.recv(1024)
        f.close()
        print('Done receiving file')

    elif sentence == 'SEND':
        f = open(fileName,"rb")

        print('Sending file to server...')
        l = f.read(1024)
        while (l):
            clientSocket.send(l)
            l = f.read(1024)
        f.close()
        print('Done sending')

    clientSocket.close()
