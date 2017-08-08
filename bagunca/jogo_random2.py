from random import randint

n = (randint(1,10))
p = 0
t = 0

while p != n:
    p = int(input("Digite o numero: "))
    t += 1
    if p == n:
        print("Parabens! Seus pontos: %i" % t)

    elif p < n:
        print("Digite um numero maior")
    else:
        print("Digite um numero menor")

print("fim do jogo")
