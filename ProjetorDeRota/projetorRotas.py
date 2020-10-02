from Graph import Graph
import tempfile
from menu import menu
from funcoes import dijkstra, imagem_mapa
from graphviz import Digraph


if __name__ == '__main__':
    edges = menu()

    '''
        Capitais centro-oeste: Brasilia, Goiania, Cuiaba, Campo Grande.
        Capitais Sudeste: São Paulo, Rio de Janeiro, Vitoria, Belo Horizonte

    '''
    g = Graph({})

    '''

        Fonte distancias estradas: https://www.distanciaentreascidades.com.br/distancia-de-rio-de-janeiro-ate-vitoria-espirito-santo-brazil

    '''


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

    # grafCaminho.view(tempfile.mktemp('.gv'))
    grafCaminho.format= 'svg'
    grafCaminho.view()