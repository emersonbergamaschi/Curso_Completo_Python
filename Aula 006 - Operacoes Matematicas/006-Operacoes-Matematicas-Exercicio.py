"""
Escreva um Programa que imprime dois numeros de sua escolha
e que depois imprime a soma, a subtração, a multiplicação,
a divisão normal e a divisão inteira,
e o resto da divisão do maior pelo menor
(coloque na mensagem a palavra resto ao invez do símbolo %)

EXEMPLO DE SAÍDA:
>>>
x = 15
y = 10
15 + 10 = 25
15 - 10 = 5
15 x 10 = 150
15 / 10 = 1.5
15 // 10 = 1
15 resto 10 = 5
>>>
"""


x = int(input('Digite um número: '))
y = int(input('Agora digite outro número: '))

print(f'x = {x}')
print(f'y = {y}')
print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x - y}')
print(f'{x} x {y} = {x * y}')
print(f'{x} potencia {y} = {x ** y}')
print(f'{x} / {y} = {x / y}')
print(f'{x} // {y} = {x // y}')
print(f'{x} resto {y} = {x % y}')
