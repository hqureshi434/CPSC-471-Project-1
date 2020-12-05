import os, sys, time, socket

headerSize = 10
serverFolder = "./serverFiles/"
clientFolder = "./clientFiles/"
commands = ["get", "put", "ls", "quit"]

#Send data until all bytes sent
def send_data(sock, data):
    data = data.encode("utf-8")
    sentBytes = 0
    while len(data) > sentBytes:
        sentBytes += sock.send(data[sentBytes:])


# keep receiving data until all bytes are received
def receive_data(sock, size):
                  
        return sock.recv(size).decode("utf-8")
        
# make data size fit in fixed header size
def adjustSize(data, size):
    data = str(data)
    while len(data) < size:
        data = "0" + data
    return data

def get_data_serv(sock, fileName):
        #Send filename we want to receive 
        sendName = fileName.encode()
        sock.send(sendName)

        #Receive content size
        recvSize = sock.recv(40)
        recvSize = recvSize.decode()
        recvSize = int(recvSize)

        #Create var to hold incoming data
        tempMsg = ""
        while True:
                msg = sock.recv(40)
                tempMsg += msg.decode()
                if len(tempMsg)==recvSize:
                        sock.send("1".encode())
                        print("Sent True")
                        break

        #Open file path and create file of received data
        filePath = os.path.join(const.CLIENT_FOLDER, fileName)
        fileData = open(filePath, "w")
        fileData.write(tempMsg)

        print("The file name is: " + fileName)
        print("The number of bytes that got transferred: " + str(recvSize))

        return 0

def send_data_serv(sock):
        #Receive the file we send
        fileName = sock.recv(40)
        fileName = fileName.decode()
        
        #Find file, store it to send
        filePath = os.path.join(const.SERVER_FOLDER, fileName)
        fileData = open(filePath)
        content = fileData.read()
        
        #Get content length, then send
        recvLen = str(len(content)).encode()
        sock.send(recvLen)
        
        #Send content in .5s intervals until everythings sent
        while True:
                content = content.encode()
                sock.send(content)
                recvdata = sock.recv(40)
                recvdata = recvdata.decode()
                if recvdata == "1":
                        print("File has beensent successfully!")
                        break
                time.sleep(.500) #Where we use time from
                
        return 0