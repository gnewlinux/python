from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://frutodagua.com.br/index.php")
bsObj = BeautifulSoup(html, "html.parser")

# children (onelevel) x descendants (all)
# se voce possui o id da tabela use-o
for child in bsObj.find("table",{"id":"giftList"}).children:
	print(child)
