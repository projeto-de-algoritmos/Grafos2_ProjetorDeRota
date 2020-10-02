def criar_mapa():
    qtd_cidade = 0
    while(qtd_cidade <= 0):
        qtd_cidade = int(input("Quantidade de cidades: " ))
    
    mapa = []

    for i in range(qtd_cidade):
        nome_cidade = input("Nome da cidade: " )
        qtd_vizinhos = 0
        while(qtd_vizinhos <= 0):
            qtd_vizinhos = int(input("Numero de cidades vizinhas: " ))

        for j in range(qtd_vizinhos):
            nome_vizinho, distancia = input("Nome da cidade(vizinha) e a distancia: ").split()
            mapa.append((nome_cidade, nome_vizinho, distancia))

    
    