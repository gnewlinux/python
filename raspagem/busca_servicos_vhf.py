from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://py4bo.blogspot.com.br/2012/02/frequencia-vhf-servico-publico-e.html")
bsObj = BeautifulSoup(html.read(), 'html.parser')
lista = bsObj.findAll('div', {'class':'post-body entry-content'})

for text in lista:
	print(text.getText())

#print(html.read().decode("utf-8"))
#print(bsObj.h1)
#print(bsObj.h1.getText())
