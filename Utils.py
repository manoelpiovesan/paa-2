class Utils:
    def __init__(self):
        pass
    
    #
    # Atenção: leva em consideração que o array começa em 0 e vai até n-1 sem repetições de elementos.
    #
    @staticmethod
    def isSorted(arr):
        sorted = []
        for i in range(len(arr)):
            sorted.append(i)
        if arr == sorted:
            return True
        else:
            return False
    
    
    @staticmethod
    def WorstCaseArrayByLength(length):
        arr = []
        for i in range(length):
            arr.append(length-i)
        return arr