import random
import time
from datetime import datetime
class QuickSort:
        
    


            #####QuickSort#####################
    """ Implementaçao do algoritmo quick sort """

        
def swap(a_list, pos1, pos2):
    """ Troca a posição de dois itens em uma lista """
    temp = a_list[pos1]
    a_list[pos1] = a_list[pos2]
    a_list[pos2] = temp


def partition(a_list, start, end):
    """ Divide uma lista """
    pivot = a_list[start]
    while True:
        while a_list[start] < pivot:
            start = start + 1

        while a_list[end] > pivot:
            end = end - 1

        if start >= end:
            return end

        swap(a_list, start, end)

        start = start + 1
        end = end - 1


def quick_sortM(a_list, start, end):
    """ Algoritmo de quick sort """
    if start < end:
        part = partition(a_list, start, end)
        quick_sortM(a_list, start, part)
        quick_sortM(a_list, part + 1, end)

f = open("file.txt",'r')
linha = int(f.readline())
lista1=[]
          
            #lista melhor
for i in range (linha):
    lista1.append(random.randint(0,linha))


a=lista1
print("as",a)


        
    #a = [9, 8, 5, 7, 6, 2, 4, 3, 1]
    
quick_sortM(a, 0, len(a) - 1)
print(a)





#####QuickSort######################
    
    