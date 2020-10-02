import sys
import time
from funcoes import criar_mapa, imagem_mapa, busca_caminho


edges = [   ('Cuiaba - MT', 'Goiania - GO', 895), 
            ('Cuiaba - MT', 'Campo Grande - MS', 707),

            ('Goiania - GO', 'Campo Grande - MS', 846), 
            ('Goiania - GO', 'Belo Horizonte - MG', 890), 

            ('Campo Grande - MS', 'Sao Paulo - SP', 1013), 

            ('Sao Paulo - SP', 'Rio de Janeiro - RJ', 441), 
            ('Sao Paulo - SP', 'Belo Horizonte - MG', 592), 

            ('Belo Horizonte - MG', 'Vitoria - ES', 523), 

            ('Rio de Janeiro - RJ', 'Vitoria - ES', 527)]

def menu():
    print("Bem-Vindo")
    print("O programa tem o objetivo de encontrar caminhos em um mapa.")
    print("Mapa: ")
    print("1 - Para usar o mapa padrão")
    print("2 - Criar meu mapa")
    print("3 -Sair ")
    opcao = 0
    
    while(opcao <=0):
        
        opcao = int(input("Digite a opção: "))

        if(opcao == 1 ):
            imagem_mapa(edges)
            mapa = edges
        
        elif (opcao == 2):
            mapa = criar_mapa()
            imagem_mapa(mapa)
            
        elif (opcao == 3):
            print("Saindo...")
            # sys.exit()
        else:
            print("Opcao não invalida....")
            opcao = 0
    
    print('\n' * 100)
    print("--------------------------------------")
    print("Opcoes:")
    print("1- Buscar menor caminho até outra cidade")
    print("2- Buscar caminho passando por pontos")
    print("3- Buscar menor caminho para todos os pontos")
    opcao = 0
    while(opcao<=0 ):
        opcao = int(input("Digite: "))
        if(opcao == 1):
            inicio = input("Ponto de partida(cidade): ")
            final = input("Ponto final(cidade): ")
            
            busca_caminho(inicio,[final],mapa)

        
        elif (opcao == 2):
            pass
        elif(opcao == 3):
            pass
        else:
            opcao = 0

    time.sleep(100)

    return mapa