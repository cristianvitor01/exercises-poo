"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%
"""

sal = float(input("Informe o salário do funcionário: "))
new_sal = sal*1.25

print('O novo salário do funcionário é R$ {:.2f}'.format(new_sal))
