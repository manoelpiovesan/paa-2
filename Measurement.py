# Na classe principal seria interessante que chamassemos os métodos de uma classe externa que contenha
# os métodos de ordenação. Assim, a classe principal ficaria mais limpa e organizada.

# Aqui fariamos a medição de memória e tempo de execução dos métodos de ordenação.
from SortingAlgorithms import SortingAlgorithms
from Utils import Utils

class Measurement:
    def __init__(self):
        self.algorithms = SortingAlgorithms()
        self.testCases = [10, 100, 1000, 5000, 10000] # basta adicionar os casos de teste aqui para que sejam testados
        self.methods = [self.algorithms.bubbleSort, self.algorithms.selectionSort] # basta adicionar os métodos de ordenação aqui para que sejam testados

    
    def main(self):
        algorithms = SortingAlgorithms()
        for i in self.testCases:
            arr = Utils.WorstCaseArrayByLength(i) # Pior caso (pode trocar dps para melhor caso, caso médio, etc)
            print("-----------------------------------------------------------------------------")
            print("---------------------------CASO DE", i, "ELEMENTOS---------------------------")
            print("-----------------------------------------------------------------------------")
            for method in self.methods:
                print("Método: ", method.__name__)
                result = method(arr.copy())
                print("Iteracoes: ", result["iterations"])
                print("Comparacoes: ", result["comparisons"])
                print("Trocas: ", result["swaps"])
                print("\n\n")
            
if __name__ == "__main__":
    m = Measurement()
    m.main()