#!/usr/bin/python

def lerArquivo():
	try:
		with open("arquivo.txt","r") as f:
			print f.read()
	except Exception as e:
		print "Arquivo nao existes: %s"%e

def escreverArquivo():
	try:
		with open("arquivo.txt","w") as f:
			f.write("Escrendo no arquivo!")
	except Exception as e:
		print "Nao foi possivel escrever no arquivo"


if __name__ == "__main__":
	escreverArquivo()
	lerArquivo()
