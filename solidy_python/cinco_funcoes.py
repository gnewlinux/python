# definir funcao
def soma(numero1, numero2):
	resp = numero1 + numero2
	return resp

def imprimi_oi():
	print("oi")

def tem_sete_itens(argumento):
	if len(argumento) == 7:
		return True
	else:
		return False

print(soma(1,2))

imprimi_oi()

if tem_sete_itens('qwerasd'):
	print('realmente tem sete letras')