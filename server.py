#!/usr/bin/env python
import sys
import os
import socket
from datetime import datetime
print("."* 100)

def server_program():
    host = socket.gethostname() #get the hostname
    port = 5000 #initiate port above 1024

    server_socket = socket.socket() #get instance
    server_socket.bind((host,port)) #binds host adress and port together
    
    server_socket.listen(5) # configure how many clients the server can listen simultaneously
    conn,address = server_socket.accept() #accept  new connection
    print("connection from :{}".format(address))
    while True:
        data = conn.recv(1024).decode() #receive data stream.it wount acceptdata packet greater than 1024 bytes
        if not data:
            break# if data is not received break
        print("from connected user: {}".format(data))
        data = input(' -> ')
        conn.send(data.encode()) #send data to the client

    conn.close()

if __name__ == '__main__':
    server_program()

