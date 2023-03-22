"""
3-Considere um sistema onde os dados são armazenados em dicionários. Nesse sistema existe um dicionario principal e o dicionário de backup.
Cada vez que o dicionário principal atinge tamanho 5, ele imprime os dados na tela e apaga o seu conteúdo. 
Crie um programa que insira dados em um dicionário, realizando o backup a cada dado e excluindo os dados do dicionário principal
quando ele atingir tamanho 5.
"""

principal = {}
backup = {}

while True:
    chave = input("Digite a chave para inserir no dicionário: ")
    valor = input("Digite o valor para a chave: ")
    principal[chave] = valor
    backup[chave] = valor

    if len(principal) == 5:
        print("Dados do dicionário principal:")
        print(principal)
        principal = {}

    if len(backup) == 10:
        print("Realizando backup dos dados:")
        print(backup)
        backup = {}
