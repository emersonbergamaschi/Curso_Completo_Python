"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
"""
import math

area = int(input("Digite o tamanho da área: "))

# Acrescentamos os 10% de folga
area = area * 1.1

# Agora vamos arredondar a área da seguinte maneira
area = math.ceil(area)

# Vamos calcular o numero de litros necessários para pintar a casa
litros = area // 6
if area % 6 > 0:
    litros = litros + 1

print(f'Litros necessários: {litros} \n')

print('1) comprar apenas latas de 18 litros')
latas = litros // 18
if litros % 18 > 0:
    latas = latas + 1

print(f'Serão necessárias {latas} latas')
print(f'Obteremos {latas * 18} litros')
print(f'Total: R$ {latas * 80}\n')

print("2) Comprar apenas galões de 4 litros")
galoes = litros // 4
if litros % 4 > 0:
    galoes = galoes + 1

print(f'Serão necessárias {galoes} galoes')
print(f'Obteremos {galoes * 4} litros')
print(f'Total: R$ {galoes * 25}\n')

# Vamos pensar, o preço total por litro pago nas latas é 80/18 ~ 4.44 R$/L
# enquanto que para o galão é 25/4 ~ 6.25 R$/L
# portanto é sempre mais vantajoso comprar o máximo de latas possíveis
# e o mínimo de galões, desde que o preço desses galoes não ultrapasse o preço
# de uma lata, isto é, o numero de galoes seja menor ou igual a 3 (R$ 75)
print('3) Misturar latas e galões, de forma que o preço seja o menor.')
latas = litros // 18
galoes = 0
litros_restantes = litros % 18

if litros_restantes <= 3 * 4:
    # Ou seja o numero de galoes necessarios seja menor do que três
    galoes = litros_restantes // 4
    if litros_restantes % 4 > 0:
        galoes += 1
else:
    latas += 1

print(f'Serão necessárias {latas} latas')
print(f'Serão necessárias {galoes} galoes')
print(f'Obteremos {latas * 18 + galoes * 4} litros')
print(f'Total: R$ {galoes * 25 + latas * 80}')
