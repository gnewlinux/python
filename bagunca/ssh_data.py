#!/usr/bin/python

from paramiko.client import SSHClient
import paramiko
from datetime import datetime,date,timedelta
import sys

hosts = ["192.168.1.10","192.168.1.106","192.168.1.100"]

acesso = [2016,02,01,00,00,00]
atual = [2016,02,01,01,00,00]

ssh = SSHClient()
# ler as chaves
ssh.load_system_host_keys()
# se eh um server que nao conheco fazer add
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for h in hosts:
	try:
		print "Conectando no servidor %s na data %s"%(h,datetime.now())
		ssh.connect(h)

		if (atual - acesso).total_seconds() >= 3600:
			print "Seu token de acesso expirou"
			break

		stdin,stdout,stderr = ssh.exec_command('w')
		if stderr.channel.recv_exit_status() != 0:
			print stderr.read()
		else:
			print stdout.read()
		print "Saindo do servidor %s na data %s"%(h,datetime.now())
	except Exception as e:
		print "Nao conseguiu conectar ao servidor: %s"%e
