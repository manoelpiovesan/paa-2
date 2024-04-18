class SortingAlgorithms:
    def __init__(self):
        self.iterations = 0 # Iterações
        self.comparisons = 0 # Comparações
        self.swaps = 0 # Trocas
    
    # Deve ser chamado antes de cada metodo de ordenação para zerar os contadores.
    def clearCounters(self):
        self.iterations = 0
        self.comparisons = 0
        self.swaps = 0
    
    # Metodos de incremento (tá meio redundante mas depois pode ser adicionado mais coisas quando for incrementar um dos parametros)
    # Usar os metodos para incrementar os parametros de contagem em cada metodo de ordenação
    def incrementIterations(self):
        self.iterations += 1
    
    def incrementComparisons(self):
        self.comparisons += 1
    
    def incrementSwaps(self):
        self.swaps += 1
    
    #
    # Métodos de ordenação
    #
    
    # Bubble Sort 
    def bubbleSort(self, arr):
        self.clearCounters()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                self.incrementIterations()
                if arr[j] > arr[j+1]:
                    self.incrementComparisons()
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.incrementSwaps()
        return {"iterations": self.iterations, "comparisons": self.comparisons, "swaps": self.swaps}
    
    # Selection Sort
    def selectionSort(self, arr):
        self.clearCounters()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                self.incrementIterations()
                if arr[j] < arr[min_idx]:
                    self.incrementComparisons()
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.incrementSwaps()
        return {"iterations": self.iterations, "comparisons": self.comparisons, "swaps": self.swaps}