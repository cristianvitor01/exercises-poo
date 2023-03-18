"""
5-Faça um Programa que leia 20 números inteiros e armazene-os uma lista. Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima as três listas.
"""

num = []

for item in range(20):
    num.append(int(input('Informe um número: ')))

par = [x for x in num if x % 2 == 0]

impar = [x for x in num if x % 2 != 0]

print(f'Lista: {num}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
