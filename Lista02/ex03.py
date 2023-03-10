"""
Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem Números iguais. 
"""
num1 = int(input('Informe um número: '))
num2 = int(input('Informe um segundo número: '))

if num1 > num2:
	print(f'{num1} é o maior')
elif num1 == num2:
	print('Números iguais')
else:
	print(f'{num2} é o maior')
	