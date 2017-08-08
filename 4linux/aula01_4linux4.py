#!/usr/bin/python

### COMANDO WILHE

num = 1

while num <= 10:
	print num
	num += 1

opcao = ""

while opcao != "#sair":
	print "Digite a funcao que voce quer executar: "
	opcao = raw_input()

while True:
	opcao = raw_input("Digite a opcao: ")
	if opcao == "#sair":
		break

print "Fim do while"
