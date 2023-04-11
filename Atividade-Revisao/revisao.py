funcionarios = [
    {
        "nome": "cristian",
        "cpf": "111111",
        "cargo": "devpleno",
        "salario": 8000,
        "telefones": [159159, 148148, 126126],
    },
    {
        "nome": "func2",
        "cpf": "22222",
        "cargo": "func",
        "salario": 1000,
        "telefones": [11111, 22222, 22222],
    }
]


def PesquisarFunc(cpf):
    """Função que pesquisa funcionário pelo seu cpf e exibe na tela seus dados."""
    encontrado = False
    for f in funcionarios:
        if f['cpf'] == cpf:
            for k, v in f.items():
                print(k, v)
            encontrado = True
            break
    if not encontrado:
        print('Funcionário não encontrado.')


def addTel(cpf, telefone):
    """Encontra funcionário e adiciona um novo telefone."""
    encontrado = False
    for f in funcionarios:
        if f['cpf'] == cpf:
            #  adicionar um novo telefone
            f['telefones'].append(telefone)
            encontrado = True
            break
    if encontrado:
        print('Novo telefone adicionado com sucesso.')
        print()
    else:
        print('Funcionário não encontrado.')
        print()


def editaFunc(cpf, **kwargs):
    """Encontra Funcionário e edita os dados."""
    encontrado = False
    for f in funcionarios:
        if f['cpf'] == cpf:
            for k, v in kwargs.items():
                # Editar os dados
                f[k] = v
            encontrado = True
            break
    if encontrado:
        print('Funcionário editado com sucesso.')
    else:
        print('Funcionário não encontrado.')

def delFunc(cpf):
    """Deleta Funcionário através do CPF."""
    encontrado = False
    for f in funcionarios:
        if f['cpf'] == cpf:
                # deleta funcionário
                funcionarios.remove(f)
                encontrado = True
                break
    if encontrado:
        print('Funcionário deletado com sucesso.')
    else:
        print('Funcionário não encontrado.')



"""Testes"""
cpf = input('Informe um CPF para deletar: ')
PesquisarFunc(cpf)

delFunc(cpf)

# cargo = input('Informe o novo cargo para o funcionário: ')
# salario = float(input('Informe o novo salário para o funcionário: '))
# editaFunc(cpf, cargo=cargo, salario=salario)

print(funcionarios)

# cpf = input('Informe um CPF: ')
# PesquisarFunc(cpf)
        
# cpf = input('Informe um CPF: ')
# telefone = int(input('Informe um telefone para adicionar: '))
# addTel(cpf, telefone)

# print(funcionarios)