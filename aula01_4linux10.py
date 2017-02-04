#!/usr/bin/python

## uso o import sys para o sys.exit() no sair do programa
import sys

## mais sobre funcoes

nome = ""
senha = ""

def cadastrar_usuario():
	# buscar uma variavel global
	global nome
	global senha
	nome = raw_input("Digite o login do novo usuario: ")
	senha = raw_input("Digite a senha do novo usuario: ")
	print "Usuario cadastrado com sucesso"

def acessar_sistema():
	global nome
	global senha
	print "Sistema acessado"
	login = raw_input("Digite seu usuario: ")
	passwd = raw_input("Digite sua senha: ")
	if nome == login and senha == passwd:
		print "Autenticado com Sucesso! \n Seja bem vindo %s"%nome
	else:
		print "Acesso Negado"


def sair_sistema():
	print "Saindo do sistema..."
	sys.exit()
	

def menu():
	print "\
			1 - Cadastrar Usuario \n\
			2 - Acessar Sistema \n\
			3 - Sair do Sistema \n"
	opcao = input("Digite a opcao desejada: ")
	return opcao

def switch(x):
	dict_options = {1:cadastrar_usuario,2:acessar_sistema,3:sair_sistema}
	dict_options[x]()

if __name__ == '__main__':
	while True:
		switch(menu())
