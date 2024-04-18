#
# Classe com métodos úteis para o projeto.
# 
import random


class Utils:
    def __init__(self):
        pass
    
    #
    # Verifica se o array está ordenado.
    # Atenção: leva em consideração que o array começa em 1 e vai até n sem repetições de elementos.
    #
    @staticmethod
    def isSorted(arr):
        sorted = []
        for i in range(len(arr)):
            sorted.append(i+1)
        if arr == sorted:
            return True
        else:
            return False
    
    #
    # Retorna o pior caso de um array de tamanho length.
    #
    @staticmethod
    def worstCaseArrayByLength(length):
        arr = []
        for i in range(length):
            arr.append(length-i)
        return arr

    #
    # Retorna o caso médio de um array de tamanho n sem repetições de elementos.
    #
    @staticmethod
    def averageCaseArrayByLength(length):
        arr = []
        for i in range(length):
            arr.append(i+1)
        # embaralhando o array
        for i in range(length):
            j = random.randint(0, length-1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    
    #
    # Retorna o melhor caso de um array de tamanho n sem repetições de elementos.
    #
    @staticmethod
    def bestCaseArrayByLength(length):
        arr = []
        for i in range(length):
            arr.append(i+1)
        return arr
        