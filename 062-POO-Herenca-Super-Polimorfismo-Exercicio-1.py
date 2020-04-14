"""
Defina uma nova classe ObjetoGráfico subclasse de object, cujos atributos são:
    cor_de_preenximento --> inteiro
    preenchida --> bool
    cor_de_contorno --> inteiro

Escreva três classes:
    Retangulo --> Atributos: base e altura
    Circulo --> Atributos: raio
    Triangulo --> Atributos: base e altura

Subclasses da classe ObjetoGráfico que possuam todas métodos area e perimetro
"""
from math import pi


class ObjetoGrafico(object):
    def __init__(self, preenchimento, preenchida, contorno):
        self.cor_preenchimento = preenchimento
        self.preenchida = preenchida
        self.cor_contorno = contorno


class Retandulo(ObjetoGrafico):
    def __init__(self, cor_preenchimento, preenchida, cor_contorno, base, altura):
        super().__init__(cor_preenchimento, preenchida, cor_contorno)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base + self.altura) * 2


class Circulo(ObjetoGrafico):
    def __init__(self, cor_preenchimento, preenchida, cor_contorno, raio):
        super().__init__(cor_preenchimento, preenchida, cor_contorno)
        self.raio = raio

    def area(self):
        return pi * (self.raio ** 2)

    def perimetro(self):
        return 2 * pi * self.raio


class Triangulo(ObjetoGrafico):
    def __init__(self, cor_preenchimento, preenchida, cor_contorno, base, altura):
        super().__init__(cor_preenchimento, preenchida, cor_contorno)
        self.base = base
        self.altura = altura
        pass


emerson = Retandulo(1, 1, 1, 30, 20)
print(emerson.area())
print(f'{emerson.perimetro():.2f}')

emerson = Circulo('red', True, 'blue', 20)
print(f'{emerson.area():.2f}')
print(f'{emerson.perimetro():.2f}')
