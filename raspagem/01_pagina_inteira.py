from urllib.request import urlopen
html = urlopen("http://www.frutodagua.com.br/index.php")
print(html.read().decode('utf-8'))
