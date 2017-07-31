#!/usr/bin/env python
import socket

host = '192.168.0.107'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))
s.listen(2)
while True:
	conn, addr = s.accept()

	print addr, "Conectado"
	conn.send("Obrigado por conectar")
	conn.close()