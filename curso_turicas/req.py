import requests
from bs4 import BeautifulSoup

#url = 'http://diego.sarzi.com.br/'
#resposta = requests.get(url)
#print(resposta.text)

requisicao = requests.get('https://twitter.com/diegosarzi')
sopa = BeautifulSoup(requisicao.content, "html.parser")

blocos = sopa.find_all('p', {'class':'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'})

for linha in blocos:
	twitter = linha.text
	print(twitter)

