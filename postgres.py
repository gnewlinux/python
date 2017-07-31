#!/usr/bin/python

import psycopg2

try:
	con = psycopg2.connect("host=127.0.0.1 dbname=python user=admin password=4linux")
	print "Comunicacao com o banco... ok"
	cur = con.cursor()

except Exception as e:
	print "Erro %s"%e
