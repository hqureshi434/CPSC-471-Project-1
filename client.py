import os, sys, socket

headerSize = 10
serverFolder = "./serverFiles/"
clientFolder = "./clientFiles/"
commands = ["get", "put", "ls", "quit"]










"""
#Pseudocode (with changes) from the assignment PDF for the client
#Client code
#from socket import *
#Name and port number of the server to
#which want to connect.
#serverName = ecs.fullerton.edu
#serverPort = 12000

#Create a socket
#clientSocket = socket(AF INET, SOCK STREAM) 11
#Connect to the server
#clientSocket.connect((serverName, serverPort)) 14

#A string we want to send to the server
#data = "Hello world! This is a very long string.�

#bytes Sent = 0

#Keep sending bytes until a l l bytes are sent
# while bytes Sent != len(data) :
#	Send that string!
#	bytes Sent += clientSocket.send(data[bytes Sent : ]) 24
#	Close the socket
#	 clientSocket.close()

