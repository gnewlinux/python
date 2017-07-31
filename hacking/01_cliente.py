#!/usr/bin/env python
import socket

host = '192.168.0.107'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))

print s.recv(1024)
s.send('Ola Server')
s.close()