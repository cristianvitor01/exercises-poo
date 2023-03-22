"""
2-Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e depois coloque em um dicionário.
Depois remova todas as pessoas menores de 18 anos do dicionário e coloque em outro dicionário.
"""

pessoas = {}
menores = {}

while True:
    cpf = input('Digite o CPF: ')

    # o laço para quando o cpf não é informado.
    if not cpf:
        break
    
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))

    pessoas[cpf] = {
        'nome': nome,
        'idade': idade,
    }

    if idade < 18:
        menores[nome] = pessoas


print("Pessoas menores de 18 anos: ")
print(menores)