from Graph import Graph
from graphviz import Digraph
from queue import PriorityQueue
from math import inf
import tempfile

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


if __name__ == '__main__':

    '''
        Capitais centro-oeste: Brasilia, Goiania, Cuiaba, Campo Grande.
        Capitais Sudeste: São Paulo, Rio de Janeiro, Vitoria, Belo Horizonte

    '''
    g = Graph({})

    '''

        Fonte distancias estradas: https://www.distanciaentreascidades.com.br/distancia-de-rio-de-janeiro-ate-vitoria-espirito-santo-brazil

    '''

    edges = [   ('Cuiaba - MT', 'Goiania - GO', 895), 
                ('Cuiaba - MT', 'Campo Grande - MS', 707),

                ('Goiania - GO', 'Campo Grande - MS', 846), 
                ('Goiania - GO', 'Belo Horizonte - MG', 890), 

                ('Campo Grande - MG', 'Sao Paulo - SP', 1013), 

                ('Sao Paulo - SP', 'Rio de Janeiro - RJ', 441), 
                ('Sao Paulo - SP', 'Belo Horizonte - MG', 592), 

                ('Belo Horizonte - MG', 'Vitoria - ES', 523), 

                ('Rio de Janeiro - RJ', 'Vitoria - ES', 527)]

    graf = Digraph('Graf', filename='graf', node_attr={'color': 'lightblue2'}, engine='sfdp')
    graf.attr(size='100', shape='ellipse', fontsize='10', rankdir='LR')
    graf.attr('node', shape='doublecircle')

    grafCaminho = Digraph('Graf', filename='graf', node_attr={'color': 'lightblue2'}, engine='sfdp')
    grafCaminho.attr(size='100', shape='ellipse', fontsize='10', rankdir='LR')
    grafCaminho.attr('node', shape='doublecircle')

    for e in edges:
        graf.edge(e[0], e[1], label=str(e[2]), color='black', constraint='false',dir='none')

    for e in edges:
        g.add_edge(*e)

    # Aqui coloca-se o Nó de inicio;
    partidaInicial = 'Cuiaba - MT'
    # Aqui coloca-se as paradas a serem feitas, na ordem a serem realizadas;
    parada = [ 'Belo Horizonte - MG', 'Sao Paulo - SP', 'Rio de Janeiro - RJ']

    partida = partidaInicial
    distanciaTotal = 0
    visitados = []
    caminhoPercorrido = []

    # caminho de a ate g passando por d

    print("Visitados: ", visitados)

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

    print("listCaminho", listCaminho)

    for e in edges:
        grafCaminho.edge(e[0], e[1], label=str(e[2]), color='black', constraint='false',dir='none')


    for e in range(0, len(listCaminho) - 1):
        if e == len(listCaminho) - 2:
            grafCaminho.edge(listCaminho[e], listCaminho[e + 1], label=str(distanciaTotal), color='red', constraint='true')
        else:
            grafCaminho.edge(listCaminho[e], listCaminho[e + 1], color='red', constraint='false')

    grafCaminho.view(tempfile.mktemp('.gv')) 
