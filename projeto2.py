import random
import time
from datetime import datetime
import csv

from HeapSort import HeapSort


start_time = datetime.now()
#Fazendo a leitura do arquivo txt
f = open("file.txt",'r')
linha = int(f.readline())


lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]
#lista melhor
for i in range (linha):
    lista1.append(random.randint(0,linha))

#lista pior
for i in range (linha):
    lista2.append(random.randint(0,linha))




def Teste_HeapSort_Melhor():
        import time
        from datetime import datetime
        start_time = datetime.now()
        
        heapSort = HeapSort()
        
        print("Processando melhor caso do HEAPSORT!")
        print("Processando melhor caso do HEAPSORT!")
        
        heapSort.sort(lista1)
        
        print('--'*20)
        #print(lista1)
        from datetime import datetime
        Duracao = end_time = datetime.now()
        Duracao=format(end_time - start_time)

        datahora=datetime.now()
                #print(datahora,"melhor caso:",Duracao)

        import datetime

        now = datetime.datetime.now()
        data = now.strftime("%d/%m/%y")
        time = now.strftime("%H:%M:%S")

        import psutil
                # physical memory usage
        memoria = psutil.virtual_memory()
        me=str(memoria[3])
        print("Data :",data," Hora ",time,"HeapSort","Tamanho do vetor",linha," melhor caso ",Duracao," memoria Ram ",me)




        with open('dados_gerados.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Data :",data," Hora ",time,"HeapSort","Tamanho do vetor",linha," melhor caso ",Duracao," memoria Ram ",me])
            #writer.writerow(["Data :",data1," Hora ",time1," bubblesort","Tamanho do vetor",linha," Melhor pior ",Duracao1," memoria Ram ",me1])                   
            file.close()




    
def Teste_HeapSort_Pior():
        print("Concluirdo com Sucesso!")
        import time
        from datetime import datetime
        start_time = datetime.now()
        #print(lista2)
        heapSort = HeapSort()
       
        print("Processando Pior caso do HEAPSORT!")
        print("Processando Pior caso do HEAPSORT!")
        heapSort.sortpior(lista2)
        #print(lista2)  
        print('--'*20)
        print('-pior-'*20)

       
        from datetime import datetime
        Duracao = end_time = datetime.now()
        Duracao=format(end_time - start_time)

        datahora=datetime.now()
                #print(datahora,"melhor caso:",Duracao)

        import datetime

        now = datetime.datetime.now()
        data = now.strftime("%d/%m/%y")
        time = now.strftime("%H:%M:%S")

        import psutil
                # physical memory usage
        memoria = psutil.virtual_memory()
        me=str(memoria[3])
        print("Data :",data," Hora ",time,"HeapSort","Tamanho do vetor",linha," Pior caso ",Duracao," memoria Ram ",me)

        with open('dados_gerados.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["Data :",data," Hora ",time,"HeapSort","Tamanho do vetor",linha," Pior caso ",Duracao," memoria Ram ",me])
            #writer.writerow(["Data :",data1," Hora ",time1," bubblesort","Tamanho do vetor",linha," Melhor pior ",Duracao1," memoria Ram ",me1])
                    
            file.close()




    #lista rando

def salvarbubblesortP():

        def bubbleSortpior(alist):
            for passnum in range(len(alist)-1,0,-1):
                for i in range(passnum):
                    #verificar se os elementos estão na ordem certa
                    if alist[i]<alist[i+1]:
                        #irá trocar os itens i e j da lista. Sem o armazenamento temporário, um dos valores seria sobrescrito.
                        temp = alist[i]
                        alist[i] = alist[i+1]
                        alist[i+1] = temp

            

       # print("Gerando Pior Caso\n"*3)
        #print("Por Favor espero o procesamento!\n"*3)
        bubbleSortpior(lista2)
        print("Geração do Pior Caso\n"*3)

       #print(lista2)
        print("Concluido Obrigado por espera")
        
        
        from datetime import datetime
        Duracao = end_time = datetime.now()
        Duracao=format(end_time - start_time)

        datahora=datetime.now()
        #print(datahora,"melhor caso:",Duracao)

        import datetime
        now = datetime.datetime.now()
        data = now.strftime("%d/%m/%y")
        time = now.strftime("%H:%M:%S")
        #print(data,time,linha,Duracao)
        import psutil
        # physical memory usage
        memoria = psutil.virtual_memory()
        me=str(memoria[3])
        
        with open('dados_gerados.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["Data :",data," Hora ",time," bubblesort","Tamanho do vetor",linha," Pior caso ",Duracao," memoria Ram ",me])
            #writer.writerow(["Data :",data1," Hora ",time1," bubblesort","Tamanho do vetor",linha," Melhor pior ",Duracao1," memoria Ram ",me1])
            
            file.close()







#print("Gerando o Melhor Caso\n"*3)
#print("Por Favor espero o procesamento!\n"*3)  

    #Função de ordenação 1 BublleSort
def bubbleSortmelhor(alist):
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if alist[i]>alist[i+1]:
                    #irá trocar os itens i e j da lista. Sem o armazenamento temporário, um dos valores seria sobrescrito.
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp

#bubbleSortmelhor(lista1)
#print(lista1)
print("Concluido Obrigado por espera")

def salvarbubblesortM():

  
    
    from datetime import datetime
    Duracao = end_time = datetime.now()
    Duracao=format(end_time - start_time)

    datahora=datetime.now()
    #print(datahora,"melhor caso:",Duracao)

    import datetime
    now = datetime.datetime.now()
    data = now.strftime("%d/%m/%y")
    time = now.strftime("%H:%M:%S")
    #clsprint(data,time,linha,Duracao)
    import psutil
    # physical memory usage
    memoria = psutil.virtual_memory()
    me=str(memoria[3])
    
    with open('dados_gerados.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Data :",data," Hora ",time," bubblesort","Tamanho do vetor",linha," Melhor caso ",Duracao," memoria Ram ",me])
        #writer.writerow(["Data :",data1," Hora ",time1," bubblesort","Tamanho do vetor",linha," Melhor pior ",Duracao1," memoria Ram ",me1])
           
        file.close()
salvarbubblesortM()
salvarbubblesortP()
  
#testBubbleSort()


def InsertionSortM(lista1):
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

         
        return lista1
def InsertionSortMelhor():
    print("Processando melhor caso do INSERTIONSORT!")
    print("Processando melhor caso do iNSERTIONSORT!")
   # print(lista1)
    InsertionSortM(lista1)
    #print(lista1)
    
    from datetime import datetime
    Duracao = end_time = datetime.now()
    Duracao=format(end_time - start_time)

    datahora=datetime.now()
                #print(datahora,"melhor caso:",Duracao)

    import datetime

    now = datetime.datetime.now()
    data = now.strftime("%d/%m/%y")
    time = now.strftime("%H:%M:%S")

    import psutil
                # physical memory usage
    memoria = psutil.virtual_memory()
    me=str(memoria[3])
    print("Data :",data," Hora ",time,"InsertionSort","Tamanho do vetor",linha," Melhor caso ",Duracao," memoria Ram ",me)

    with open('dados_gerados.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Data :",data," Hora ",time,"InsertionSort","Tamanho do vetor",linha," Melhor caso ",Duracao," memoria Ram ",me])
            #writer.writerow(["Data :",data1," Hora ",time1," bubblesort","Tamanho do vetor",linha," Melhor pior ",Duracao1," memoria Ram ",me1])
                    
        file.close()
    

#InsertionSortMelhor()
##pior caso Insertion sort###
def InsertionSortP(lista1):
        # começamos o loop no segundo elemento (índice 1), uma vez que o primeiro item já está classificado
        for j in range(1,len(lista1)):
            key = lista1[j] #O próximo item que vamos inserir na seção classificada da matriz

            i = j-1 # o último item com o qual iremos comparar
            #agora continuamos movendo a chave para trás, desde que seja menor do que o último item da matriz
            while (i > -1) and key > lista1[i]: #if i == -1 significa que esta chave pertence ao início
                lista1[i+1]=lista1[i] #move o último objeto comparado uma etapa à frente para abrir espaço para a chave
                i=i-1#observe o próximo item para a próxima vez.
            #okay i não é maior que key significa que a key pertence a i + 1
            lista1[i+1] = key

         
        return lista1
def InsertionSortPior():
    print("Processando Pior caso do INSERTIONSORT!")
    print("Processando Pior caso do iNSERTIONSORT!")
   # print(lista1)
    InsertionSortP(lista2)
  #  print(lista1)
    
    from datetime import datetime
    Duracao = end_time = datetime.now()
    Duracao=format(end_time - start_time)

    datahora=datetime.now()
                #print(datahora,"melhor caso:",Duracao)

    import datetime

    now = datetime.datetime.now()
    data = now.strftime("%d/%m/%y")
    time = now.strftime("%H:%M:%S")

    import psutil
                # physical memory usage
    memoria = psutil.virtual_memory()
    me=str(memoria[3])
    print("Data :",data," Hora ",time,"InsertionSort","Tamanho do vetor",linha," Pior caso ",Duracao," memoria Ram ",me)

    with open('dados_gerados.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Data :",data," Hora ",time,"InsertionSort","Tamanho do vetor",linha," Pior caso ",Duracao," memoria Ram ",me])
            #writer.writerow(["Data :",data1," Hora ",time1," bubblesort","Tamanho do vetor",linha," Melhor pior ",Duracao1," memoria Ram ",me1])
                    
        file.close()
    











#####SHELLSOR#####################
def shellSort(nums):
    h = 1
    n = len(nums)
    while h > 0:
            for i in range(h, n):
                c = nums[i]
                j = i
                while j >= h and c < nums[j - h]:
                    nums[j] = nums[j - h]
                    j = j - h
                    nums[j] = c
            h = int(h / 2.2)
    return nums

def ShellsortMelhor():
    print("Processando melhor caso do SHELLSORT!")
    print("Processando melhor caso do SHELLSORT!")
    
    shellSort(lista1)
    from datetime import datetime
    Duracao = end_time = datetime.now()
    Duracao=format(end_time - start_time)

    datahora=datetime.now()
                #print(datahora,"melhor caso:",Duracao)

    import datetime

    now = datetime.datetime.now()
    data = now.strftime("%d/%m/%y")
    time = now.strftime("%H:%M:%S")

    import psutil
                # physical memory usage
    memoria = psutil.virtual_memory()
    me=str(memoria[3])
    print("Data :",data," Hora ",time,"InsertionSort","Tamanho do vetor",linha," Melhor caso ",Duracao," memoria Ram ",me)

    with open('dados_gerados.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Data :",data," Hora ",time,"ShellSort","Tamanho do vetor",linha," Melhor caso ",Duracao," memoria Ram ",me])
            #writer.writerow(["Data :",data1," Hora ",time1," bubblesort","Tamanho do vetor",linha," Melhor pior ",Duracao1," memoria Ram ",me1])
                    
        file.close()
    
    
    0#ShellsortMelhor()
#####TESTE PIOR CASO########################33
''' Basicamente o algoritmo passa várias vezes pela lista dividindo o grupo maior em menores. 
Nos grupos menores é aplicado o método da ordenação por inserção. Implementações do algoritmo
'''
def shellSortP(nums):
    h = 1
    n = len(nums)
    while h > 0:
            for i in range(h, n):
                c = nums[i]
                j = i
                while j >= h and c > nums[j - h]:
                    nums[j] = nums[j - h]
                    j = j - h
                    nums[j] = c
            h = int(h / 2.2)
    return nums
start_time = datetime.now()
def ShellsortPior():
    print("Processando PIOR caso do SHELLSORT!")
    print("Processando PIOR caso do SHELLSORT!")
    #print(lista2)
    shellSortP(lista2)
    #print(lista2)
    from datetime import datetime
    Duracao = end_time = datetime.now()
    Duracao=format(end_time - start_time)

    datahora=datetime.now()
                #print(datahora,"melhor caso:",Duracao)

    import datetime

    now = datetime.datetime.now()
    data = now.strftime("%d/%m/%y")
    time = now.strftime("%H:%M:%S")

    import psutil
                # physical memory usage
    memoria = psutil.virtual_memory()
    me=str(memoria[3])
    print("Data :",data," Hora ",time,"ShellSort","Tamanho do vetor",linha," Pior caso ",Duracao," memoria Ram ",me)

    with open('dados_gerados.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Data :",data," Hora ",time,"ShellSort","Tamanho do vetor",linha," Pior caso ",Duracao," memoria Ram ",me])
            #writer.writerow(["Data :",data1," Hora ",time1," bubblesort","Tamanho do vetor",linha," Melhor pior ",Duracao1," memoria Ram ",me1])
                    
        file.close()


#####SHELLSORT######################
    


meuArquivo = open('file.txt','r')
tlinhas = (meuArquivo.readlines())


a="insertion"
b="heapsort"
c="shellsort"
d="bublle"


if tlinhas[1] == a:
    print('insertionsort')
    #salvarbubblesortP()
    #salvarbubblesortM()
    print("espero por favor o melhor caso!")
    InsertionSortMelhor()
    print("espero por favor o Pior caso!")
    InsertionSortPior()

elif tlinhas[1] == b:
    print('HeapSortt')
    #insertionsortmelhor(lista1)
    #salvarInsetionsort()
    print("espero por favor o melhor caso!")
    Teste_HeapSort_Melhor()
    print("espero por favor o Pior caso!")
    Teste_HeapSort_Pior()
elif tlinhas[1] == c:
    print('shellSort')
    print("espero por favor o melhor caso!")
    ShellsortMelhor()
     
    print("espero por favor o Pior caso!")
    ShellsortPior()
elif tlinhas[1] == d:
    print('BublleSort')
    print("espero por favor o melhor caso!")
    salvarbubblesortM()
     
    print("espero por favor o Pior caso!")
    salvarbubblesortP()
   
   

else:
    print('Não existe essa função de ordenação')