#!/usr/bin/python

### FOR MAIS INDICES

animais = ["gato","cachorro","onca","leao","tartaruga"]

for animal in animais:
	print animal

frutas = ["banana", "maca", "melao", "laranja"]

for fruta in range(0,len(frutas)):
	print frutas[fruta], "numero: ", fruta

## vamos encontrar algum item da lista
## O break se usa para parar o for e ir para o else
for item in animais:
	if item == "leao":
		print "Leao Encontrado!"
		break
else:
	print "Leao nao encontrado :("

grupos = ["tecnologia","vendas","diretoria","treinamento","design"]


## o continue se usa para continuar o loop
for grupo in grupos:
	if grupo == "diretoria":
		print "Diretoria nao precisa alterar senha"
		continue
	print "Usuario do grupos [ %s ] precisa alterar a senha"%grupo
