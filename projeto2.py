import random
import time
from datetime import datetime
import csv
start_time = datetime.now()


f = open("file.txt",'r')
linha = int(f.readline())
lista1=[]
lista2=[]
#lista melhor
for i in range (linha):
    lista1.append(random.randint(0,linha))
#print(lista1)
#lista pior
for i in range (linha):
    lista2.append(random.randint(0,linha))



def testBubbleSort(): 
    #Função de ordenação 1 BublleSort
    def bubbleSortmelhor(alist):
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if alist[i]>alist[i+1]:
                    #irá trocar os itens i e j da lista. Sem o armazenamento temporário, um dos valores seria sobrescrito.
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
   

    from datetime import datetime
    bubbleSortmelhor(lista1)
    print(lista1)

   
    Duracao = end_time = datetime.now()
    Duracao=format(end_time - start_time)

    datahora=datetime.now()
    print(datahora,"melhor caso:",Duracao)

    import datetime
    now = datetime.datetime.now()
    data = now.strftime("%d/%m/%y")
    time = now.strftime("%H:%M:%S")
    print(data,time,Duracao)
    import psutil
    # physical memory usage
    memoria = psutil.virtual_memory()
    me=str(memoria[0])
    print(me)
    


    fh = open("result.csv","w") 
    linhas_de_texto = ["Data :",data," Hora ",time," bubblesort"," Melhor caso ",Duracao," memoria Ram ",me];
    linhas_de_texto1 = ["Data :",data," Hora ",time," bubblesort"," Melhor caso ",Duracao," memoria Ram ",me];
    fh.writelines(linhas_de_texto) 
    fh.writelines(linhas_de_texto1) 

    fh.close()



#testBubbleSort()

meuArquivo = open('file.txt')
tlinhas = (meuArquivo.readlines())


a="bubblesort"
b="insertiorsort"
c="selectionsort"
d="merge"
if tlinhas[1] == a:
    print('bubblesort')
    testBubbleSort()
elif tlinhas[1] == b:
    print('insertiorsort')
elif tlinhas[1] == c:
    print('selectionsort')
else:
    print('Não existe essa função de ordenação')