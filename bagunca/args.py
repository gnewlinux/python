#!/usr/bin/python

def argumentos(*args):
	if len(args) == 1:
		print "Calcule area do quadrado:"
		print args[0] * args[0]	
	elif len(args) == 3:
		print "Calcule area do retangulo:"
		print args[0] * args[1] * args[2]	
	else:
		print "Outro objeto"


if __name__ == "__main__":
	argumentos(2,3,1)
