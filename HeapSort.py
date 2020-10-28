
class HeapSort:

    import time
    from datetime import datetime
    start_time = datetime.now()
    def heapify(self, array, n, i):
         #Seja i o índice de um dado elemento da heap. Podem ser facilmente encontradas referências aos
        # elementos a ele conectados (pai e filhos) através das seguintes relações:
        maior = i
        l = 2 * i + 1#direita 
        r = 2 * i + 2#esqueda
        #Onde i é o inde atual, e o resulta da operação é o índice desejado

        if l < n and array[i] < array[l]:
            maior = l

        if r < n and array[maior] < array[r]:
            maior = r

        if maior != i:
            array[i], array[maior] = array[maior], array[i]
            self.heapify(array, n, maior)


    def sort(self, array):
        n = len(array)

        for i in range(n, -1, -1):
            self.heapify(array, n, i)

        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)

    def heapifypior(self, array, n, i):
        maior = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and array[i] > array[l]:
            maior = l

        if r < n and array[maior] > array[r]:
            maior = r

        if maior != i:
            array[i], array[maior] = array[maior], array[i]
            self.heapifypior(array, n, maior)


    def sortpior(self, array):
        n = len(array)

        for i in range(n, -1, -1):
            self.heapifypior(array, n, i)

        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapifypior(array, i, 0)
    
   