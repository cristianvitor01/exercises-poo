funcionarios = [
    {
        "nome": "cristian",
        "cpf": "111111",
        "cargo": "devpleno",
        "salario": "8000",
        "telefones": [159159, 148148, 126126],
    },
    {
        "nome": "func2",
        "cpf": "22222",
        "cargo": "func",
        "salario": "1000",
        "telefones": [11111, 22222, 22222],
    }
]


def PesquisarFunc(cpf):
    for f in funcionarios:
        if f['cpf'] == cpf:
            for k, v in f.items():
                print(k, v)
        else:
            print('Funcionario não encontrado.')



cpf = input('Informe um cpf: ')
PesquisarFunc(cpf)

