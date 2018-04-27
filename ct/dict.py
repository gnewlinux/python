import csv

arquivo = open('brasil.csv', encoding='utf8')
estado_desejado = input('Digite o estado: ')
estado_desejado = estado_desejado.upper()
for registro in csv.DictReader(arquivo):
    densidade = int(registro['habitantes']) / float(registro['area'])
    print(f'Densidade de {registro["municipio"]}: {densidade:.1f} hab/km2')
