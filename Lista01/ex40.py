"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados
pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.
"""

valor_dia = 30.00
dias_trabalhados = int(input('Informe o número de dias trabalhados: '))
desc = 0.08

sal = valor_dia * dias_trabalhados
imposto = sal * desc
salario_total = sal - imposto

print('O encanador trabalhou por {} dias e receberá R$ {:.2f}.'.format(dias_trabalhados, salario_total))
