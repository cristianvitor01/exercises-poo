veiculos={"BCC009":{"marca":"Fiat", "modelo":"UNO", "ano":"2003", 
                    "placa":"BCC009", "chassi":"36563652", "cor":"Branco","km":500},
         "BCC006":{"marca":"Fiat", "modelo":"Toro", "ano":"2003", 
                   "placa":"BCC006", "chassi":"36563652","cor":"Branco","km":500},
         "BCC008":{"marca":"Fiat", "modelo":"Argo", "ano":"2003", 
                   "placa":"BCC007", "chassi":"36563652","cor":"Branco","km":500}  }

motoristas={"11111":{"nome":"François", "CPF":"11111", "RG":"223212", "CNH":"34221"},
            "22222":{"nome":"Ana", "CPF":"22222", "RG":"223212", "CNH":"34221"},
            "33333":{"nome":"MAria", "CPF":"33333", "RG":"223212", "CNH":"34221"}}

viagens={1:{"destino":"Bacabal", 
                "origem":"Caxias", 
                "distância":200.0, 
                "motorista":motoristas["11111"], 
                "veiculo":veiculos["BCC009"]},
         2:{"destino":"Bacabel", 
                "origem":"Caxias", 
                "distância":200.0, 
                "motorista":motoristas["11111"], 
                "veiculo":veiculos["BCC009"]
               }}

manutencoes ={1:{"veiculo":veiculos["BCC009"],"data":"02-02-2023", "tipo":"preventiva","custo":1000.0},
              2:{"veiculo":veiculos["BCC009"],"data":"02-02-2023", "tipo":"preventiva","custo":1000.0} }

abastecimentos={1:{"veiculo":veiculos["BCC009"],"valor":400.0,"data":"4-2-2023","quantidade":150},
               2:{"veiculo":veiculos["BCC009"],"valor":400.0,"data":"4-2-2023","quantidade":150},
               3:{"veiculo":veiculos["BCC009"],"valor":400.0,"data":"4-2-2023","quantidade":150},}



def cadastrar_novo_motorista(cod, nome, cpf, rg, cnh):
    motoristas.update({
        cod: {
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "cnh": cnh,
        }
    })
    print()
    print('Motorista cadastrado!')
    print(motoristas)


def pesquisar_motorista(cod):
    encontrado = False
    for k, v in motoristas.items():
        if k == cod:
            print()
            print('Motorista encontrado: ')
            print()
            print(k, v)
            encontrado = True
            break
    if not encontrado:
        print('Motorista não encontrado.')


def editar_motorista(cod, **kwargs):
    pass


def deletar_motorista(cod):
    pesquisar_motorista(cod)
    motoristas.pop(cod)

    print()
    print('Motorista deletado!')
    print(motoristas)

def cadastrar_veic(placa, marca, modelo, ano, placa, chassi, cor, km):
    veiculos.update({
        placa: {
            "marca": marca,
            "modelo": modelo,
            "ano": ano,
            "placa": placa,
            "chassi": chassi,
            "cor": placa,
            "km": km,
        }
    })
    print()
    print('Veículo cadastrado!')
    print(veiculos)

def pesquisar_veic(placa):
    encontrado = False
    for k, v in veiculos.items():
        if k == placa:
            print()
            print('Veículo encontrado: ')
            print()
            print(k, v)
            encontrado = True
            break
    if not encontrado:
        print('Veículo não encontrado.')

def editar_veic():
    pass

def deletar_veic():
    pass

def ver_km():
    pass

def cadastrar_viagem():
    pass

def editar_viagem():
    pass

def registrar_abastecimento():
    pass

def registrar_manut():
    pass

def menu():
    print("[1] Cadastrar Novo Motorista")
    print("[2] Pesquisar Motorista")
    print("[3] Editar Motorista")
    print('[4] Deletar Motorista')
    print('[5] Cadastrar Veículo')
    print('[6] Pesquisar Veículo')
    print('[7] Editar Veículo')
    print('[8] Deletar Veículo')
    print('[10] Ver quilomentragem do veículo')
    print('[11] Cadastar Viagem')
    print('[12] Editar Viagem')
    print('[13] Registrar Abastecimento')
    print('[14] Registrar Manutenção')
    print('[15] Relatório')
    print("[0] Sair.")

menu()
opc = int(input('Escolha uma opção acima: '))

while opc != 0:
    if opc == 1:
        cod = int(input('COD:'))
        nome = input('Nome: ')
        cpf = input('CPF: ')
        rg = input('RG: ')
        cnh = int(input('CNH: '))
        cadastrar_novo_motorista(cod, nome, cpf, rg, cnh)
        break
    elif opc == 2:
        print('Pesquisar Motorista.')
        cod = input('Informe o CPF/COD: ')
        pesquisar_motorista(cod)
        break
    elif opc == 3:
        print('Editar Motorista.')
        break
    elif opc == 4:
        print('Deletar Motorista.')
        cod = input('Informe o CPF/COD: ')
        deletar_motorista(cod)
        break
    elif opc == 5:
        print('Cadastrar Veículo')
        pass
        break
    elif opc == 6:
        print('Pesquisar Veículo')
        pass
        break
    elif opc == 7:
        print('Editar Veículo')
        pass
        break
    elif opc == 8:
        print('Deletar Veículo')
        pass
        break
    elif opc == 9:
        print('Ver quilometragem de Veículo')
        pass
        break
    else:
        print('Opção inválida!')
        break