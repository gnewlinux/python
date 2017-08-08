#!/usr/bin/python

### metodos para trabalhar com lista

grupos = []

print "Conteudo da lista grupos: ",grupos


## adicionar no final
grupos.append("tecnologia")
grupos.append("tecnologia")
grupos.append("administrativo")
grupos.append("marketing")
grupos.append("diretoria")
grupos.append("treinamento")

# inserir na posicao
grupos.insert(2,"limpeza")

print "Conteudo da lista atualizada: ", grupos
### reverse funcao
#grupos.reverse()

# posicao da lista
print grupos.index("diretoria")

# remover ultimo da lista
grupos.pop()
# ou posicao especifica
grupos.pop(2)

# remover item
grupos.remove("administrativo")

# saber quantos iguais tem na mesma lista
print "Repetidos", grupos.count("tecnologia")


print grupos
