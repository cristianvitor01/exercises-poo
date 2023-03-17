"""
4-Faça um Programa que leia lista  de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

lista = []

vogais = ['a', 'e', 'i', 'o', 'u']

for i in range(5):
    lista.append(input('Informe um caractere: '))

cons = [x for x in lista if x not in vogais]

print(cons)

qtt = len(cons)

print(f'Quantidade de consoantes: {qtt}')

