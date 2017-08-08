class Meu_Objeto():
    def __init__(self):
        self.nome = 'Pedro'
        self.idade = 27
        print ('Construtor chamado com sucesso')
    
    def imprime(self):
        print ("Ola meu nome é %s e minha idade é %d" %(self.nome, self.idade))

Pedro = Meu_Objeto()
Pedro.imprime()

class Meu_SegundoObjeto():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprime(self):
        print (self.nome, self.idade)
        

Jose = Meu_SegundoObjeto('Jose', 20)
Jose.imprime()
