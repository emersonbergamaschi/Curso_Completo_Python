class Meu_Objeto():
    def __init__(self, n, i):
        self.nome = n
        self.idade = i
        print(f'Construtor chamado com sucesso!')
    def imprime(self):
        print(f'Olá meu nome é {self.nome} e tenho {self.idade} anos.')


Pedroca = Meu_Objeto('Emerson', 44)
Pedroca.imprime()
