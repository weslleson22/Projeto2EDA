

f = open("file.txt",'r')
texto = f.readlines()

x = 0

while x < len(texto):
    if texto[x] == "\n":
        local = texto.index(texto[x])
        texto.pop(local)
    else:
        texto[x] = texto[x].split(',')
        x += 1

# Esse for abaixo aqui é só para tirar o "\n" em algumas strings, é opcional.

for i in linha:
    local = linha.index(i) # Local do i em texto
    for b in i:
        local2 = linha[local].index(b) # Local2 do b em i ( local )
        if "\n" in b:
            texto[local][local2] = b.replace("\n",'') # Substitui o valor de acordo com "local" e "local2"

lista1, lista2 = texto
print("lista1 =",lista1)
print("lista2 =",lista2)








import numpy as np


def read_file(string,method):
    string = str(string)
    method = str(method)
    with open(string,method) as file:
        content = []
        for line in file:
            content.append(line.replace('\n',''))
        file.close()
        graph_type = content[0]
        del(content[0])
        print(content)
    return content, graph_type

def split_vertex(content):
    vertex = []
    for element in content:
        vertex += element.split(',')
    vertex = list(set(vertex))
    vertex.sort()
    return vertex

def get_position(vertex,list_vertex):
    for i in range(len(list_vertex)):
        if list_vertex[i] == vertex:
            return i
    return -1

def set_vertex(matrix,edges,list_vertex):
    for edge in edges:
        vertex = edge.split(',')
        i , j = get_position(vertex[0], list_vertex),get_position(vertex[1], list_vertex)
        print(i,j)
       
        matrix[i][j]=1           
    if matrix[i][j]==1:
        print("A MATRIZ É ADJACENTE")  
        print(matrix) 
    else:
            print('Não é matriz adjacente')
    


file_name = "matriz.txt"
method = "r"

edges, graph_type = read_file(file_name, method)

list_vertex = split_vertex(edges)
num_vertex = len(list_vertex)
matrix = np.zeros((num_vertex,num_vertex), dtype=np.int)
set_vertex(matrix, edges, list_vertex)
            
            
print(list_vertex)


def menu():
    from time import sleep
    print('=-=' * 10)

    opção = 0
    while opção != 5:
        print('=-=' * 10)
        print('''
        [1] Apresentar se são ou não adjacentes
        [2] Calcular o grau de um vértice qualquer
        [3] Buscar todos os vizinhos de vértice qualquer
        [4] Visitar todas as arestas do grafo
        [5] sair do programa''')
        opção = int(input('>>>> Qual é sua opção? '))
        if opção == 1:
            print('-')
            
            matrix = np.zeros((num_vertex,num_vertex), dtype=np.int)
            set_vertex(matrix, edges, list_vertex)
            
            
        elif opção == 2:
            print('-')
        
        elif opção == 3:
            print('-')

        elif opção == 4:
            print('-')

        elif opção == 5:
            print('Finalizando...')
            
        else:
            print('Opção inválida. Tente novamente.')
        print('=-=' * 10)
        sleep(3)
    print('Fim do programa! Volte sempre!')

menu()
        