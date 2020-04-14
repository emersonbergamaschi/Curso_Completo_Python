class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def setnome(self, nome):
        self.nome = nome

    def setidade(self, idade):
        self.idade = idade

    def getnome(self):
        return self.nome

    def getidade(self):
        return self.idade


class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade):
        super().__init__(nome, idade)
        self.CPF = cpf

    def setcpf(self, cpf):
        self.CPF = cpf

    def getcpf(self):
        return self.CPF


class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nome):
        super().__init__(nome)
        self.CNPJ = cnpj

    def setcnpj(self, cnpj):
        self.CNPJ = cnpj

    def getcnpj(self):
        return self.CNPJ


Pedro = Pessoa()

Emerson = PessoaFisica(27429743854, 'Emerson Bergamaschi', 45)
print(Emerson.getcpf())

print(Pedro.nome())