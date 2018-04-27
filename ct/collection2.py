import csv
import collections

populacao = collections.Counter()
arquivo = open('brasil.csv', encoding='utf8')

for registro in csv.DictReader(arquivo):
    populacao[registro['estado']] += int(registro['habitantes'])

print(populacao)
