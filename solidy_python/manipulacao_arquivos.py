#!/usr/bin/env python3

while True:
		
	resp = input('Oque deseja? le, escreve, apagar, sair: ')

	if resp == 'le':
		le = open('arquivo.txt', 'r')
		print(le.read())
		le.close()
	elif resp == 'escreve':
		palavra = input('Oque deseja escrever? ')
		escreve = open('arquivo.txt', 'a') # 'a' append
		escreve.write(palavra)
		escreve.close()
	elif resp == 'apagar':
		apagar = open('arquivo.txt','w')
		print('Texto apagado com sucesso!')
		apagar.close()
	elif resp == 'sair':
		break
	else:
		print('Digite corretamente a resposta!')