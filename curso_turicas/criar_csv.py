import csv
import collections

# fazendo contagem a partir do CSV
arquivo = open('brasil.csv', encoding='utf8') # abrindo aqruivo
populacao = collections.Counter() # criando contador vazio
area = collections.Counter()
for registro in csv.DictReader(arquivo):
	populacao[registro['estado']] += int(registro['habitantes'])

# criando arquivo CSV com o resultado
arquivo_saida = open('estados.csv', mode='w', encoding='utf8')
escritor = csv.writer(arquivo_saida, lineterminator='\n')
escritor.writerow(['estado', 'habitantes'])
for estado, habitantes in populacao.most_common():
	escritor.writerow([estado, habitantes])
arquivo_saida.close()
