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
    print(motoristas)


def pesquisar_motorista():
    pass

def editar_motorista():
    pass

def deletar_motorista():
    pass



def menu():
    print("[1] Cadastrar Novo Motorista")
    print("[2] Pesquisar Motorista")
    print("[3] Editar Motorista")
    print('[4] Deletar Motorista')
    print('[4] Cadastrar Veículo')
    print('[4] Pesquisar Veículo')
    print('[4] Editar Veículo')
    print('[4] Deletar Veículo')
    print('[4] Ver quilomentragem do veículo')
    print('[4] Cadastar Viagem')
    print('[4] Editar Viagem')
    print('[4] Registrar Abastecimento')
    print('[4] Registrar Manutenção')
    print('[4] Relatório')
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
        pass
        break
    elif opc == 3:
        pass
        break
    elif opc == 4:
        pass
        break
    else:
        print('Opção inválida!')
        break