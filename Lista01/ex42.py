"""
Receba o salário base de um funcionário, calcule e imprima o salário a receber,
sabendo-se que o funcionário tem gratificação 5% sobre o salário base e paga imposto de 7% também sobre o salário base.
"""

salario_base = float(input('Informe o salário base do funcionário: '))
bonus = salario_base * 0.05
imposto = salario_base * 0.07

salario = (salario_base + bonus - imposto)

print('O salário a receber é de R$ {:.2f}'.format(salario))