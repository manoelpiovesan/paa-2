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

        description = resultsByComplexityCase["complexityCase"] + " para " + str(resultsByComplexityCase["lengthCase"]) + " elementos."

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
        
        description = resultsByComplexityCase["complexityCase"] + " para " + str(resultsByComplexityCase["lengthCase"]) + " elementos."

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
        
        description = resultsByComplexityCase["complexityCase"] + " para " + str(resultsByComplexityCase["lengthCase"]) + " elementos."

        plt.bar(x, y)
        plt.xlabel("Métodos")
        plt.ylabel("Iterações")
        plt.title("Iterações x Método de ordenação\n" + description)
        plt.grid()
        return plt.show()
    
    #
    # 
    #
    @staticmethod
    def barGraphForAll(resultsByComplexityCase):
        xGeneric = []
        ySwaps = []
        yComparisons = []
        yIterations = []

        for result in resultsByComplexityCase["results"]:
            ySwaps.append(result["iterations"])
            yComparisons.append(result["comparisons"])
            yIterations.append(result["iterations"])

            xGeneric.append(result["method"])
        
        description = resultsByComplexityCase["complexityCase"] + " para " + str(resultsByComplexityCase["lengthCase"]) + " elementos."

        fig, (swapsGraph, comparisonsGraph, iterationsGraph) = plt.subplots(3)

        swapsGraph.bar(xGeneric, ySwaps)
        swapsGraph.set_title(description +"\n\nTrocas x Método de ordenação")

        comparisonsGraph.bar(xGeneric, yComparisons)
        comparisonsGraph.set_title("Comparações x Método de ordenação")

        iterationsGraph.bar(xGeneric, yIterations)
        iterationsGraph.set_title("Iterações x Método de ordenação")

        plt.tight_layout()
        plt.show()
