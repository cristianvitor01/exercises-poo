"""
Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.
"""

num = int(input('Informe um número inteiro: '))

for i in range(1, 2*num, 2):
    print(i)
