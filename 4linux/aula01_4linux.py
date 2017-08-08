#!/usr/bin/python

num1 = 1
num2 = 2

print num1 + num2
print num1 - num2
print num1 * num2
print num1 / num2
print num1 % num2

num1 = num1 + 2
print num1

print "Hello Wold"

# feita validacao
prog = raw_input("Qual a melhor linguagem de programacao: ")

if prog == "python":
    print "Voce acertou"
else:
    print "Voce errou"

nome = raw_input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print "Seu nome e: "+nome+" e sua idade e: ",idade
print "Seu nome e: "+nome+" e sua idade e: "+str(idade)
print "Seu nome e: %s e sua idade e %s"%(nome,idade)
