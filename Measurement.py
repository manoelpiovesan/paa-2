from SortingAlgorithms import SortingAlgorithms
from Utils import Utils
from Graph import Graph

class Measurement:
    def __init__(self):
        self.algorithms = SortingAlgorithms()
        self.lengthCasesToBeTested = [124, 256, 512, 1024, 2048, 4096, 8192]
        self.methodsToBeTested = [
            self.algorithms.bubbleSort,
            self.algorithms.selectionSort,
            self.algorithms.mergeSort,
            self.algorithms.heapSort,
            self.algorithms.binaryInsertionSort,
            self.algorithms.combSort,
            self.algorithms.shellSort,
            self.algorithms.radixSortLDS,
            self.algorithms.radixSortMDS,
            self.algorithms.insertionSort,
            # self.algorithms.timSort,
            self.algorithms.cocktailShakerSort,
            self.algorithms.gnomeSort,
            self.algorithms.oddEvenSort,
            # self.algorithms.quickSort,
            # self.algorithms.bitonicSort,
        ]  # Adicionando o Bitonic Sort aqui
        self.complexityCasesToBeTested = [
            Utils.worstCaseArrayByLength,
            Utils.averageCaseArrayByLength,
            Utils.bestCaseArrayByLength,
        ]

    def main(self):
        for lengthCase in self.lengthCasesToBeTested:
            self._printLengthCase(lengthCase)

            for complexityCase in self.complexityCasesToBeTested:
                arr = complexityCase(lengthCase)
                resultsByComplexityCase = {
                    "complexityCase": Utils.getCaseTitle(complexityCase.__name__),
                    "lengthCase": lengthCase,
                    "results": [],
                }

                for method in self.methodsToBeTested:
                    sorted_arr, memory_consumption, cpu_consumption = method(arr.copy())
                    result = {
                        "method": method.__name__,
                        "iterations": sorted_arr["iterations"],
                        "comparisons": sorted_arr["comparisons"],
                        "swaps": sorted_arr["swaps"],
                        "memory": memory_consumption,
                        "cpu": cpu_consumption
                    }
                    resultsByComplexityCase["results"].append(result)
                    self._printInfo(result)

                Graph.barGraphForAll(resultsByComplexityCase)
                Graph.barGraphForCpu(resultsByComplexityCase)
                Graph.barGraphForMemory(resultsByComplexityCase)

    def _printInfo(self, result):
        print("Método: ", result["method"])
        print("Iterações: ", result["iterations"])
        print("Comparações: ", result["comparisons"])
        print("Trocas: ", result["swaps"])
        print("Memória RAM (MB): ", result["memory"])
        print("Uso de CPU (%): ", result["cpu"])
        print("\n\n")

    def _printLengthCase(self, lengthCase):
        print(
            "-----------------------------------------------------------------------------"
        )
        print(
            "---------------------------CASO DE",
            lengthCase,
            "ELEMENTOS---------------------------",
        )
        print(
            "-----------------------------------------------------------------------------"
        )


if __name__ == "__main__":
    m = Measurement()
    m.main()
