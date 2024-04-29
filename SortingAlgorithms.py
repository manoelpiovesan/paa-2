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

    # Merge Sort
    def mergeSort(self, arr):
        self._clearCounters()
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            left_half = merge_sort(left_half)
            right_half = merge_sort(right_half)

            self._incrementIterations()

            return merge(left_half, right_half)
        def merge(left, right):
            merged = []
            left_idx, right_idx = 0, 0

            while left_idx < len(left) and right_idx < len(right):
                if left[left_idx] < right[right_idx]:
                    merged.append(left[left_idx])
                    left_idx += 1
                else:
                    merged.append(right[right_idx])
                    right_idx += 1
                    self._incrementSwaps()

                self._incrementComparisons()

            merged.extend(left[left_idx:])
            merged.extend(right[right_idx:])

            return self._returnArrayIfSorted(merged)


    # Heap Sort
    def heapSort(self, arr):
        self._clearCounters()
        def heapify(arr, n, i):
            greater = i
            left = 2 * i + 1
            right = 2 * i + 2
            self._incrementIterations()

            if left < n and arr[i] < arr[left]:
                greater = left
                self._incrementComparisons()
            self._incrementIterations()

            if right < n and arr[greater] < arr[right]:
                greater = right
                self._incrementComparisons()
            self._incrementIterations()

            if greater != i:
                arr[i], arr[greater] = arr[greater], arr[i]
                self._incrementSwaps()
                yield from heapify(arr, n, greater)
            self._incrementIterations()

        def heap_sort(arr):
            n = len(arr)
            for i in range(n // 2, -1, -1):
                yield from heapify(arr, n, i)

            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                yield from heapify(arr, i, 0)

        generator = heap_sort(arr)
        for _ in generator:
            pass

        return self._returnArrayIfSorted(arr)

    # Binary Insertion Sort
    def binaryinsertionSort(self, arr):
        self._clearCounters()
        def binary_search(arr, item, start, end):
            if start == end:
                self._incrementIterations()
                self._incrementComparisons()
                return start if arr[start] > item else start + 1
            if start > end:
                self._incrementIterations()
                self._incrementComparisons()
                return start

            middle = (start + end) // 2
            self._incrementIterations()
            if arr[middle] < item:
                self._incrementComparisons()
                return binary_search(arr, item, middle + 1, end)
            elif arr[middle] > item:
                self._incrementComparisons()
                return binary_search(arr, item, start, middle - 1)
            else:
                self._incrementComparisons()
                return middle

        def binary_insertion_sort(arr):
            for i in range(1, len(arr)):
                item_to_insert = arr[i]
                j = i - 1
                insert_index = binary_search(arr, item_to_insert, 0, j)
                while j >= insert_index:
                    arr[j + 1] = arr[j]
                    j -= 1
                    self._incrementIterations()
                    self._incrementComparisons()
                    self._incrementSwaps()
                arr[j + 1] = item_to_insert
            return self._returnArrayIfSorted(arr)


    # Comb Sort
    def combSort(self, arr):
        self._clearCounters()
        gap = len(arr)
        shrink_factor = 1.3
        swapped = False

        iterations = 0
        max_iterations = len(arr) * len(arr) // 2

        while (gap != 1 or swapped) and iterations < max_iterations:
            gap = int(gap / shrink_factor)
            if gap < 1:
                gap = 1
            i = 0
            swapped = False

            while i + gap < len(arr):
                self._incrementComparisons()
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
                    self._incrementSwaps()

                i += 1
                iterations += 1
                self._incrementIterations()

        return self._returnArrayIfSorted(arr)


    # Shell Sort
    def shellSort(self, arr):
        self._clearCounters()
        length = len(arr)
        gap = length // 2

        while gap > 0:
            for i in range(gap, length):
                current_element = arr[i]
                j = i
                while j >= gap and arr[j - gap] > current_element:
                    arr[j] = arr[j - gap]
                    j -= gap
                    self._incrementIterations()
                    self._incrementComparisons()
                    self._incrementSwaps()
                arr[j] = current_element
            gap //= 2
        return self._returnArrayIfSorted(arr)


    # Radix Sort LDS
    def radixSortLDS(self, arr):
        self._clearCounters()
        def contSortLDS(arr, exp):
            n = len(arr)
            aux = [0] * n
            count = [0] * 10

            for i in range(n):
                idx = arr[i] // exp
                count[idx % 10] += 1
                self._incrementIterations()

            for i in range(1, 10):
                count[i] += count[i - 1]
                self._incrementIterations()

            i = n - 1

            while i >= 0:
                idx = arr[i] // exp
                aux[count[idx % 10] - 1] = arr[i]
                count[idx % 10] -= 1
                self._incrementIterations()
                self._incrementComparisons()
                i -= 1

            for i in range(n):
                arr[i] = aux[i]
                self._incrementIterations()

        def radix_sort_LDS(arr):
            max_num = max(arr)
            exp = 1
            while max_num // exp > 0:
                contSortLDS(arr, exp)
                exp *= 10
                self._incrementIterations()

        radix_sort_LDS(arr)
        return self._returnArrayIfSorted(arr)


    # Radix Sort MDS
    def radixSortMDS(self, arr):
        def contSortMDS(arr, exp):
            n = len(arr)
            aux = [0] * n
            count = [0] * 10

            for i in range(n):
                idx = (arr[i] // exp) % 10
                count[idx] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                idx = (arr[i] // exp) % 10
                aux[count[idx] - 1] = arr[i]
                count[idx] -= 1
                i -= 1
                self._incrementSwaps()

            for i in range(n):
                arr[i] = aux[i]
                self._incrementIterations()
                yield arr.copy(), i

        def radix_sort_MDS(arr):
            max_num = max(arr)
            exp = 1
            while max_num // exp > 0:
                yield from contSortMDS(arr, exp)
                exp *= 10

        generator = radix_sort_MDS(arr)
        for sorted_arr, _ in generator:
            pass
            self._incrementComparisons()

        return self._returnArrayIfSorted(arr)

    # Insertion Sort
    def insertionSort(self, arr):
        self._clearCounters()
        for j in range(1, len(arr)):
            key = arr[j]
            i = j - 1

            while i >= 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i -= 1
                self._incrementIterations()
                self._incrementComparisons()
                self._incrementSwaps()
        arr[i + 1] = key
        self._incrementSwaps()

        return self._returnArrayIfSorted(arr)


    # Tim Sort
    def timSort(self, arr):
        self._clearCounters()
        valorMin = 32
        def calcMinRun(n):
            last = 0
            while n >= valorMin:
                last |= n & 1
                n >>= 1
            return n + last

        def insertionSort(arr, left, right):
            for i in range(left + 1, right + 1):
                j = i
                while j > left and arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    j -= 1
                    self._incrementIterations()
                    self._incrementComparisons()
                    self._incrementSwaps()

        def merge(arr, first, mid, last):
            len1, len2 = mid - first + 1, last - mid
            left, right = [], []
            for i in range(0, len1):
                left.append(arr[first + i])
            for i in range(0, len2):
                right.append(arr[mid + 1 + i])

            i = 0
            j = 0
            k = first

            while i < len1 and j < len2:
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
                self._incrementIterations()
                self._incrementComparisons()

            while i < len1:
                arr[k] = left[i]
                k += 1
                i += 1
                self._incrementSwaps()

            while j < len2:
                arr[k] = right[j]
                k += 1
                j += 1
                self._incrementSwaps()

        def tim_sort(arr):
            n = len(arr)
            minRun = calcMinRun(n)
            for start in range(0, n, minRun):
                fim = min(start + minRun - 1, n - 1)
                insertionSort(arr, start, fim)
            size = minRun
            while size < n:
                for left in range(0, n, 2 * size):
                    half = min(n - 1, left + size - 1)
                    right = min((left + 2 * size - 1), (n - 1))
                    if half < right:
                        merge(arr, left, half, right)
                size = 2 * size
            return arr

        sort_arr = tim_sort(arr)
        return self._returnArrayIfSorted(sort_arr)

    # Cocktail Shaker Sort
    def cocktailshakerSort(self, arr):
        self._clearCounters()
        def cocktail_shaker_sort(arr):
            n = len(arr)
            swap = True
            start = 0
            end = n - 1

            while swap:
                swap = False

                for i in range(start, end):
                    self._incrementIterations()
                    if arr[i] > arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        swap = True
                        self._incrementSwaps()
                    self._incrementComparisons()
                    yield arr

                if not swap:
                    break

                swap = False
                end -= 1

                for i in range(end - 1, start - 1, -1):
                    self._incrementIterations()
                    if arr[i] > arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        swap = True
                        self._incrementSwaps()
                    self._incrementComparisons()
                    yield arr

                start += 1

            return arr

        return self._returnArrayIfSorted(list(cocktail_shaker_sort(arr))[-1])

    # Gnome Sort
    def gnomeSort(self, arr):
        self._clearCounters()
        n = len(arr)
        idx = 0
        while idx < n:
            self._incrementIterations()
            if idx == 0 or arr[idx] >= arr[idx - 1]:
                idx += 1
            else:
                arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
                idx -= 1
                self._incrementSwaps()
                self._incrementComparisons()
        return arr

    # Odd Even Sort
    def oddevenSort(self, arr):
        self._clearCounters()
        n = len(arr)
        def odd_even_sort(arr):
            sort = False
            while not sort:
                sort = True
                for i in range(0, n - 1, 2):
                    self._incrementIterations()
                    if arr[i] > arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        sort = False
                        self._incrementSwaps()
                    self._incrementComparisons()
                    yield arr

                for i in range(1, n - 1, 2):
                    self._incrementIterations()
                    if arr[i] > arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        sort = False
                        self._incrementSwaps()
                    self._incrementComparisons()
                    yield arr
            yield arr

        sort_arr_generator = odd_even_sort(arr)
        sorted_array = None
        for sorted_array in sort_arr_generator:
            pass
        return self._returnArrayIfSorted(sorted_array)

    # Quick Sort
    def quickSort(self, arr):
        self._clearCounters()
        def partition(arr, low, high):
            pivot_index = (low + high) // 2
            pivot_value = arr[pivot_index]
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            i = low
            for j in range(low, high):
                self._incrementComparisons()
                if arr[j] < pivot_value:
                    arr[i], arr[j] = arr[j], arr[i]
                    self._incrementSwaps()
                    i += 1
                self._incrementIterations()
            arr[i], arr[high] = arr[high], arr[i]
            self._incrementSwaps()
            return i

        def median_of_three(arr, low, high):
            mid = (low + high) // 2
            if arr[low] > arr[mid]:
                arr[low], arr[mid] = arr[mid], arr[low]
            if arr[mid] > arr[high]:
                arr[mid], arr[high] = arr[high], arr[mid]
            if arr[low] > arr[mid]:
                arr[low], arr[mid] = arr[mid], arr[low]
            return mid

        def quick_sort_med(arr, low, high):
            if low < high:
                pivot_index = median_of_three(arr, low, high)
                pivot_index = partition(arr, low, high)
                yield arr
                yield from quick_sort_med(arr, low, pivot_index - 1)
                yield from quick_sort_med(arr, pivot_index + 1, high)

        def quick_sort(arr):
            yield from quick_sort_med(arr, 0, len(arr) - 1)

        sorted_arr = arr.copy()
        for _ in quick_sort(sorted_arr):
            pass
        return self._returnArrayIfSorted(sorted_arr)

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