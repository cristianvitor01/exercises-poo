"""
Crie um dicionário que é uma agenda e coloque nele os seguintes dados:
chave (cpf), nome, idade, telefone. O programa deve ler um número indeterminado de dados,
criar a agenda e imprimir todos os itens do dicionário no formato chave: nome-idade-fone.
"""

agenda = {}

# para o número indeterminado de dados.
while True:
    cpf = input('Digite o CPF: ')

    # o laço para quando o cpf não é informado.
    if not cpf:
        break
    
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    telefone = input('Digite o telefone: ')
    
    agenda[cpf] = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone
    }

print('Agenda:')
for cpf, dados in agenda.items():
    print(f"{dados['nome']}-{dados['idade']}-{dados['telefone']}")
