#!/usr/bin/python

from paramiko.client import SSHClient
import paramiko

ssh = SSHClient()
# ler as chaves
ssh.load_system_host_keys()
# se eh um server que nao conheco fazer add
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.1.106")
stdin,stdout,stderr = ssh.exec_command('ls -la')

if stderr.channel.recv_exit_status() != 0:
	print stderr.read()
else:
	print stdout.read()
