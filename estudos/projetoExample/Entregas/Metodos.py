def escolher_veiculo(veiculos, distancia, peso):
    for Veiculo in veiculos:
        if Veiculo.atende_requisitos(distancia, peso):
            return Veiculo.nome_modelo
    return None