"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1. // %
"""
# ======================================
#               SOLUÇÃO 01
# ======================================

valor = int(input('Qual valor você deseja sacar? '))
saque = valor

notas = 0
if 10 <= saque <= 600:
    if saque >= 100:
        while True:
            saque = saque - 100
            notas += 1
            if saque < 100:
                break
    print(f'Voce vai receber {notas} de R$100')
    notas = 0
    if saque >= 50:
        while True:
            saque = saque - 50
            notas += 1
            if saque < 50:
                break
    print(f'Voce vai receber {notas} de R$50')
    notas = 0
    if saque >= 10:
        while True:
            saque = saque - 10
            notas += 1
            if saque < 10:
                break
    print(f'Voce vai receber {notas} de R$10')
    notas = 0
    if saque >= 5:
        while True:
            saque = saque - 5
            notas += 1
            if saque < 5:
                break
    print(f'Voce vai receber {notas} de R$5')
    notas = 0
    if saque >= 1:
        while True:
            saque = saque - 1
            notas += 1
            if saque == 0:
                break
    print(f'Voce vai receber {notas} de R$1')
    notas = 0
else:
    print('Voce não pode sacar este valor')

print('=-' * 20)

# ======================================
#               SOLUÇÃO 02
# ======================================

notas2 = [100, 50, 10, 5, 1]
saque2 = valor
count = 0
if valor < 10:
    print('O valor mínimo para saque é R$10')
elif valor > 600:
    print('O valor máximo para saque é R$600')
else:
    for x in notas2:
        count = 0
        if saque2 >= x:
            while True:
                saque2 = saque2 - x
                count += 1
                if saque2 < x:
                    break
        print(f'Voce vai receber {count} de R${x}')

print('=-' * 20)

# ======================================
#               SOLUÇÃO 03
# ======================================

saque3 = valor
if 10 <= saque3 <= 600:
    notas3 = saque3 // 100
    print(f'Voce vai receber {notas3} de R$100')
    saque3 = saque3 % 100

    notas3 = saque3 // 50
    print(f'Voce vai receber {notas3} de R$50')
    saque3 = saque3 % 50

    notas3 = saque3 // 10
    print(f'Voce vai receber {notas3} de R$10')
    saque3 = saque3 % 10

    notas3 = saque3 // 5
    print(f'Voce vai receber {notas3} de R$5')
    saque3 = saque3 % 5

    notas3 = saque3 // 1
    print(f'Voce vai receber {notas3} de R$1')
    saque3 = saque3 % 1

else:
    print("Nao é possivel fazer o saque")

print('=-' * 20)

# ======================================
#               SOLUÇÃO 04
# ======================================

notas3 = [100, 50, 10, 5, 1]
saque3 = valor
if 10 <= saque3 <= 600:
    for x in notas3:
        notas3 = saque3 // x
        print(f'Voce vai receber {notas3} de R${x}')
        saque3 = saque3 % x
elif saque3 < 10:
    print('O valor mínimo para saque é R$10')
elif valor > 600:
    print('O valor máximo para saque é R$600')
