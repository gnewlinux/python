# -*- coding: utf-8 -*- 

class Cachorro():
    def __init__(self):
        self.nome = 'Rex'
        self.idade = 2
        print ('Construtor chamado com sucesso!')

    def imprime(self):
        print ('Ola meu nome é %s e tenho %i'%(self.nome, self.idade))

# variavel que armazena objeto
Rex = Cachorro()
Rex.imprime()
