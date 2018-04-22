import csv
import collections

# fazendo contagem a partir do CSV
arquivo = open('brasil.csv', encoding='utf8') # abrindo aqruivo
populacao = collections.Counter() # criando contador vazio
area = collections.Counter()
for registro in csv.DictReader(arquivo):
	populacao[registro['estado']] += int(registro['habitantes'])
	populacao[registro['estado']] += float(registro['area'], 'ola')



populacao = populacao.most_common()
area = area.most_common()
print(populacao, area)




# criando arquivo CSV com o resultado
arquivo_saida = open('estados.csv', mode='w', encoding='utf8')
escritor = csv.writer(arquivo_saida, lineterminator='\n')
escritor.writerow(['estado', 'habitantes', 'area'])
for estado, habitantes in populacao:
	escritor.writerow([estado, habitantes])

for areas in area:
	escritor.writerow([areas])

arquivo_saida.close()
