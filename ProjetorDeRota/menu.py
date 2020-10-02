from funcoes import criar_mapa

edges = [   ('Cuiaba - MT', 'Goiania - GO', 895), 
            ('Cuiaba - MT', 'Campo Grande - MS', 707),

            ('Goiania - GO', 'Campo Grande - MS', 846), 
            ('Goiania - GO', 'Belo Horizonte - MG', 890), 

            ('Campo Grande - MG', 'Sao Paulo - SP', 1013), 

            ('Sao Paulo - SP', 'Rio de Janeiro - RJ', 441), 
            ('Sao Paulo - SP', 'Belo Horizonte - MG', 592), 

            ('Belo Horizonte - MG', 'Vitoria - ES', 523), 

            ('Rio de Janeiro - RJ', 'Vitoria - ES', 527)]

def menu():
    print("Bem-Vindo")
    print("O programa tem o objetivo de encontrar caminhos para um rally.")
    print("Mapa: ")
    print("1 - Para usar o mapa padrão")
    print("2 - Criar meu mapa")

    opcao = int(input("Digite a opção: "))

    if(opcao == 1 ):
        return edges
    
    elif (opcao == 2):
        criar_mapa()
        return []
    print(opcao)

print(menu())