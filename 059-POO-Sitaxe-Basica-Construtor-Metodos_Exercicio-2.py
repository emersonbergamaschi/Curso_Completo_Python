"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe
as medidades de um local. Depois, deve criar um objeto com as medidas e calcular
a quantidade de pisos necessárias para o local.
"""


class Retangulo:
    def __init__(self, larg=10, comp=20):
        self.comprimento = larg
        self.largura = comp

    def mudar_retangulo(self, larg, comp):
        self.comprimento = comp
        self.largura = larg

    def retorna_lados(self):
        return self.largura, self.comprimento

    def calcula_area(self):
        return self.largura * self.comprimento

    def calcula_perimetro(self):
        return (self.largura + self.comprimento) * 2


# -------------------------------------------
# Solicita dimensões do local e calcula área
# -------------------------------------------

l = float(input('Digite a largura do local: '))
c = float(input('Digite o comprimento do local: '))

ret = Retangulo(l, c)
area_local = ret.calcula_area()

# --------------------------------------------------
# Solicita dimensões do piso e calcula área do piso
# --------------------------------------------------

lpiso = float(input('Digite a largura do piso: '))
cpiso = float(input('Digite o comprimento do piso: '))

ret.mudar_retangulo(lpiso, cpiso)
area_piso = ret.calcula_area()

# -----------------------------------
# Calcula total de pisos necessários
# -----------------------------------

total_piso = round(area_local / area_piso)
print(f'O total de pisos necessário para sua área é {total_piso}')
