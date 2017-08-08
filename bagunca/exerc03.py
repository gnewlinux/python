# Considere a empresa de telefonia Tchau.
# Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto.
# Entre 200 a 400 minutos, o preço é R$ 0,18. Acima de 400 minutos o preço por
# minutos o preço por minuto é R$ 0,15. 
# Calcule sua conta de telefone.

a = 0.20
b = 0.18
c = 0.15

valor = int(input("Quantos minutos voce usuou da sua conta: "))

if valor < 200:
	print ("Sua conta abaixo de 200 minutos é de : %6.2f" % (valor * a))
if valor >= 200 and valor < 400 :
	valor = valor * b
	print ("Sua conta entre 200 a 400 minutos é de: %2.f" %valor)
if valor >= 400:
	valor = valor * c
	print ("Sua conta maior que 400 minutos é de: %2.f" %valor)
