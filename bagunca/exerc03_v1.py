minutos = int(input("Minutos utilizados: "))

if minutos < 200:
	preco = 0.20
else:
	if minutos <=400:
		preco = 0.18
	else:
		preco = 0.15
		if minutos <= 800:
			preco = 0.08

print ("Conta telefonica: R$%6.2f" % (minutos * preco))