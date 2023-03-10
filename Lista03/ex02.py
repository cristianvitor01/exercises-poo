"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente.
"""

num = int(input('Informe um número inteiro positivo par: '))

for i in range(0, num+1, 2):
    print(i)
