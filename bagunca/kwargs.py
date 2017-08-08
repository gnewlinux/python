#!/usr/bin/python

## KWARGS e para trabalhar com dicionairos
## dicionario = {"nome":"valor","nome2":"valor2"}

def exemplo(**kwargs):
	print type(kwargs)
	print kwargs

if __name__ == "__main__":
	exemplo(nome="Tenis",preco=59.90,categoria="Calcados")
