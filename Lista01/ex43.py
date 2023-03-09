"""
- Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
- o total a pagar com desconto de 10%;
- o valor de cada parcela, no parcelamento de 3 x sem juros;
- a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto )
- a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""
valor_total = float(input('Digite o valor total da venda: '))

desc = valor_total * 0.1
novo_valor = valor_total - desc

print('Total a pagar com desconto de 10%: R$ {:.2f}'.format(novo_valor))

parcela = valor_total / 3

print('Valor de cada parcela (3x sem juros): R$ {:.2f}'.format(parcela))

comissao_vista = novo_valor * 0.05
comissao_parcelada = valor_total * 0.05

print('Comissão do vendedor à vista: R$ {:.2f}'.format(comissao_vista))
print('Comissão do vendedor parcelada: R$ {:.2f}'.format(comissao_parcelada))
