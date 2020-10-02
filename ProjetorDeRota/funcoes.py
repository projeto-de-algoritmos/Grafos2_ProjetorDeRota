from queue import PriorityQueue
from math import inf
from graphviz import Digraph


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

def dijkstra(graph, root):
    queue = PriorityQueue()  
    path = {}  
    for v in graph.vertices():
        if v == root:
            path[v] = [[], 0]  
        else:
            path[v] = [[], inf]  

        queue.put((path[v][1], v))  

    remaing_vertices = list(graph.vertices()) 

    for i in range(len(graph.vertices())):
        u = queue.get()[1]  
        remaing_vertices.remove(u) 

        for v in remaing_vertices:  
            du = path[u][1] 
            w = graph.direct_cost(u, v) 
            dv = path[v][1]  
            if du + w < dv:  
                path[v][1] = du + w  
                path[v][0] = path[u][0] + [u]  
                queue.queue.remove((dv, v)) 
                queue.put((path[v][1], v))

    return path

def imagem_mapa(e):
    mapa = Digraph('mapa', filename='mapa', node_attr={'color': 'lightblue2'}, engine='sfdp')
    mapa.attr(size='100', shape='ellipse', fontsize='10', rankdir='LR')
    mapa.attr('node', shape='doublecircle')

    for i in e:
        mapa.edge(i[0], i[1], label=str(i[2]), color='black', constraint='false',dir='none')
    
    mapa.format = 'svg'
    mapa.view()
    
    input("Pressione enter para continuar...")
