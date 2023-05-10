class Motorista:
    def __init__(self, nome, cpf, rg, cnh)
    self.nome = nome
    self.cpf = cpf
    self.rg = rg 
    self.cnh = cnh

    def cadastrar_novo_motorista(self, nome, cpf, rg, cnh):
        pass

    def pesquisar_motorista(cpf):
        pass

    def editar_motorista(cpf):
        pass

    def deletar_motorista(cpf):
        pass


class Veiculo:
    def __init__(self, placa, marca, modelo, ano, chassi, cor, km)
    self.placa = placa
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.chassi = chassi
    self.cor = cor 
    self.km = km

    def cadastrar_veic(placa, marca, modelo, ano, placa, chassi, cor, km):
        pass

    def pesquisar_veic(placa):
        pass

    def editar_veic():
        pass

    def deletar_veic():
        pass

    def ver_km():
        pass

class Viagens:
    def __init__(self, id, destino, origem, distancia)
    self.id = id 
    self.destino = destino
    self.origem = origem
    self.distancia = distancia

    def cadastrar_viagem():
        pass

    def editar_viagem():
        pass


class Manutencoes:
    def __init__(self, id, veiculo, data, tipo, custo)
    self.id = id 
    self.veiculo = veiculo
    self.data = data
    self.tipo = tipo
    self.custo = custo

    def registrar_manutencao():
        pass

class Abastecimento:
    def __init__(self, id, veiculo, valor, data, quantidade)
    self.id = id 
    self.veiculo = veiculo
    self.valor = valor
    self.data = data
    self.quantidade = quantidade

    def registrar_abastecimento():
        pass