import psutil
import os
from Utils import Utils
import memory_profiler

class SortingAlgorithms:
    def __init__(self):
        self.iterations = 0  # Iterações
        self.comparisons = 0  # Comparações
        self.swaps = 0  # Trocas

    # Deve ser chamado antes de cada método de ordenação para zerar os contadores.
    def _clearCounters(self):
        self.iterations = 0
        self.comparisons = 0
        self.swaps = 0

    # Métodos de incremento
    def _incrementIterations(self):
        self.iterations += 1

    def _incrementComparisons(self):
        self.comparisons += 1

    def _incrementSwaps(self):
        self.swaps += 1

    # Função para verificar se o array está ordenado
    def _returnArrayIfSorted(self, arr):
        if not Utils.isSorted(arr):
            raise Exception("Array não está ordenado.")
        return {
            "iterations": self.iterations,
            "comparisons": self.comparisons,
            "swaps": self.swaps,
        }

    def _get_memory_usage(self):
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / (1024 * 1024)  # Convertendo para megabytes

 
    def _get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)  # Percentual de uso da CPU

    # Métodos de ordenação
    @memory_profiler.profile
    def bubble(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                self._incrementIterations()
                self._incrementComparisons()
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self._incrementSwaps()

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    @memory_profiler.profile
    def merge(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        sorted_arr = self._mergeSort(arr)

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(sorted_arr), memory_consumption, cpu_consumption

    def _mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = self._mergeSort(arr[:mid])
        right_half = self._mergeSort(arr[mid:])
        return self._mergeS(arr, left_half, right_half, len(left_half), len(right_half))


    def _mergeS(self, arr, left, right, len_left, len_right):
        merged = []
        left_idx, right_idx = 0, 0
        while left_idx < len_left and right_idx < len_right:
            if left[left_idx] < right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1
        merged.extend(left[left_idx:])
        merged.extend(right[right_idx:])
        return merged

    
    @memory_profiler.profile
    def heap(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        self._heapSort(arr)

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    def _heapSort(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self._incrementSwaps()
            self._heapify(arr, i, 0)


    def _heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        self._incrementIterations()
        if left < n and arr[i] < arr[left]:
            largest = left
            self._incrementComparisons()
        if right < n and arr[largest] < arr[right]:
            largest = right
            self._incrementComparisons()
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._incrementSwaps()
            self._heapify(arr, n, largest)

    @memory_profiler.profile
    def binaryIns(self, arr):
            self._clearCounters()

            initial_memory = self._get_memory_usage()
            initial_cpu = self._get_cpu_usage()

            for i in range(1, len(arr)):
                key = arr[i]
                left, right = 0, i - 1
                while left <= right:
                    mid = (left + right) // 2
                    self._incrementIterations()
                    if arr[mid] < key:
                        left = mid + 1
                    else:
                        right = mid - 1
                arr[left+1:i+1] = arr[left:i]
                arr[left] = key
                self._incrementSwaps()
            final_memory = self._get_memory_usage()
            final_cpu = self._get_cpu_usage()

            memory_consumption = abs(final_memory - initial_memory)
            cpu_consumption = abs(final_cpu - initial_cpu)

            return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    def _binaryInsertionSort(self, arr):
        for i in range(1, len(arr)):
            item_to_insert = arr[i]
            j = i - 1
            insert_index = self._binarySearch(arr, item_to_insert, 0, j)
            while j >= insert_index:
                arr[j + 1] = arr[j]
                j -= 1
                self._incrementIterations()
                self._incrementComparisons()
                self._incrementSwaps()
            arr[j + 1] = item_to_insert

    def _binarySearch(self, arr, item, start, end):
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
            return self._binarySearch(arr, item, middle + 1, end)
        elif arr[middle] > item:
            self._incrementComparisons()
            return self._binarySearch(arr, item, start, middle - 1)
        else:
            self._incrementComparisons()
            return middle

    @memory_profiler.profile
    def comb(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        self._combSort(arr)

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    def _combSort(self, arr):
        gap = len(arr)
        shrink_factor = 1.3
        swapped = True
        while gap != 1 or swapped:
            gap = int(gap / shrink_factor)
            if gap < 1:
                gap = 1
            swapped = False
            for i in range(len(arr) - gap):
                self._incrementIterations()
                self._incrementComparisons()
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    self._incrementSwaps()
                    swapped = True

    @memory_profiler.profile
    def shell(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        self._shellSort(arr)

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    def _shellSort(self, arr):
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

    @memory_profiler.profile
    def lds(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        self._radixSortLDS(arr)

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    def _radixSortLDS(self, arr):
        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            self._countSortLDS(arr, exp)
            exp *= 10

    def _countSortLDS(self, arr, exp):
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

    @memory_profiler.profile
    def mds(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        self._radixSortMDS(arr)

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    def _radixSortMDS(self, arr):
        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            self._countSortMDS(arr, exp)
            exp *= 10

    def _countSortMDS(self, arr, exp):
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

    @memory_profiler.profile
    def insertion(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                self._incrementIterations()
                self._incrementComparisons()
                self._incrementSwaps()
            arr[j + 1] = key

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    @memory_profiler.profile
    def selection(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                self._incrementIterations()
                self._incrementComparisons()
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
            self._incrementSwaps()

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    def _merge(self, arr, l, m, r):
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        for i in range(0, len1):
            left.append(arr[l + i])
        for i in range(0, len2):
            right.append(arr[m + 1 + i])
        i, j, k = 0, 0, l
        while i < len1 and j < len2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len1:
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len2:
            arr[k] = right[j]
            k += 1
            j += 1

    @memory_profiler.profile
    def tim(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        min_run = 32
        n = len(arr)

        for start in range(0, n, min_run):
            end = min(start + min_run - 1, n - 1)
            self._insertionSortTim(arr, start, end)
            
        size = min_run
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))

                if mid < right:
                    self._merge(arr, left, mid, right)

            size = 2 * size

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    def _insertionSortTim(self, arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                self._incrementIterations()
                self._incrementComparisons()
                self._incrementSwaps()
            arr[j + 1] = key

    @memory_profiler.profile
    def cocktail(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        while swapped:
            swapped = False
            for i in range(start, end):
                self._incrementIterations()
                self._incrementComparisons()
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    self._incrementSwaps()
                    swapped = True
            if not swapped:
                break
            swapped = False
            end -= 1
            for i in range(end - 1, start - 1, -1):
                self._incrementIterations()
                self._incrementComparisons()
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    self._incrementSwaps()
                    swapped = True
            start += 1

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    @memory_profiler.profile
    def gnome(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        n = len(arr)
        index = 0
        while index < n:
            self._incrementIterations()
            if index == 0:
                index += 1
            if arr[index] >= arr[index - 1]:
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                self._incrementSwaps()
                index -= 1

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu) 

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    @memory_profiler.profile
    def oddEven(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        n = len(arr)
        sorted = False
        while not sorted:
            sorted = True
            for i in range(0, n - 1, 2):
                self._incrementIterations()
                self._incrementComparisons()
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    self._incrementSwaps()
                    sorted = False
            for i in range(1, n - 1, 2):
                self._incrementIterations()
                self._incrementComparisons()
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    self._incrementSwaps()
                    sorted = False

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    @memory_profiler.profile
    def quick(self, arr, low=0, high=None):
        if high is None:
            high = len(arr) - 1

        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        self._quickSort(arr, low, high)

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    def _quickSort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quickSort(arr, low, pi - 1)
            self._quickSort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            self._incrementIterations()
            self._incrementComparisons()
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self._incrementSwaps()
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self._incrementSwaps()
        return i + 1

    @memory_profiler.profile
    def bitonic(self, arr):
        self._clearCounters()
        initial_memory = self._get_memory_usage()
        initial_cpu = self._get_cpu_usage()

        self._bitonicSort(arr, 0, len(arr), True)

        final_memory = self._get_memory_usage()
        final_cpu = self._get_cpu_usage()

        memory_consumption = abs(final_memory - initial_memory)
        cpu_consumption = abs(final_cpu - initial_cpu)

        return self._returnArrayIfSorted(arr), memory_consumption, cpu_consumption

    def _bitonicSort(self, arr, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            self._bitonicSort(arr, low, k, True)
            self._bitonicSort(arr, low + k, k, False)
            self._bitonicMerge(arr, low, cnt, direction)

    def _bitonicMerge(self, arr, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                self._compareAndSwap(arr, i, i + k, direction)
            self._bitonicMerge(arr, low, k, direction)
            self._bitonicMerge(arr, low + k, k, direction)

    def _compareAndSwap(self, arr, i, j, direction):
        self._incrementIterations()
        if (direction == (arr[i] > arr[j])):
            arr[i], arr[j] = arr[j], arr[i]
            self._incrementSwaps()