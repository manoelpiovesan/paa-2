import tkinter as tk
from tkinter import messagebox
import random
import sys
import psutil
import csv
import matplotlib.pyplot as plt
import pandas as pd


def binary_insertion_sort(arr):
    comparisons = 0
    swaps = 0

    def binary_search(arr, val, start, end):
        nonlocal comparisons
        while start < end:
            mid = (start + end) // 2
            comparisons += 1
            if arr[mid] < val:
                start = mid + 1
            else:
                end = mid
        return start

    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
        swaps += (i - j)

    return arr, comparisons, swaps

def bitonic_sort(arr):
    comparisons = 0
    swaps = 0

    def compare_and_swap(a, b, direction):
        nonlocal comparisons, swaps
        comparisons += 1
        if (a > b) == direction:
            swaps += 1
            return b, a
        else:
            return a, b

    def bitonic_merge(arr, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                arr[i], arr[i + k] = compare_and_swap(arr[i], arr[i + k], direction)
            bitonic_merge(arr, low, k, direction)
            bitonic_merge(arr, low + k, k, direction)

    def bitonic_sort_rec(arr, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            bitonic_sort_rec(arr, low, k, True)
            bitonic_sort_rec(arr, low + k, k, False)
            bitonic_merge(arr, low, cnt, direction)

    bitonic_sort_rec(arr, 0, len(arr), True)
    return arr, comparisons, swaps

def bubble_sort(arr):
    comparisons = 0
    swaps = 0

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1

    return arr, comparisons, swaps

def cocktail_shaker_sort(arr):
    comparisons = 0
    swaps = 0

    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True
        start += 1

    return arr, comparisons, swaps

def comb_sort(arr):
    comparisons = 0
    swaps = 0

    def get_next_gap(gap):
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap

    n = len(arr)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False
        for i in range(0, n - gap):
            comparisons += 1
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swaps += 1
                swapped = True

    return arr, comparisons, swaps

def gnome_sort(arr):
    comparisons = 0
    swaps = 0

    n = len(arr)
    index = 0
    while index < n:
        if index == 0:
            index += 1
        comparisons += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            swaps += 1
            index -= 1

    return arr, comparisons, swaps

def heap_sort(arr):
    comparisons = 0
    swaps = 0

    def heapify(arr, n, i):
        nonlocal comparisons, swaps
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        comparisons += 1
        if left < n and arr[i] < arr[left]:
            largest = left
        comparisons += 1
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            swaps += 1
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swaps += 1
        heapify(arr, i, 0)

    return arr, comparisons, swaps

def insertion_sort(arr):
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
        arr[j + 1] = key

    return arr, comparisons, swaps

def merge_sort(arr):
    comparisons = 0
    swaps = 0

    def merge(left, right):
        nonlocal comparisons, swaps
        result = []
        while left and right:
            comparisons += 1
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
                swaps += 1
        result.extend(left or right)
        return result

    def merge_sort_rec(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_rec(arr[:mid])
        right = merge_sort_rec(arr[mid:])
        return merge(left, right)

    arr = merge_sort_rec(arr)
    return arr, comparisons, swaps

def odd_even_sort(arr):
    comparisons = 0
    swaps = 0

    n = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(1, n-1, 2):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                is_sorted = False
        for i in range(0, n-1, 2):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                is_sorted = False

    return arr, comparisons, swaps

def quicksort(arr):
    comparisons = 0
    swaps = 0

    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                comparisons += 1
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swaps += 1

            stack.append((low, i))
            stack.append((i + 2, high))

    return arr, comparisons, swaps



def radix_sort_lds(arr):
    comparisons = 0
    swaps = 0

    def counting_sort(arr, exp):
        nonlocal comparisons, swaps
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
        for i in range(n):
            arr[i] = output[i]
            swaps += 1
            comparisons += 1


    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr, comparisons, swaps

def radix_sort_mds(arr):
    comparisons = 0
    swaps = 0

    def counting_sort(arr, exp):
        nonlocal comparisons, swaps
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        for     i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
        for i in range(n):
            arr[i] = output[i]
            swaps += 1
            comparisons += 1


    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr, comparisons, swaps

def selection_sort(arr):
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1

    return arr, comparisons, swaps

def shell_sort(arr):
    comparisons = 0
    swaps = 0

    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                j -= gap
                swaps += 1
            arr[j] = temp
        gap //= 2

    return arr, comparisons, swaps

def tim_sort(arr):
    comparisons = 0
    swaps = 0

    def insertion_sort(arr, left, right):
        nonlocal comparisons, swaps
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                comparisons += 1
                arr[j + 1] = arr[j]
                j -= 1
                swaps += 1
            arr[j + 1] = key

    def merge(arr, l, m, r):
        nonlocal comparisons, swaps
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        for i in range(0, len1):
            left.append(arr[l + i])
        for i in range(0, len2):
            right.append(arr[m + 1 + i])
        i, j, k = 0, 0, l
        while i < len1 and j < len2:
            comparisons += 1
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                swaps += 1
            k += 1
        while i < len1:
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len2:
            arr[k] = right[j]
            k += 1
            j += 1

    min_run = 32
    n = len(arr)
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size

    return arr, comparisons, swaps

def generate_sorted_array(n, ascending=True):
    if ascending:
        return list(range(1, n+1))
    else:
        return list(range(n, 0, -1))

def generate_random_array(n):
    return random.sample(range(1, n+1), n)

def generate_partially_ordered_array(n, ordered_portion='start'):
    ordered = list(range(1, n//2 + 1)) if ordered_portion == 'start' else list(range(n//2 + 1, n + 1))
    random_part = generate_random_array(n - len(ordered))
    return ordered + random_part

def generate_partial_ordered_start(n, ordered_portion=0.25):
    ordered = list(range(1, int(n*ordered_portion) + 1))
    random_part = generate_random_array(n - len(ordered))
    return ordered + random_part

def generate_partial_ordered_middle(n, ordered_portion=0.25):
    random_part1 = generate_random_array(n // 2)
    ordered = list(range(n // 2 + 1, int(n // 2 + n*ordered_portion) + 1))
    random_part2 = generate_random_array(n - len(ordered) - len(random_part1))
    return random_part1 + ordered + random_part2

def generate_partial_ordered_end(n, ordered_portion=0.25):
    random_part = generate_random_array(n // 2)
    ordered = list(range(n // 2 + 1 - int(n*ordered_portion), n // 2 + 1))
    random_part2 = generate_random_array(n - len(ordered) - len(random_part))
    return random_part + ordered + random_part2



def run_sorting_algorithms(array):
    results = {}
    algorithms = {
            'Bitonic Sort': bitonic_sort,
            'Bubble Sort': bubble_sort,
            'Cocktail Shaker Sort': cocktail_shaker_sort,
            'Comb Sort': comb_sort,
            'Gnome Sort': gnome_sort,
            'Heap Sort': heap_sort,
            'Insertion Sort': insertion_sort,
            'Merge Sort': merge_sort,
            'Odd-Even Sort': odd_even_sort,
            'Quicksort': quicksort,
            'Radix Sort LDS': radix_sort_lds,
            'Radix Sort MDS': radix_sort_mds,
            'Selection Sort': selection_sort,
            'Shell Sort': shell_sort,
            'Tim Sort': tim_sort
    }

    process = psutil.Process()
    initial_memory = process.memory_info().rss
    initial_cpu = process.cpu_percent(interval=None)

    for algorithm_name, algorithm_func in algorithms.items():
        _, comparisons, swaps = algorithm_func(array.copy())
        results[algorithm_name] = {'Comparisons': comparisons, 'Swaps': swaps}

    final_memory = process.memory_info().rss
    final_cpu = process.cpu_percent(interval=None)

    memory_consumed = final_memory - initial_memory
    cpu_consumed = final_cpu - initial_cpu

    # Adicionando código para escrever os resultados em um arquivo CSV
    with open('sorting_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escrevendo o cabeçalho do CSV
        writer.writerow(['Algorithm', 'Comparisons', 'Swaps', 'Memory Consumed', 'CPU Consumed'])
        # Escrevendo os resultados de cada algoritmo no arquivo CSV
        for algorithm_name, result in results.items():
            writer.writerow([algorithm_name, result['Comparisons'], result['Swaps'], memory_consumed, cpu_consumed])

    return results, memory_consumed, cpu_consumed
# Função para iniciar a ordenação quando o botão "Start" é clicado

def start_sorting():
    array_type = array_type_var.get()
    array_size = int(array_size_var.get())

    if array_type == "Totalmente ordenado crescentemente":
        array = generate_sorted_array(array_size, ascending=True)
    elif array_type == "Totalmente ordenado decrescentemente":
        array = generate_sorted_array(array_size, ascending=False)
    elif array_type == "Totalmente aleatório desordenado":
        array = generate_random_array(array_size)
    elif array_type == "50% ordenado do início ao meio, com o meio para o final aleatório":
        array = generate_partially_ordered_array(array_size, ordered_portion='start')
    elif array_type == "50% ordenado do meio ao final, com o início até o meio aleatório":
        array = generate_partially_ordered_array(array_size, ordered_portion='end')
    elif array_type == "25% ordenado apenas no início":
        array = generate_partial_ordered_start(array_size)
    elif array_type == "25% ordenado no meio":
        array = generate_partial_ordered_middle(array_size)
    elif array_type == "25% ordenado no final":
        array = generate_partial_ordered_end(array_size)

    results, memory_consumed, cpu_consumed = run_sorting_algorithms(array)

    print("Results:")
    for algorithm_name, result in results.items():
        print(f"Algorithm: {algorithm_name}")
        print(f"Comparisons: {result['Comparisons']}")
        print(f"Swaps: {result['Swaps']}")
        print(f"Total Memory Consumed: {memory_consumed} bytes")
        print(f"Total CPU Consumed: {cpu_consumed}%")

def generate_all():
    array_sizes = ["10"]
    array_types = [
        "Totalmente ordenado crescentemente",
        "Totalmente ordenado decrescentemente",
        "Totalmente aleatório desordenado",
        "50% ordenado do início ao meio, com o meio para o final aleatório",
        "50% ordenado do meio ao final, com o início até o meio aleatório",
        "25% ordenado apenas no início",
        "25% ordenado no meio",
        "25% ordenado no final"
    ]

    for array_size in array_sizes:
        for array_type in array_types:
            array_size = int(array_size)
            if array_type == "Totalmente ordenado crescentemente":
                array = generate_sorted_array(array_size, ascending=True)
            elif array_type == "Totalmente ordenado decrescentemente":
                array = generate_sorted_array(array_size, ascending=False)
            elif array_type == "Totalmente aleatório desordenado":
                array = generate_random_array(array_size)
            elif array_type == "50% ordenado do início ao meio, com o meio para o final aleatório":
                array = generate_partially_ordered_array(array_size, ordered_portion='start')
            elif array_type == "50% ordenado do meio ao final, com o início até o meio aleatório":
                array = generate_partially_ordered_array(array_size, ordered_portion='end')
            elif array_type == "25% ordenado apenas no início":
                array = generate_partial_ordered_start(array_size)
            elif array_type == "25% ordenado no meio":
                array = generate_partial_ordered_middle(array_size)
            elif array_type == "25% ordenado no final":
                array = generate_partial_ordered_end(array_size)

            results, memory_consumed, cpu_consumed = run_sorting_algorithms(array)

            # Criando um identificador único para o tipo de array e tamanho de array
            identifier = f"{array_size}_{array_type.replace(' ', '_').lower()}"

            # Escrevendo os resultados em um arquivo CSV separado para cada combinação de tipo de array e tamanho de array
            with open(f'sorting_results_{identifier}.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                # Escrevendo o cabeçalho do CSV
                writer.writerow(['Algorithm', 'Comparisons', 'Swaps', 'Memory Consumed', 'CPU Consumed'])
                # Escrevendo os resultados de cada algoritmo no arquivo CSV
                for algorithm_name, result in results.items():
                    writer.writerow([algorithm_name, result['Comparisons'], result['Swaps'], memory_consumed, cpu_consumed])


root = tk.Tk()
root.title("Sorting Algorithms")

array_type_var = tk.StringVar(root)
array_types = [
    "Totalmente ordenado crescentemente",
    "Totalmente ordenado decrescentemente",
    "Totalmente aleatório desordenado",
    "50% ordenado do início ao meio, com o meio para o final aleatório",
    "50% ordenado do meio ao final, com o início até o meio aleatório",
    "25% ordenado apenas no início",
    "25% ordenado no meio",
    "25% ordenado no final"
]


array_type_label = tk.Label(root, text="Tipo de Array:")
array_type_label.grid(row=0, column=0, padx=5, pady=5)

array_type_dropdown = tk.OptionMenu(root, array_type_var, *array_types)
array_type_dropdown.grid(row=0, column=1, padx=5, pady=5)

array_size_label = tk.Label(root, text="Tamanho do Array:")
array_size_label.grid(row=1, column=0, padx=5, pady=5)

array_size_var = tk.StringVar(root)
array_sizes = ["100", "1000", "5000", "10000"]
array_size_dropdown = tk.OptionMenu(root, array_size_var, *array_sizes)
array_size_dropdown.grid(row=1, column=1, padx=5, pady=5)

start_button = tk.Button(root, text="Start", command=start_sorting)
start_button.grid(row=2, columnspan=2, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate All", command=generate_all)
generate_button.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()