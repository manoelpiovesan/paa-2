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
            # self.algorithms.mergeSort,
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
        algorithms = SortingAlgorithms()

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
                    result = method(arr.copy())
                    result["method"] = method.__name__
                    resultsByComplexityCase["results"].append(result)
                    self._printInfo(result)

                Graph.barGraphForAll(resultsByComplexityCase)

    def _printInfo(self, result):
        print("Metodo: ", result["method"])
        print("Iteracoes: ", result["iterations"])
        print("Comparacoes: ", result["comparisons"])
        print("Trocas: ", result["swaps"])
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
