valor = int(input('Digite o valor da sua conta: '))

if valor < 200:
	preco = 0.20
else:
	if valor <= 400:
		preco = 0.18
	else:
		preco = 0.15

print ('Conta telefonica: R$%6.2f' % (valor * preco))
