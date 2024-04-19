from SortingAlgorithms import SortingAlgorithms
from Utils import Utils
from Graph import Graph 
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
        self.lengthCasesToBeTested = [124, 256, 512, 1024, 2048, 4096, 8192] # basta adicionar novos tamanho de arrays aqui para que sejam testados
        self.methodsToBeTested = [self.algorithms.bubbleSort, self.algorithms.selectionSort] # basta adicionar os métodos de ordenação aqui para que sejam testados
        self.complexityCasesToBeTested = [Utils.worstCaseArrayByLength, Utils.averageCaseArrayByLength, Utils.bestCaseArrayByLength] 
        # adicionar na classe Utils novas formas de gerar Arrays, e adicionar aqui para que sejam testados.
    #
    # Método principal para medir os métodos de ordenação.
    # Os metodos são iterados para cada caso de teste e método, com base no construtor desta classe.
    #
    def main(self):
        algorithms = SortingAlgorithms()
        
        # Itera sobre os casos de teste.
        for lengthCase in self.lengthCasesToBeTested:
            self._printLengthCase(lengthCase) # printando o caso de teste atual no console
            
            for complexityCase in self.complexityCasesToBeTested:
                arr = complexityCase(lengthCase) 
                resultsByComplexityCase = {"complexityCase": Utils.getCaseTitle(complexityCase.__name__), "lengthCase": lengthCase, "results": []}

                for method in self.methodsToBeTested:
                    result = method(arr.copy())
                    result["method"] = method.__name__ # adicionando o nome do método de ordenação no resultado
                    resultsByComplexityCase["results"].append(result) # adicionando o resultado na lista de resultados                  
                    self._printInfo(result) # printando as informações do método de ordenação atual no console

                # Gráfico de trocas por método de ordenação
                #Graph.barGraphForSwaps(resultsByComplexityCase)    
                # Gráfico de comparações por método de ordenação
                #Graph.barGraphForComparisons(resultsByComplexityCase)
                # Gráfico de iterações por método de ordenação
                # Graph.barGraphForIterations(resultsByComplexityCase)            
                Graph.barGraphForAll(resultsByComplexityCase)

    #
    # Método privado para imprimir as informações de cada método de ordenação.
    #
    def _printInfo(self, result):
        print("Metodo: ", result["method"])
        print("Iteracoes: ", result["iterations"])
        print("Comparacoes: ", result["comparisons"])
        print("Trocas: ", result["swaps"])
        print("\n\n")

    def _printLengthCase(self, lengthCase):
        print("-----------------------------------------------------------------------------")
        print("---------------------------CASO DE", lengthCase, "ELEMENTOS---------------------------")
        print("-----------------------------------------------------------------------------")
    
if __name__ == "__main__":
    m = Measurement()
    m.main()