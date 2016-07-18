from random import randint
print ('Bem vindo')
sorteado = randint (1, 100)
chute = 0

while chute != sorteado:
	g = input ('Chute um numero: ')
	chute = int(g)
	if chute == sorteado:
		print ('Voce venceu!')
	else:
		if chute > sorteado:
			print ('alto')
		else:
			print ('baixo')
print ('Fim do jogo')
