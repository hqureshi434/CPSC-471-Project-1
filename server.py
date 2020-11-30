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

#include <String>
#include <stdio>

using namespace std;


void server() {
	int serverPort = 12000
}