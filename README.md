# CPSC-471-Project-1
Project Assignment for CPSC 471 

Jared Castaneda - jaredcast@csu.fullerton.edu - Section 1
Ricardo Martinez - Rickym72@csu.fullerton.edu - Section 1
Hammad Qureshi - qureshi434@csu.fullerton.edu - Section 4
Omar Ramirez - ramirez97@csu.fullerton.edu - section 1

Language used: Python 3.9.0

How to execute: 
	Step 1: Run the server that will actively listen for connections.
	$ py server.py "PORT"
	Example: $ py server.py 12000

	Step 2: Run the client which will connect to the server.
	$ py client.py "SERVER MACHINE" "PORT"
	Example: $ py client.py 127.0.0.1 12000

	List of commands for client.py:
	ftp> get "FILE NAME" :	downloads "FILE NAME" from the server
	ftp> put "FILE NAME" :	uploads "FILE NAME" from the client to the server
	ftp> ls		     :	lists fils on the server
	ftp> quit	     :	disconnects and exits

Notes:
	Client files are read and stored in the clientFiles folder.
	Server files are read and stored in the serverFiles folder.
