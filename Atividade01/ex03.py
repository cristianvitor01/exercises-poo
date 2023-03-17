"""
3-Faça um Programa que leia 4 notas, adicione em uma lista e mostre as notas e a média na tela.
"""

notas = list()

for i in range(4):
    notas.append(int(input('Informe uma nota: ')))
    media = sum(notas)/4

print(f'Notas: {notas}')
print(f'Media: {media}')