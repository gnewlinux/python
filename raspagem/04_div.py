from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://frutodagua.com.br/index.php")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("div", {"id":"text"})

for name in nameList:
	print(name.get_text())
