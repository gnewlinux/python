n1 = 1
n2 = 2

nome = 'Diego'
idade = input('Qual sua idade? ')

nomes = ['Rafa', 'Brena', 'Mel', 'Mateus']

print('Os nomes são: ', nomes)
print('Seu nome e: ', nome, 'e sua idade e', idade)

for x in nomes:
	print(x)

saida = False

while saida == False:
	resposta = input('Sair S/N: ')

	if resposta == 'S':
		print('bye,bye')
		saida = True
	elif resposta == 'N':
		print('OK, fique ai')
	else:	
		print('Digite S/N:')
	pass


for i in range(len(nomes)):
	print(nomes[i])