from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://frutodagua.com.br/index.php")
bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj.h1)
print(bsObj.h1.getText())
