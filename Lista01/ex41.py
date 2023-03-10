"""
Faça um programa que leia o valor da hora de trabalho (em reais) e o número de
horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando
10% sobre o valor calculado.
"""

valor_hora = float(input('Informe o valor da hora de trabalho: '))
horas_trabalhadas = float(input('Informe o número de horas trabalhadas no mês: '))

valor = valor_hora * horas_trabalhadas
acrescimo = valor * 0.1
valor_pago = valor + acrescimo

print('O valor a ser pago é de R$ {:.2f}'.format(valor_pago))
