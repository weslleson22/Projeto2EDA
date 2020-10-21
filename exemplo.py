import random
import time
from datetime import datetime
import csv
start_time = datetime.now()


f = open("file.txt",'r')
linha = int(f.readline())

lista1=[]

for i in range (linha):
    lista1.append(random.randint(0,linha))


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                #irá trocar os itens i e j da lista. Sem o armazenamento temporário, um dos valores seria sobrescrito.
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#bubbleSort(lista1)
#print(lista1)

#Selection Sort 
for i in range(len(lista1)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(lista1)): 
        if lista1[min_idx] > lista1[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    lista1[i], lista1[min_idx] = lista1[min_idx], lista1[i] 
  
# Driver code to test above 

#print([i]),  
for i in range(len(lista1)): 
   # print(lista1[i]) 

    def insertionsort(lista1):
        # começamos o loop no segundo elemento (índice 1), uma vez que o primeiro item já está classificado
        for j in range(1,len(lista1)):
            key = lista1[j] #O próximo item que vamos inserir na seção classificada da matriz

            i = j-1 # o último item com o qual iremos comparar
            #agora continuamos movendo a chave para trás, desde que seja menor do que o último item da matriz
            while (i > -1) and key < lista1[i]: #if i == -1 significa que esta chave pertence ao início
                lista1[i+1]=lista1[i] #move o último objeto comparado uma etapa à frente para abrir espaço para a chave
                i=i-1#observe o próximo item para a próxima vez.
            #okay i não é maior que key significa que a key pertence a i + 1
            lista1[i+1] = key

       # print(lista1) 
        return lista1


#insertionsort(lista1)


tempo=end_time = datetime.now()
Duracao=format(end_time - start_time)
print('Duração de execução:',Duracao)
print(tempo)

