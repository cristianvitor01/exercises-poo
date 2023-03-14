"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""

qtt_num = int(input('Informe a quantidade de números a serem lidos: '))

maior_num = None # armazenar o maior número

cont_maior = 0 # contar quantas vezes o maior número foi lido

for i in range(qtt_num):
	num = float(input(f'Digite o {i+1}º: '))

	if maior_num is None or num > maior_num: # se o número digitado for maior que o último maior, então 'maior_num = num' e cont recebe 1.
		maior_num = num
		cont_maior = 1
	elif num == maior_num:
		cont_maior += 1

print(f'O maior número lido foi {maior_num}, que foi lido {cont_maior} vezes.')
