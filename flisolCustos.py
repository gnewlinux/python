ida = 38.10
volta = 33.87
onibus = 8.00
alimentacao = {
	"cafe" : 12.00,
	"almoco" : 20.00,
	"salgado" : 10.00
}

def soma(num1,num2,num3):
	return num1+num2+num3+\
	alimentacao["cafe"]+alimentacao["almoco"]+alimentacao["salgado"]

total = soma(ida,volta,onibus)

print('FLISOL 2018')
print('### Custos ####' + '\nIda: ' + 'R$' + str(ida) + '\nVolta: ' + 'R$' + str(volta) + '\nOnibus: ' + 'R$' + str(onibus))

for n in alimentacao:
	print(str(n), 'R$'+str(alimentacao[n]))

print('Total : R$' + str(total))
