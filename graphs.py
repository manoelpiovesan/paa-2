import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd
import csv  # Importando o módulo csv
import os
import trabalho2

def plot_graphs_for_each_csv(file_paths):
    # Crie uma pasta para salvar os gráficos, se ainda não existir
    if not os.path.exists('graphs'):
        os.makedirs('graphs')

    for file_path in file_paths:
        # Lendo o arquivo CSV
        df = pd.read_csv(file_path)

        # Plotando os gráficos
        plt.figure(figsize=(12, 8))
        plt.suptitle(f'Sorting Results: {file_path}', fontsize=16)

        # Gráfico de comparações
        plt.subplot(2, 2, 1)
        plt.bar(df['Algorithm'], df['Comparisons'], color='blue')
        plt.title('Comparisons')
        plt.xlabel('Algorithm')
        plt.ylabel('Comparisons')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Gráfico de trocas
        plt.subplot(2, 2, 2)
        plt.bar(df['Algorithm'], df['Swaps'], color='green')
        plt.title('Swaps')
        plt.xlabel('Algorithm')
        plt.ylabel('Swaps')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Gráfico de memória consumida
        plt.subplot(2, 2, 3)
        plt.bar(df['Algorithm'], df['Memory Consumed'], color='orange')
        plt.title('Memory Consumed')
        plt.xlabel('Algorithm')
        plt.ylabel('Memory Consumed (bytes)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Gráfico de CPU consumida
        plt.subplot(2, 2, 4)
        plt.bar(df['Algorithm'], df['CPU Consumed'], color='red')
        plt.title('CPU Consumed')
        plt.xlabel('Algorithm')
        plt.ylabel('CPU Consumed (%)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Salvar o gráfico com o mesmo nome do arquivo CSV na pasta 'graphs'
        file_name = os.path.basename(file_path).replace('.csv', '')
        plt.savefig(f'graphs/{file_name}.png')

        # Limpar a figura para liberar memória
        plt.clf()

    # Fechar todas as figuras para evitar acumulação de memória
    plt.close('all')


file_paths = [
    'sorting_results_100_totalmente_ordenado_crescentemente.csv',
    'sorting_results_100_totalmente_ordenado_decrescentemente.csv',
    'sorting_results_100_totalmente_aleatório_desordenado.csv',
    'sorting_results_100_50%_ordenado_do_início_ao_meio,_com_o_meio_para_o_final_aleatório.csv',
    'sorting_results_100_50%_ordenado_do_meio_ao_final,_com_o_início_até_o_meio_aleatório.csv',
    'sorting_results_100_25%_ordenado_apenas_no_início.csv',
    'sorting_results_100_25%_ordenado_no_final.csv',
    'sorting_results_100_25%_ordenado_no_meio.csv',
    'sorting_results_1000_totalmente_ordenado_crescentemente.csv',
    'sorting_results_1000_totalmente_ordenado_decrescentemente.csv',
    'sorting_results_1000_totalmente_aleatório_desordenado.csv',
    'sorting_results_1000_50%_ordenado_do_início_ao_meio,_com_o_meio_para_o_final_aleatório.csv',
    'sorting_results_1000_50%_ordenado_do_meio_ao_final,_com_o_início_até_o_meio_aleatório.csv',
    'sorting_results_1000_25%_ordenado_apenas_no_início.csv',
    'sorting_results_1000_25%_ordenado_no_final.csv',
    'sorting_results_1000_25%_ordenado_no_meio.csv',
    'sorting_results_5000_totalmente_ordenado_crescentemente.csv',
    'sorting_results_5000_totalmente_ordenado_decrescentemente.csv',
    'sorting_results_5000_totalmente_aleatório_desordenado.csv',
    'sorting_results_5000_50%_ordenado_do_início_ao_meio,_com_o_meio_para_o_final_aleatório.csv',
    'sorting_results_5000_50%_ordenado_do_meio_ao_final,_com_o_início_até_o_meio_aleatório.csv',
    'sorting_results_5000_25%_ordenado_apenas_no_início.csv',
    'sorting_results_5000_25%_ordenado_no_final.csv',
    'sorting_results_5000_25%_ordenado_no_meio.csv',
    'sorting_results_10000_totalmente_ordenado_crescentemente.csv',
    'sorting_results_10000_totalmente_ordenado_decrescentemente.csv',
    'sorting_results_10000_totalmente_aleatório_desordenado.csv',
    'sorting_results_10000_50%_ordenado_do_início_ao_meio,_com_o_meio_para_o_final_aleatório.csv',
    'sorting_results_10000_50%_ordenado_do_meio_ao_final,_com_o_início_até_o_meio_aleatório.csv',
    'sorting_results_10000_25%_ordenado_apenas_no_início.csv',
    'sorting_results_10000_25%_ordenado_no_final.csv',
    'sorting_results_10000_25%_ordenado_no_meio.csv'
    # Adicione aqui os caminhos para os arquivos CSV gerados
]

plot_graphs_for_each_csv(file_paths)
