from random import randint

n = (randint(1,10))
p = 0
t = 0

while n != p:
    p = int(input("Seu palpite: "))
    t += 1

    if p == n:
        print("Parabens! Sua pontuacao é: %i" % t)

    elif p > n:
        print("Tente um numero menor")
    else:
        print("Tente um numero maior")
print("Fim do jogo")
