a = 0.20
b = 0.18
c = 0.15

valor = float(input('Digite o valor de sua conta: '))

if valor < 200:
	valor = valor * a
	print ('Valor da conta: %.2f' %valor)
	print (a)
elif valor >= 200 and valor < 400:
	valor = valor * b
	print ('Valor da conta: %.2f' %valor)
	print (b)
elif valor >= 400:
	valor = valor * c
	print ('Valor da conta: %.2f' %valor)
	print (c)
