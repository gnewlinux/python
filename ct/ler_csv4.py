import csv

arquivo = open('brasil.csv', encoding='utf8')
estado = input('Qual estado? ')
estado = estado.upper()
populacao = 0


# le em formato de lista
for registro in csv.reader(arquivo):
    if registro[0] == estado:
        populacao += int(registro[2])

print(populacao)
