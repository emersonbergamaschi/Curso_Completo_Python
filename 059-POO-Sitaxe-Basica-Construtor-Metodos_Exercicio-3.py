"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor
que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    nome = ''
    idade = ''
    peso = ''
    altura = ''

    def envelhecer(self, anos=1):
        self.idade += anos
        return self.idade

    def engordar(self, eng_kg=1):
        self.peso += eng_kg
        return print(self.peso)

    def emagrecer(self, ema_kg):
        self.peso -= ema_kg
        return print(self.peso)

    def crescer(self, daquiidade):
        if self.idade < 21:
            c = (21 - self.idade) * 0.05
            return print(self.altura + c)


p = Pessoa()
p.nome = 'Emerson'
p.peso = 83
p.idade = 20
p.altura = 1.75
print(p.peso)

p.engordar(3)
p.crescer(2)
p.emagrecer(10)

print(p.__dict__)
