#!/usr/bin/env python
print('----------creating a port scanner example-----')
#What a port scanner basically does is: It tries to connect to certain ports at a host or a whole network, in order to find loopholes for future attacks. Open ports mean a security breach. And with our skills, we can already code our own penetration testing tool.
import socket
target = "192.168.23.1"

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conn = s.connect((target,port))
        return True
    except:
        return False
    
    for x in range(1,501):
        if(portscan(x)):
            print("Port {} is open!".format(x))
        else:
            print("Port {} is closed!!".format(x))


