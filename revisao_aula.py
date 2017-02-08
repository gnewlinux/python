#!/usr/bin/python

nome1 = raw_input("Nome 1 :  ")
nome2 = raw_input("Nome 2 :  ")
idade1 = raw_input("Idade  1 : ")

lista = {"nomes":[nome1, nome2], "idades":[idade1]}

print lista.values(lista[1])


#print "Primeiro nome: " + lista["nomes"][0]
#print "Segundo nome: " + lista["nomes"][1]

#print "Escolha um nome para ser exibido: "
#print len(lista["idades"])
