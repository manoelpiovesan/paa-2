#
# Classe com métodos úteis para o projeto.
# 
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
    def WorstCaseArrayByLength(length):
        arr = []
        for i in range(length):
            arr.append(length-i)
        return arr