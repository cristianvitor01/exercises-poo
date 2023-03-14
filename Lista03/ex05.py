"""
Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número superior ao número lido. Exemplo: se o usuário informou o número 30, a sequência a ser impressa será0 1 1 2 3 5 8 13 21  34.
"""
numero = int(input('Informe um número positivo: '))

anterior = 0
atual = 1

while atual <= numero:

	print(atual, end=" | ")

	proximo = anterior + atual
	anterior = atual
	atual = proximo

print()