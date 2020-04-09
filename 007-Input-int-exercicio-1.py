"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média
"""
soma = int(input("Digite a primeira nota: "))
soma = soma + int(input("Digite a segunda nota: "))
soma = soma + int(input("Digite a terceira nota: "))
soma = soma + int(input("Digite a quarta nota: "))
media = soma / 4  # queremos um numero real

print(f'A média do aluno foi, {media}')
