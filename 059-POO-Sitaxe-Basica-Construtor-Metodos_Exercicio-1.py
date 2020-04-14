"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, lado=50):
        self.lado = lado

    def muda_lado(self, mlado):
        self.lado = mlado

    def retorna_lado(self):
        return print(self.lado)

    def calcula_area(self):
        return print(self.lado ** 2)


quad = Quadrado(30)
quad.retorna_lado()
quad.muda_lado(15)
quad.retorna_lado()
quad.calcula_area()
