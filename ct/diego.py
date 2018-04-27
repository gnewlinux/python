import requests
from bs4 import BeautifulSoup

url = 'http://diego.sarzi.com.br/'
requisicao = requests.get(url)
sopa = BeautifulSoup(requisicao.content, "html.parser")

blocos = sopa.find_all('@')

planilha = []

for linha in blocos:
	t = linha.text
	planilha.append(t)

print(planilha)
