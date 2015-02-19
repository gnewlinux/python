# Pergunte a velocidade de um carro, supondo um valor inteiro. Caso ultrapasse 110 km 
# exiba uma mensagem dizendo que o usuario foi multado. Neste caso, exiba o valor da
# multa cobrando 5 reais por jm acima de 110.

km = int(input("Qual velocidade do seu carro? "))

if km > 110 :
	multa = (km - 110) * 5
	print ("Voce foi multado em: %d" %multa)