#!/usr/bin/python
import sys

usuario = ""
senha = ""

def menu():
	try:
		print "--- Digite a opcao: ---"
		print "\
1 - Cadastrar Usuario\n\
2 - Acessar Sistema\n\
3 - Sair do Sistema\n"
		opcao = input("Digite sua opcao: ")
		return opcao
	except Exception as e:
		print "Erro %s"%e
		return 3

def switch(x):
	try:
		dict_options = {1:cadastrar_usuario,2:acessar_sistema,3:sair_sistema}
		dict_options[x]()
	except Exception as e:
		print "Opcao Invalida"



def cadastrar_usuario():
	global usuario
	global senha
	usuario = raw_input("Digite seu usuario: ")
	senha = raw_input("Digite sua senha: ")
	print "Usuario %s cadastrado com sucesso!"%usuario

def acessar_sistema():
	global usuario
	global senha
	login = raw_input("Digite seu usuario: ")
	passwd = raw_input("Digite sua senha: ")
	if login == usuario and passwd == senha:
		print "Login com sucesso!"
		print "ACESSO LIBERADO!"
	else:
		print "Login ou senha invalidas"

def sair_sistema():
	print "Bye,bye"
	sys.exit()

if __name__ == "__main__":
	while True:
		switch(menu())
