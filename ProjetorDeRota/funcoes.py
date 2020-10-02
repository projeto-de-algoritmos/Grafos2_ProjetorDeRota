from queue import PriorityQueue
from math import inf
from graphviz import Digraph
from Graph import Graph


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

    return mapa

def dijkstra(graph, raiz):
    fila = PriorityQueue()  
    caminho = {}  
    for v in graph.vertices():
        if v == raiz:
            caminho[v] = [[], 0]  
        else:
            caminho[v] = [[], inf]  

        fila.put((caminho[v][1], v))  

    remanescentes_vertices = list(graph.vertices()) 

    for i in range(len(graph.vertices())):
        u = fila.get()[1]  
        remanescentes_vertices.remove(u) 

        for v in remanescentes_vertices:  
            du = caminho[u][1] 
            w = graph.direct_cost(u, v) 
            dv = caminho[v][1]  
            if du + w < dv:  
                caminho[v][1] = du + w  
                caminho[v][0] = caminho[u][0] + [u]  
                fila.queue.remove((dv, v)) 
                fila.put((caminho[v][1], v))

    return caminho

def imagem_mapa(e):
    mapa = Digraph('mapa', filename='mapa', node_attr={'color': 'lightblue2'}, engine='sfdp')
    mapa.attr(size='100', shape='ellipse', fontsize='10', rankdir='LR')
    mapa.attr('node', shape='doublecircle')

    for i in e:
        mapa.edge(i[0], i[1], label=str(i[2]), color='black', constraint='false',dir='none')
    
    mapa.format = 'svg'
    mapa.view()
    
    input("Pressione enter para continuar...")

def busca_caminho(partida, parada, mapa):
    print("Busca caminho")
    g = Graph({})
    for e in mapa:
        g.add_edge(*e)
    
    distanciaTotal = 0
    visitados = []
    caminhoPercorrido = []
    for i in parada:
        distance = dijkstra(g, partida)
        visitados.append(partida)
        partida = i
        caminhoPercorrido.append(distance[i][0])
        distanciaTotal += int(distance[i][1])
    
    visitados.append(partida)
    caminhoPercorrido.append(parada[-1:])

    for g in caminhoPercorrido:
            print("\n caminhoPercorrido lista macro: ", g)

    listCaminho = []
    for g in caminhoPercorrido:
        for h in g:
            listCaminho.append(h)
            print("\n caminhoPercorrido lista: ", h)

    pass