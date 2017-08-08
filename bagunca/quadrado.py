class Quadrado():
    def __init__(self, valor):
        self.valor = valor

    def mudaValor(self):
        self.valor = input('Digite o valor')

    def retornaValor(self):
        print (self.valor)

    def calculaArea(self):
        self.area = int(self.valor * self.valor)

quadrado = Quadrado(10)
quadrado.mudaValor()
quadrado.calculaArea()
quadrado.retornaValor()
