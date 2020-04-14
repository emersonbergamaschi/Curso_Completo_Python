"""
Escreva um programa de bancos que possua:
    Uma classe Banco com os atributos
    - private total
    - public TaxaReserva
    - private reservaExigida

    E métodos
    - public podeFazerEmprestimo(valor) --> bool
    - public MudaTotal(valor)

E uma classe conta com os atributos
    - private saldo
    - private ID
    - private senha

    E métodos
    - public deposito(senha, valor)
    - public saque(senha, valor)
    - public podeReceberEmprestimo(valor) --> bool
    - public saldo --> float
"""
class Banco(object):
    __total = 10000
    taxareserva = 0.1
    __reservaexigida = __total * taxareserva

    def podeFazerEmprestimo(valor):
        Banco.__total -= valor
        if Banco.__total >= Banco.__reservaexigida:
            pode = True
        else:
            pode = False
        Banco.__total += valor

    def MudaTotal(valor):
        Banco.__total += valor

    def SaldoBanco():
        print(Banco.__total)

class Conta(Banco):
    def __init__(self, dep_inicial, id, senha):
        self.__saldo = dep_inicial
        self.__id = id
        self.__senha = senha
        Banco.MudaTotal(dep_inicial)

    def deposito(self, senha, valor):
        if self.__senha == senha:
            self.__saldo += valor
            Banco.MudaTotal(valor)
            print(f'Seu saldo agora é de {self.__saldo}')
            Banco.SaldoBanco()
        else:
            print('Senha inválida!')

    def saque(self, senha, valor):
        if self.__senha == senha:
            if self.__saldo >= valor:
                self.__saldo -= valor
                Banco.MudaTotal(-valor)
                print(f'Seu saldo agora é de {self.__saldo}')
                Banco.SaldoBanco()
            else:
                print('Saldo insuficiente para este saque!')
        else:
            print('Senha inválida!')

    def podeReceberEmprestimo(self, valor):
        return Banco.podeFazerEmprestimo(valor)

    def saldo(self):
        print(self.__saldo)

itau = Banco()
Emerson = Conta(5000, 1, 123)
Emerson.deposito(123, 2000)
Emerson.saque(123, 1500)
Emerson.deposito(123, 450)
Emerson.saldo()

Pedro = Conta(1000, 1, 321)
Pedro.saldo()

Banco.SaldoBanco()
