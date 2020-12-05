import os, sys, socket
from datafun import send_data, receive_data, adjustSize, send_data_serv


headerSize = 10
serverFolder = "./serverFiles/"
clientFolder = "./clientFiles/"
commands = ["get", "put", "ls", "quit"]

def bind(port = 0):
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind(('', port))
        serverSocket.listen(1)
    except Exception as e:
        print(e)
        return None
    return serverSocket

def receive_file(sock):
    #Create a brand new socket
    newSocket = bind()

    #Sending the port number to client
    serverPort = newSocket.getsockname()[1]
    send_data(sock, str(serverPort))

    #Accept connection
    print("Listening on port number: " + str(serverPort))
    dataSocket, addr = newSocket.accept()
    print("Currently connected to: " + addr[0])

    # Get sizes
    filenameSize = receive_data(dataSocket, headerSize)
    fileDataSize = receive_data(dataSocket, headerSize)

    # error checking
    if fileNameSize == "":
        print("Error retrieving filename size")
        return

    if fileDataSize == "":
        print("FaiError retrieving data size")
        return

    # read payload
    fileName = receive_data(dataSocket, int(fileNameSize))
    fileData = receive_data(dataSocket, int(fileDataSize))

    # write file
    filePath = serverFolder + fileName
    userFile = open(filePath, "w")
    userFile.write(fileData)

    print(fileName + " received!")
    print("The file size is: " + fileDataSize)

    # close file and connection
    userFile.close()
    dataSocket.close()
    print("File and data socket are now closed.")

def run(args):
    if len(args) != 2:
        print("Usage: python3 " + args[0] + " <PORT>")
        sys.exit()

    port = args[1]

    #Bind socket to given port number, args[1]
    serverSocket = bind(int(port))
    if not serverSocket:
        print("ERROR: CANNOT BIND A PORT.")
        sys.exit()

    while True:
        # keep listening for connections until user ends process
        print("Status: Currently listening on port " + port)
        clientSocket, addr = serverSocket.accept()
        print("Currently connected to: " + addr[0])

        while True:
			#Get the query passed in from client
            query = receive_data(clientSocket, heade)

            # get <file name>, downloads <file name> from server
            if query == commands[0]:
                send_data_serv(clientSocket)

            # put <file name>, uploads to client
            elif query == commands[1]:
                receive_file(clientSocket)

            # ls, lists files on the server
            elif query == commands[2]:
                #Get all file names from specified folder
                files = os.listdir(serverFolder) 
                response = "" #will hold the response
                for file in files:
                    response += file + "  "
                response = response[:-2]

                # Send the response
                responseSize = adjustSize(len(response), headerSize)
                data = responseSize + response
                send_data(clientSocket, data)

            # quit
            # closes the connection
            elif query == commands[3]:
                clientSocket.close()
                print("Closing the connection.")
                break

            else:
                print("Invalid command. Closing connection")
                clientSocket.close()
                break

if __name__ == '__main__':
    run(sys.argv)

"""
//Pseudocode (with changes) from the assignment PDF for the server
/*
//Server code
 from socket import ∗

 //The port on which to listen
 serverPort = 12000

 //Create a TCP socket
 serverSocket = socket(AF INET, SOCK STREAM) 9
 //Bind the socket to the port
 serverSocket.bind(( ’ ’, serverPort))

 //Start listening for incoming connections
 serverSocket.listen(1)15
 print ”The server is ready to receive” 17
 //Forever accept incoming connections
 while 1 :
 //Accept a connection ; get client’s socket
 connection Socket , addr = serverSocket.accept()

 //The temporary buffer
 tmpBuff= ”” 25
 while len (data) != 40:
 //Receive whatever the newly connected client has to send
 tmpBuff = connectionSocket . recv (40 29
 //The other side unexpectedly closed it’s socket
 if not tmpBuff :
 break

 //Save the data
 data += tmpBuff

 print data 38
 //Close the s ocket
  connection Socket.close()
  */
"""



