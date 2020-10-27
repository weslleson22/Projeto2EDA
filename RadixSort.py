class RadixSort:
    def radix(self, array, exp1):
        n = len(array)
        saida = [0] * (n)
        contador = [0] * (10)

        for i in range(0, n):
            indice = (array[i] // exp1)
            contador[(indice) % 10] += 1

        for i in range(1, 10):
            contador[i] += contador[i - 1]

        i = n - 1
        while i >= 0:
            indice = (array[i] // exp1)
            saida[contador[(indice) % 10] - 1] = array[i]
            contador[(indice) % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, len(array)):
            array[i] = saida[i]


    def sort(self, array):
        maximo = max(array)
        exponecial = 1
        while maximo // exponecial > 0:
            self.radix(array, exponecial)
            exponecial *= 10