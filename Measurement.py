from SortingAlgorithms import SortingAlgorithms
from Utils import Utils
#
# Classe principal para medir os métodos de ordenação, comparando o número de iterações, comparações e trocas.
#
# Para adicionar mais métodos de ordenação, basta criar um método novo na classe SortingAlgorithms e adicionar o método na lista self.methods.
# Atenção para o retorno esperado do método de ordenação, que deve ser um map com as chaves "iterations", "comparisons" e "swaps".
# Para adicionar mais casos de teste, basta adicionar o tamanho do array na lista self.testCases.
#
class Measurement:
    def __init__(self):
        self.algorithms = SortingAlgorithms()
        self.testCases = [124, 256, 512, 1024, 2048, 4096] # basta adicionar os casos de teste aqui para que sejam testados
        self.methods = [self.algorithms.bubbleSort, self.algorithms.selectionSort] # basta adicionar os métodos de ordenação aqui para que sejam testados

    #
    # Método principal para medir os métodos de ordenação.
    # Os metodos são iterados para cada caso de teste e método, com base no construtor desta classe.
    #
    def main(self):
        algorithms = SortingAlgorithms()
        
        # Itera sobre os casos de teste.
        for i in self.testCases:
            arr = Utils.worstCaseArrayByLength(i) # Pior caso (pode trocar dps para melhor caso, caso médio, etc)
            print("-----------------------------------------------------------------------------")
            print("---------------------------CASO DE", i, "ELEMENTOS---------------------------")
            print("-----------------------------------------------------------------------------")
            
            # Itera sobre os métodos de ordenação.
            for method in self.methods:
                print("Metodo: ", method.__name__)
                result = method(arr.copy())
                print("Iteracoes: ", result["iterations"])
                print("Comparacoes: ", result["comparisons"])
                print("Trocas: ", result["swaps"])
                print("\n\n")
            
if __name__ == "__main__":
    m = Measurement()
    m.main()