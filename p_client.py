#!/usr/bin/env python
print('--------------------creating a client---------------')
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))

#we just create an ordinary internet socket that uses TCP and then connect it to the localhost IP-address at the port 9999
#To now get the message from the server and decode it,we will use the recv function
message = s.recv(1024)
s.close()
print(message.decode('ascii'))

#after we connect to the server,we try to receive upto 1024 bytes from it.we then save the message into our variable and then we decode and print it

