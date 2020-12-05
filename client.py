import os, sys, socket
from dataFun import send_data, receive_data, adjustSize, get_data_serv

#used in client 
headerSize = 10
serverFolder = "./serverFiles/"
clientFolder = "./clientFiles/"
commands = ["get", "put", "ls", "quit"]

#Connect to the port in the header
def connect(address, port):
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.connect((address, port))
        print("Connected to " + address + " on port " + str(port))
    except Exception as e:
        print(e)
        return None
    return serverSocket

def put_file(sock, address, fileName):
    # grab files only from client folder
    filePath = const.CLIENT_FOLDER + fileName

    # open file and get file size
    try:
        userFile = open(filePath, "r")
        fileSize = os.path.getsize(filePath)
    except Exception as e:
        print(e)
        # print("Failed to open file")
        return

    # get data channel port number from server
    dataPort = receive_data(sock, const.HEADER_SIZE)

    # connect to new port
    dataSocket = connect(address, int(dataPort))

    # if connection failed, exit
    if not dataSocket:
        print("Failed to connect to server")
        return
    
    # make file size and file name headers
    fileNameSize = size_padding(len(fileName), const.HEADER_SIZE)
    fileDataSize = size_padding(fileSize, const.HEADER_SIZE)
    fileData = userFile.read()
    
    # add headers to payload
    data = fileNameSize + fileDataSize + fileName + fileData

    # send data
    send_data(dataSocket, data)
    print(fileName + " upload successful.")
    print("Bytes sent: " + str(len(data)))

    # close file and connection
    userFile.close()
    dataSocket.close()
    print("Data transfer connection closed")


def run(args):
    # To run: python3 cli.py <SERVER> <PORT>
    if len(args) != 3:
        print("Usage: python3 " + args[0] + " <SERVER> <PORT>")
        sys.exit()

    server = args[1]
    port = args[2]

    # connect to server
    cliSocket = connect(server, int(port))
    if not cliSocket:
        print("Failed to connect to " + server)
        sys.exit()

    query = ""

    while True:
        query = (input("ftp> ")).lower().split()
        # print(query)

        # get <FILE NAME>
        # downloads <FILE NAME> from the server
        if query[0] == commands[0]:
            if len(query) != 2:
                print("Usage: get <FILE NAME>")
            else:
                send_data(cliSocket, query[0])
                getFromServer(cliSocket, query[1])
            
        # put <FILE NAME>
        # uploads <FILE NAME> to the server
        elif query[0] == commands[1]:
            if len(query) != 2:
                print("Usage: put <FILE NAME>")
            else:
                send_data(cliSocket, query[0])
                put_file(cliSocket, server, query[1])
            
        # ls
        # lists files on the server
        elif query[0] == commands[2]:
            # send query
            send_data(cliSocket, query[0])

            # get size of response
            responseSize = receive_data(cliSocket, const.HEADER_SIZE)

            if responseSize == "":
                print("Failed to receive size of response")
            else:
                response = receive_data(cliSocket, int(responseSize))
                print(response)

        # quit
        # disconnects from the server and exits
        elif query[0] == commands[3]:
            send_data(cliSocket, query[0])
            cliSocket.close()
            print("Connection closed")
            break
        
        else:
            print("Invalid command")


if __name__ == '__main__':
    run(sys.argv)








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

