funcionarios = [
    {
        "nome": "cristian",
        "cpf": "111111",
        "cargo": "cargo-teste1",
        "salario": 8000,
        "telefones": [159159, 148148, 126126],
    },
    {
        "nome": "func2",
        "cpf": "22222",
        "cargo": "cargo-teste2",
        "salario": 1000,
        "telefones": [11111, 22222, 22222],
    }
]

def cadastrarFuncionario():
    print('Adicionar um novo funcionário no sistema.')
    print()
    nome = input('Nome: ')
    cpf = input('CPF: ')
    cargo = input('Cargo: ')
    salario = float(input('Salário: '))
    telefones = []
    while True:
        telefone = input('Telefone (ou ENTER para sair): ')
        if telefone == "":
            break
        telefones.append(telefone)

    funcionario = {"nome": nome, "cpf": cpf, "cargo": cargo, "salario": salario, "telefones": telefones}
    funcionarios.append(funcionario)
    print("Funcionario cadastrado com sucesso!")

def PesquisarFunc(cpf):
    """Função que pesquisa funcionário pelo seu cpf e exibe na tela seus dados."""
    encontrado = False
    for f in funcionarios:
        if f['cpf'] == cpf:
            print()
            print('Funcionário encontrado: ')
            print()
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
        [print(funcionario) for funcionario in funcionarios]
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
        print()
        [print(funcionario) for funcionario in funcionarios]
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
        print()
        [print(funcionario) for funcionario in funcionarios]
    else:
        print('Funcionário não encontrado.')


print('Funcionários Cadastrados: ')
[print(funcionario) for funcionario in funcionarios]

def menu():
    print("[1] Cadastrar novo funcionário")
    print("[2] Pesquisar Funcionário")
    print("[3] Cadastar novo telefone")
    print('[4] Editar dados do funcionário')
    print("[0] Sair.")

menu()
opc = int(input('Escolha uma opção acima: '))

while opc != 0:
    if opc == 1:
        cadastrarFuncionario()
        [print(funcionario) for funcionario in funcionarios]
        break
    elif opc == 2:
        print('Pesquisar Funcionário.')
        cpf = input('Informe um CPF: ')
        PesquisarFunc(cpf)
        break
    elif opc == 3:
        print('Cadastar novo telefone.')
        cpf = input('Informe um CPF: ')
        telefone = int(input('Informe um telefone para adicionar: '))
        addTel(cpf, telefone)
        break
    elif opc == 4:
        print('Editar dados do funcionário.')
        break
    else:
        print('Opção inválida!')
        break

