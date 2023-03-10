"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre
ambos.
"""
num1 = int(input('Informe um número: '))
num2 = int(input('Informe um segundo número: '))

if num1 > num2:
	print(f'{num1} é o maior')
else:
	print(f'{num2} é o maior')

diff = (num1 - num2)

print(f'Diferença entre eles: {diff}')
