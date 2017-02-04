#!/usr/bin/python

### FUNCOES !!!

def autentificacao():
	print "-- Autentificacao Usuario --"
	nome = raw_input("Digite seu usuario: ")
	senha = raw_input("Digite sua senha: ")
	if nome == "gnew" and senha == "123":
		autenticado = True
	else:
		autenticado = False
	return autenticado

def liberar_acesso(auth):
	if auth:
		print "Acesso Permitido!"
	else:
		print "Acesso Negado!"

if __name__ == 	'__main__':
	#autenticado = autentificacao()
	liberar_acesso(autentificacao())
