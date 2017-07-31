from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://frutodagua.com.br/index.php")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll({"h1","h2","h3","p"})

for name in nameList:
	print(name.get_text())

# Podendo utilizar tambem para classes:
# findAll("span", {"class":"green"})
# findAll(text="the prince")
# findAll(id="text")

