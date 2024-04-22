from Utils import Utils
class SortingAlgorithms:
    def __init__(self):
        self.iterations = 0 # Iterações
        self.comparisons = 0 # Comparações
        self.swaps = 0 # Trocas
    
    # Deve ser chamado antes de cada metodo de ordenação para zerar os contadores.
    def _clearCounters(self):
        self.iterations = 0
        self.comparisons = 0
        self.swaps = 0
    
    # Metodos de incremento (tá meio redundante mas depois pode ser adicionado mais coisas quando for incrementar um dos parametros)
    # Usar os metodos para incrementar os parametros de contagem em cada metodo de ordenação.
    # 🔴 Atenção para incrementar os parametros corretos em cada metodo. Verificar o local correto para incrementar.
    def _incrementIterations(self):
        self.iterations += 1
    
    def _incrementComparisons(self):
        self.comparisons += 1
    
    def _incrementSwaps(self):
        self.swaps += 1
    
    #
    # Métodos de ordenação
    #
    
    # Bubble Sort 
    def bubbleSort(self, arr):
        self._clearCounters()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                self._incrementIterations()
                self._incrementComparisons()
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self._incrementSwaps()
                    
        # Usar esse método para retornar o array se ele estiver ordenado.
        return self._returnArrayIfSorted(arr)
    
    # Selection Sort
    def selectionSort(self, arr):
        self._clearCounters()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                self._incrementIterations()
                self._incrementComparisons()
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self._incrementSwaps()
        
        return self._returnArrayIfSorted(arr) 
    
    #
    # Usar esse método para retornar o array se ele estiver ordenado.
    # Se não estiver, ele lança uma exceção.
    #
    def _returnArrayIfSorted(self, arr):
        if (Utils.isSorted(arr) == False):
            exception = "Array não está ordenado."
            raise Exception(exception)
        else:
            return {"iterations": self.iterations, "comparisons": self.comparisons, "swaps": self.swaps}    