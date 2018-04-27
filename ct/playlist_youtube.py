import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=DqPgURTYygQ&list=RDDqPgURTYygQ&t=214'

requisicao = requests.get(url)
sopa = BeautifulSoup(requisicao.content, 'html.parser')


blocos = sopa.find_all('a')
planilha = []

for linha in blocos:
	bloco = linha.split('href')[1]
	print(bloco)
