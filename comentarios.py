# Voce pode fazer um comentario usando o #
'''
	
	Ou voce pode comentar dessa forma

'''

a = int(input("Primeiro: "))
b = int(input("Segundo: "))
c = int(input("Terceiro: "))

if a >= b and a >= c:
	print ("Primeiro %d" %a)
elif b >= c:
	print ("Segundo %d" %b)
else:
	print ("Terceiro %d" %c)