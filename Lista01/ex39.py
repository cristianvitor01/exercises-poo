"""
A importância de 780.000,00 será dividida entre três ganhadores de um concurso. O primeiro receberá 46%;
O segundo receberá 32%; O terceiro reberá o restante;  Calcule  e imprima a quantia ganha por cada um.
"""

valor_total = 780000.00

primeiro_ganhador = valor_total * 0.46
segundo_ganhador = valor_total * 0.32
terceiro_ganhador = (valor_total - primeiro_ganhador - segundo_ganhador)

print('O primeiro ganhador recebe: R$ {:.2f}'.format(primeiro_ganhador))
print('O segundo ganhador recebe: R$ {:.2f}'.format(segundo_ganhador))
print('O terceiro ganhador recebe: R$ {:.2f}'.format(terceiro_ganhador))