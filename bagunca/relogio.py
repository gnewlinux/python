#!/usr/bin/env python3
from time import strftime, sleep
import os
from clima import Clima

def tic():
	os.system('clear')
	os.system('setterm -cursor off')
	hora = strftime('\n 	 	    Horas: %H:%M')
	print(hora)
	
	Clima.ver_clima()

	sleep(60)
	tac()

def tac():
	tic()

tic()
