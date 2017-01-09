class Carro:
    
    def criarNome(self, nome):
        self.nome = nome

    def criarAno(self, ano):
        self.ano = ano

    def obterNome(self):
        return self.nome

    def obterAno(self):
        return self.ano

carro = Carro()
carro.criarNome('Camaro')
carro.criarAno(2010)

print carro.obterNome()
print carro.obterAno()
