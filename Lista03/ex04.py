"""
Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos que compõem o número.
"""

num = int(input('Informe um número inteiro entre 100 e 999: '))

if num >= 100 and num <= 999:
	centenas = num // 100
	dezenas = (num % 100) // 10
	unidades = num % 10

	print(f'Centenas: {centenas}')
	print(f'Dezenas: {dezenas}')
	print(f'Unidades: {unidades}')
else:
	print('Número inválido. Por favor, digite um número entre 100 e 999.')
