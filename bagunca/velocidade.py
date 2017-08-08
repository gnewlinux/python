velocidade = int(input("Qual a velocidade do carro? "))
if velocidade < 110:
    print("Voce estava em velocidade permitida")
if velocidade >= 110:
    print("Multa por velocidade!")
    multa = velocidade - 110
    multa = multa * 5
    print('Valor da multa: R$',multa,',00')
