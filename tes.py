
'''def Teste_RadixSort_melhor():
        import time
        from datetime import datetime
        start_time = datetime.now()
        radixSort = RadixSort()
        #print(lista1)
        print("Processando melhor caso do RadixSORT!")
        print("Processando melhor caso do RadixSORT!")
        radixSort.sort(lista1)
        
        #print(lista1)
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
def Teste_RadixSort_Pior():
        import time
        from datetime import datetime
        start_time = datetime.now()
        radixSort = RadixSort()
        #print(lista1)
        print("Processando melhor caso do RadixSORT!")
        print("Processando melhor caso do RadixSORT!")
        radixSort.sort(lista2)
        print(lista2)
        
        #print(lista1)
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
'''

import random


def selection_sort(array):
    '''
    :param array: List[Int] -- the python list being sorted
    '''
    ### Your code ###
    # traverse through all elements
    for n in range(len(array)):
        # find the minimum in remaining unsorted array
        m = min(array[n:])
        ### key consider duplicates and indexing ###
        i = array[n:].index(m)+n
        # (1) swap the minimum with the first unsorted element
        array[n], array[i] = array[i], array[n]
        # (2) move the minimum to the last sorted element
        # del array[i]
        # array.insert(n, m)
    return array



a= [ 9,8,2,0,4]zz