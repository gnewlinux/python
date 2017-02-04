#!/usr/bin/python
import sys

def menu():
	print "--- Digite a opcao: ---"
	print "\
1 - Cadastrar Usuario\n\
2 - Acessar Sistema\n\
3 - Listar Usuarios\n\
4 - Sair do Sistema\n"
	opcao = input("Digite sua opcao: ")
	return opcao

def switch(x):
	dict_options = {1:cadastrar_usuario,2:acessar_sistema,3:listar_usuarios,4:sair_sistema}
	dict_options[x]()

usuario = []
senha = []

def cadastrar_usuario():
	global usuario
	global senha
	usuario.append(raw_input("Digite seu usuario: "))
	senha.append(raw_input("Digite sua senha: "))

def acessar_sistema():
	global usuario
	global senha

	login = raw_input("Digite seu usuario: ")
	for u in usuario:
		if login == u:
			print "Usuario correto!"
		else:
			print "Usuario invalido"
	
	passwd = raw_input("Digite sua senha: ")
	for s in senha:
		if passwd == s:
			print "Senha correta!"
		else:
			print "Senha invalida"

def listar_usuarios():
	global usuario
	global senha
	for u, name in range(0,len(usuario)):
		print u, name

def sair_sistema():
	print "Bye,bye"
	sys.exit()

if __name__ == "__main__":
	while True:
		switch(menu())
