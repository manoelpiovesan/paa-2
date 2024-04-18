import matplotlib.pyplot as plt

class Graph:

    #
    #
    #
    @staticmethod
    def barGraphForSwaps(resultsByComplexityCase):
        # Swaps
        x = [] # Nome dos métodos
        y = [] # Número de trocas
        for result in resultsByComplexityCase["results"]:
            x.append(result["method"])
            y.append(result["swaps"])

        description = "Caso: " + resultsByComplexityCase["complexityCase"] + " - Tamanho do array: " + str(resultsByComplexityCase["lengthCase"])

        plt.bar(x, y)
        plt.xlabel("Métodos")
        plt.ylabel("Trocas")
        plt.title("Trocas x Método de ordenação\n" + description)
        plt.grid()
        return plt.show()
    
    #
    #
    #
    @staticmethod
    def barGraphForComparisons(resultsByComplexityCase):
        # Comparisons
        x = []
        y = []
        for result in resultsByComplexityCase["results"]:
            x.append(result["method"])
            y.append(result["comparisons"])
        
        description = "Caso: " + resultsByComplexityCase["complexityCase"] + " - Tamanho do array: " + str(resultsByComplexityCase["lengthCase"])

        plt.bar(x, y)
        plt.xlabel("Métodos")
        plt.ylabel("Comparações")
        plt.title("Comparações x Método de ordenação\n" + description)
        plt.grid()
        return plt.show()
    
    #
    #
    #
    @staticmethod
    def barGraphForIterations(resultsByComplexityCase):
        # Iterations
        x = []
        y = []
        for result in resultsByComplexityCase["results"]:
            x.append(result["method"])
            y.append(result["iterations"])
        
        description = "Caso: " + resultsByComplexityCase["complexityCase"] + " - Tamanho do array: " + str(resultsByComplexityCase["lengthCase"])

        plt.bar(x, y)
        plt.xlabel("Métodos")
        plt.ylabel("Iterações")
        plt.title("Iterações x Método de ordenação\n" + description)
        plt.grid()
        return plt.show()
    