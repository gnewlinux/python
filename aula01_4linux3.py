#!/usr/bin/python

def func1():
	print "Entrou na funcao 1"

def func2():
	print "Entrou na funcao 2"

def func3():
	print "Entrou na funcao 3"

def switch(x):
	dict_func = {1:func1,2:func2,3:func3}
	dict_func[x]()

# podemos fazer assim:
# switch(1)

# ou assim:

x = input("Digite um valor de 1 a 3: ")
switch(x)

# ou com if
# if x == 1:
#	func1()
#elif x == 2:
#	func2()
#elif x == 3:
#	func3()
#else:
#	print "Funcao errada"
