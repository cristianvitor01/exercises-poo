"""
2-Faça um Programa que receba uma lista de 10 números reais e mostre-os na ordem inversa.
"""

numeros = []

for num in range(10):
    numeros.append(input('Informe um número inteiro: '))

print('Imprimindo lista em ordem reversa...')
numeros.reverse()

print(numeros)