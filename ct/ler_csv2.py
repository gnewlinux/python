import csv

arquivo = open('brasil.csv', encoding='utf8')

# le em formato de lista
for registro in csv.reader(arquivo):
    if registro[2] != 'habitantes':
        print(registro[2])
