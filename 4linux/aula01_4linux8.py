#!/usr/bin/python

### DICIONARIOS

lista_produtos = [
	{"nome":"Tenis","valor":39.90},
	{"nome":"Camisa","valor":29.90},
	{"nome":"Bermuda","valor":49.90}
]

produto = {"nome":"Bone","valor":109.90}

print lista_produtos[0]["nome"]

print "Voce selecionou o produto %s e o valor e %s"%(produto["nome"], produto["valor"])

produto_c_caracteristicas = {
	"nome":"Tenis",
	"valor":39.90,
	"caracteristicas":{
						"tecido":"camurca",
						"tamanho":29					
					  }

}

print produto_c_caracteristicas["caracteristicas"]["tamanho"]
