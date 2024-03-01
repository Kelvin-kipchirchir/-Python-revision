#!/usr/bin/env python
print('----------welcome to network programming-------------')
'about communicating with other applications and devices via some networks.Can be internet or just local area network.'
'Sockets->These are endpoints of the communication channel or basically,the endpoints that talk to each other.The communication may happen in the same process or even across different continents'
# creating sockets->
import socket
#Now, before we start defining and initializing our socket, we need to know a couple of things in advance:
  #  · Are we using an internet socket or a UNIX socket?
  # · Which protocol are we going to use?
   # · Which IP-address are we using?
   # · Which port number are we using?


#The first question can be answered quite simply. Since we want to communicate over a network instead of the operating system, we will stick with the internet socket . The next question is a bit trickier. We choose between the protocols TCP (Transmission Control Protocol) and UDP ( User Datagram Protocol). TCP is connection-oriented and more trustworthy than UDP. The chances oflosing data are minimal in comparison to UDP. On the other hand, UDP is much faster than TCP. So the choice depends on the task we want to fulfil.
#For our examples, we will stick with TCP since we don’t care too much about speed for now.The IP-address should be the address of the host our application will run on.For now, we will use 127.0.0.1 which is the localhost address. This applies to every machine. But notice that this only works when you are running your scripts locally.For our port we can basically choose any number we want. But be careful with low numbers, since all numbers up to 1024 are standardized and all numbers from 1024 to 49151 are reserved . If you choose one of these numbers, you might have some conflicts with other applications or your operating system.

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Here we created our first socket, by initializing an instance of the class socket . Notice that we passed two parameters here. The first one AF_INET states that we want an internet socket rather than a UNIX socket . The second one SOCK_STREAM is for the protocol that we choose. In this case it stands for TCP . If we wanted UDP , we would have to choose SOCK_DGRAM.
# CLIENT SERVER ARCHIECTURE
#3  SERVER SOCKET METHODS
# binds() ->binds the address that consist of hostname and port to the socket
# listen() ->waits for a message or a signal
# accept() ->Accepts the connection with the client

#CLIENT SOCKET METHODS
# connect() ->client attempts to connect to the server which has to accept this
# recv() ->receives a TCP message
# send() ->sends a TCP message
# recvfrom() ->Receives the UDP message
# sendto() ->Sends a UDP message
# close() ->closes a socket
# gethostname() ->Returns hostname of a socket


'CREATING A SERVER'
#using TCP and an internet socket.
#using localhost adress 127.0.0.1 and port 9999
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(("127.0.0.1",9999))
soc.listen()

print('Listening...')


