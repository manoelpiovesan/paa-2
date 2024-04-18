class Utils:
    def __init__(self):
        pass
    
    @staticmethod
    def checkIfSorted(arr):
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