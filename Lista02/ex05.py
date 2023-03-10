"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
"""
sal = float(input('Informe o salário do trabalhador: '))
emprest = float(input('Informe o valor da prestação do empréstimo: '))

prest20 = emprest * 0.20

if sal > prest20:
	print('Empréstimo não concedido.')
else:
	print('Empréstimo concedido.')
	