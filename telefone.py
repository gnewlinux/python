conta = float(input("Digite o valor de sua conta: "))
if conta < 200:
    preco = 0.20
else:
    if conta <= 400:
        preco = 0.18
    else:
        preco = 0.15
print("Conta telefonica: R$%6.2f" % (conta * preco))
