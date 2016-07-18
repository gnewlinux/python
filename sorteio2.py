from random import randint

print ('Bem Vindo')

sorteado = randint (1, 100)
chute = 0
contador = 0

while chute != sorteado:
	ninput = input ('Chute um numero: ')
	chute = int(ninput)
	contador = contador + 1
	if chute == sorteado:
		print ('Voce venceu!')
	else:
		if chute > sorteado:
			print ('alto')
		else:
			print ('baixo')

print ('Fim do jogo')
print 'Voce jogou ', contador, 'vezes'
