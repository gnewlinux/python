import csv
import collections

arquivo = open('brasil.csv', encoding='utf8') # abrindo aqruivo
populacao = collections.Counter() # criando contador vazio

# fazendo contagem a partir do CSV
for registro in csv.DictReader(arquivo):
	populacao[registro['estado']] += int(registro['habitantes'])

# exibicao da contagem
for estado, habitantes in populacao.most_common():
	print(f'O estado {estado}, possui {habitantes} hab.')
