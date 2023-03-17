"""
4-Faça um Programa que leia lista  de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

lista = ['v', 'a', 's', 'c', 'o']

vogais = ['a', 'e', 'i', 'o', 'u']

cons = [x for x in lista if x not in vogais]

print(cons)