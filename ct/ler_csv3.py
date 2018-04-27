import csv

arquivo = open('brasil.csv', encoding='utf8')
populacao = 0

# le em formato de lista
for registro in csv.reader(arquivo):
    if registro[2] != 'habitantes':
        populacao += int(registro[2])

print(populacao)
