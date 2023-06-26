import sys
import time
sys.path.append('./Ordenacao')
import bubbleSort
import heapSort
import insertSort
import mergeSort
import quickSort
import selectSort

from tratamentoDados import *

def execucaoBubblueSort(array):
    inicio_sequencial = time.time()
    bubbleSort.bubbleSort(array)
    valoresOrdenadosBubbleSortGrande = ', '.join(str(valor) for valor in array)
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    print("_____________________________________")
    print(f"O resultado da ordenação foi: {valoresOrdenadosBubbleSortGrande}")
    print("_____________________________________")
    print(f"O tempo de ordenação foi: {tempo_sequencial}")
    print("_____________________________________")

def execucaoHeapSort(array):
    inicio_sequencial = time.time()
    heapSort.heapSort(array)
    valoresOrdenadosHeapSortGrande = ', '.join(str(valor) for valor in array)
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    print("_____________________________________")
    print(f"O resultado da ordenação foi: {valoresOrdenadosHeapSortGrande}")
    print("_____________________________________")
    print(f"O tempo de ordenação foi: {tempo_sequencial}")
    print("_____________________________________")

def execucaoInsertSort(array):
    inicio_sequencial = time.time()
    insertSort.insertSort(array)
    valoresOrdenadosInsertSortGrande = ', '.join(str(valor) for valor in array)
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    print("_____________________________________")
    print(f"O resultado da ordenação foi: {valoresOrdenadosInsertSortGrande}")
    print("_____________________________________")
    print(f"O tempo de ordenação foi: {tempo_sequencial}")
    print("_____________________________________")

def execucaoMergeSort(array):
    inicio_sequencial = time.time()
    mergeSort.mergeSort(array)
    valoresOrdenadosMergeSortGrande = ', '.join(str(valor) for valor in array)
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    print("_____________________________________")
    print(f"O resultado da ordenação foi: {valoresOrdenadosMergeSortGrande}")
    print("_____________________________________")
    print(f"O tempo de ordenação foi: {tempo_sequencial}")
    print("_____________________________________")

def execucaoQuickSort(array):
    inicio_sequencial = time.time()
    quickSort.quickSort(array)
    valoresOrdenadosQuickSortGrande = ', '.join(str(valor) for valor in array)
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    print("_____________________________________")
    print(f"O resultado da ordenação foi: {valoresOrdenadosQuickSortGrande}")
    print("_____________________________________")
    print(f"O tempo de ordenação foi: {tempo_sequencial}")
    print("_____________________________________")

def execucaoSelectSort(array):
    inicio_sequencial = time.time()
    selectSort.selectSort(array)
    valoresOrdenadosSelectSortGrande = ', '.join(str(valor) for valor in array)
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    print("_____________________________________")
    print(f"O resultado da ordenação foi: {valoresOrdenadosSelectSortGrande}")
    print("_____________________________________")
    print(f"O tempo de ordenação foi: {tempo_sequencial}")
    print("_____________________________________")

def menu_internoOrdenacao(array):
    while True:    
        print("Opção 3 - Ordenação selecionada.")
        print("Você deseja: ")
        print("Opção 1: Executar o algoritmo de ordenação")
        print("Opção 2: Comparar o tempo de execução de dois algoritmos")
        print("Opção 3: Comparar o tempo de execução de três algoritmos")
        print("Opção 4: Comparar o tempo de execução de quatro algoritmos")
        print("Opção 5: Comparar o tempo de execução de cinco algoritmos")
        print("Opção 6: Comparar o tempo de execução dos seis algoritmos")
        print("Opção 7: Voltar ao menu inicial")
        selecao = input("Escolha uma opção: ")

        if selecao == "1":
            menu_internoOrdOp(array)
        elif selecao == "2":
            menu_interno2Op(array)
        elif selecao == "3":
            menu_interno3Op(array)
        elif selecao == "4":
            menu_interno4Op(array)
        elif selecao == "5":
            menu_interno5Op(array)      
        elif selecao == "6":
            print("Ordenando usando todos os algoritmos")
            print("1 BubbleSort")
            execucaoBubblueSort(array)
            print("2 HeapSort")
            execucaoHeapSort(array)
            print("3 InsertSort")
            execucaoInsertSort(array)                
            print("4 MergeSort")
            execucaoMergeSort(array)
            print("5 QuickSort")
            execucaoQuickSort(array)
            print("6 SelectSort")
            execucaoSelectSort(array)
        elif selecao == '7': 
            print("Voltando ao menu Listas")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True


def menu_internoOrdOp(array):
    while True:
        print("Qual ordenação deseja executar?")
        print("Opção 1: BubbleSort")
        print("Opção 2: HeapSort")
        print("Opção 3: InsertSort")
        print("Opção 4: MergeSort")
        print("Opção 5: QuickSort")
        print("Opção 6: SelectSort")
        print("Opção 7: Voltar ao menu Ordenação")
        sortEscolhido = input("Escolha uma opção:")
        if sortEscolhido == "1":   
            print("Opção 1 BubbleSort selecionada.")
            execucaoBubblueSort(array)
        elif sortEscolhido == "2":
            print("Opção 2 HeapSort selecionada.")
            inicio_sequencial = time.time()
            execucaoHeapSort(array)
        elif sortEscolhido == "3":
            print("Opção 3 InsertSort selecionada.")
            execucaoInsertSort(array)                
        elif sortEscolhido == "4":
            print("Opção 4 MergeSort selecionada.")
            execucaoMergeSort(array)
        elif sortEscolhido == "5":
            print("Opção 5 QuickSort selecionada.")
            execucaoQuickSort(array)
        elif sortEscolhido == "6":
            print("Opção 6 SelectSort selecionada.")
            execucaoSelectSort(array)
        elif sortEscolhido == "7":
            print("Voltando ao menu Listas")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True
    
def menu_interno2Op(array):
    while True:
        print("Qual ordenação deseja executar?")
        print("Opção 1: BubbleSort")
        print("Opção 2: HeapSort")
        print("Opção 3: InsertSort")
        print("Opção 4: MergeSort")
        print("Opção 5: QuickSort")
        print("Opção 6: SelectSort")
        print("Opção 7: Voltar ao menu Ordenação")
        sortEscolhido1 = input("Escolha o primeiro algoritmo: ")
        sortEscolhido2 = input("Escolha o segundo algoritmo: ")

        if sortEscolhido1 == "1" or sortEscolhido2 == "1":   
            print("Opção 1 BubbleSort selecionada.")
            execucaoBubblueSort(array)
        if sortEscolhido1 == "2" or sortEscolhido2 == "2":
            print("Opção 2 HeapSort selecionada.")
            execucaoHeapSort(array)
        if sortEscolhido1 == "3" or sortEscolhido2 == "3":
            print("Opção 3 InsertSort selecionada.")
            execucaoInsertSort(array)                
        if sortEscolhido1 == "4" or sortEscolhido2 == "4":
            print("Opção 4 MergeSort selecionada.")
            execucaoMergeSort(array)
        if sortEscolhido1 == "5" or sortEscolhido2 == "5":
            print("Opção 5 QuickSort selecionada.")
            execucaoQuickSort(array)
        if sortEscolhido1 == "6" or sortEscolhido2 == "6":
            print("Opção 6 SelectSort selecionada.")
            execucaoSelectSort(array)
        elif sortEscolhido1 == '7' or sortEscolhido2 == '7': 
            print("Voltando ao menu Listas")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True
    
def menu_interno3Op(array):
    while True:
        print("Qual ordenação deseja executar?")
        print("Opção 1: BubbleSort")
        print("Opção 2: HeapSort")
        print("Opção 3: InsertSort")
        print("Opção 4: MergeSort")
        print("Opção 5: QuickSort")
        print("Opção 6: SelectSort")
        print("Opção 7: Voltar ao menu Ordenação")
        sortEscolhido1 = input("Escolha o primeiro algoritmo: ")
        sortEscolhido2 = input("Escolha o segundo algoritmo: ")
        sortEscolhido3 = input("Escolha o segundo algoritmo: ")

        if sortEscolhido1 == "1" or sortEscolhido2 == "1" or sortEscolhido3 == "1":   
            print("Opção 1 BubbleSort selecionada.")
            execucaoBubblueSort(array)
        if sortEscolhido1 == "2" or sortEscolhido2 == "2" or sortEscolhido3 == "2":
            print("Opção 2 HeapSort selecionada.")
            execucaoHeapSort(array)
        if sortEscolhido1 == "3" or sortEscolhido2 == "3" or sortEscolhido3 == "3":
            print("Opção 3 InsertSort selecionada.")
            execucaoInsertSort(array)                
        if sortEscolhido1 == "4" or sortEscolhido2 == "4" or sortEscolhido3 == "4":
            print("Opção 4 MergeSort selecionada.")
            execucaoMergeSort(array)
        if sortEscolhido1 == "5" or sortEscolhido2 == "5" or sortEscolhido3 == "5":
            print("Opção 5 QuickSort selecionada.")
            execucaoQuickSort(array)
        if sortEscolhido1 == "6" or sortEscolhido2 == "6" or sortEscolhido3 == "6":
            print("Opção 6 SelectSort selecionada.")
            execucaoSelectSort(array)
        elif sortEscolhido1 == '7' or sortEscolhido2 == '7' or sortEscolhido3 == "7": 
            print("Voltando ao menu Listas")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True
    
def menu_interno4Op(array):
    while True:
        print("Qual ordenação deseja executar?")
        print("Opção 1: BubbleSort")
        print("Opção 2: HeapSort")
        print("Opção 3: InsertSort")
        print("Opção 4: MergeSort")
        print("Opção 5: QuickSort")
        print("Opção 6: SelectSort")
        sortEscolhido1 = input("Escolha o primeiro algoritmo: ")
        sortEscolhido2 = input("Escolha o segundo algoritmo: ")
        sortEscolhido3 = input("Escolha o segundo algoritmo: ")
        sortEscolhido4 = input("Escolha o segundo algoritmo: ")

        if sortEscolhido1 == "1" or sortEscolhido2 == "1" or sortEscolhido3 == "1" or sortEscolhido4 == "1":   
            print("Opção 1 BubbleSort selecionada.")
            execucaoBubblueSort(array)
        if sortEscolhido1 == "2" or sortEscolhido2 == "2" or sortEscolhido3 == "2" or sortEscolhido4 == "2":
            print("Opção 2 HeapSort selecionada.")
            execucaoHeapSort(array)
        if sortEscolhido1 == "3" or sortEscolhido2 == "3" or sortEscolhido3 == "3" or sortEscolhido4 == "3":
            print("Opção 3 InsertSort selecionada.")
            execucaoInsertSort(array)                
        if sortEscolhido1 == "4" or sortEscolhido2 == "4" or sortEscolhido3 == "4" or sortEscolhido4 == "4":
            print("Opção 4 MergeSort selecionada.")
            execucaoMergeSort(array)
        if sortEscolhido1 == "5" or sortEscolhido2 == "5" or sortEscolhido3 == "5" or sortEscolhido4 == "5":
            print("Opção 5 QuickSort selecionada.")
            execucaoQuickSort(array)
        if sortEscolhido1 == "6" or sortEscolhido2 == "6" or sortEscolhido3 == "6" or sortEscolhido4 == "6":
            print("Opção 6 SelectSort selecionada.")
            execucaoSelectSort(array)
        elif sortEscolhido1 == '7' or sortEscolhido2 == '7' or sortEscolhido3 == "7" or sortEscolhido4 == "7": 
            print("Voltando ao menu Listas")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True
    
def menu_interno5Op(array):
    while True:
        print("Qual ordenação deseja executar?")
        print("Opção 1: BubbleSort")
        print("Opção 2: HeapSort")
        print("Opção 3: InsertSort")
        print("Opção 4: MergeSort")
        print("Opção 5: QuickSort")
        print("Opção 6: SelectSort")
        sortEscolhido1 = input("Escolha o primeiro algoritmo: ")
        sortEscolhido2 = input("Escolha o segundo algoritmo: ")
        sortEscolhido3 = input("Escolha o terceiro algoritmo: ")
        sortEscolhido4 = input("Escolha o quarto algoritmo: ")
        sortEscolhido5 = input("Escolha o quinto algoritmo: ")

        if sortEscolhido1 == "1" or sortEscolhido2 == "1" or sortEscolhido3 == "1" or sortEscolhido4 == "1" or sortEscolhido5 == "1":   
            print("Opção 1 BubbleSort selecionada.")
            execucaoBubblueSort(array)
        if sortEscolhido1 == "2" or sortEscolhido2 == "2" or sortEscolhido3 == "2" or sortEscolhido4 == "2" or sortEscolhido5 == "2":
            print("Opção 2 HeapSort selecionada.")
            execucaoHeapSort(array)
        if sortEscolhido1 == "3" or sortEscolhido2 == "3" or sortEscolhido3 == "3" or sortEscolhido4 == "3" or sortEscolhido5 == "3":
            print("Opção 3 InsertSort selecionada.")
            execucaoInsertSort(array)                
        if sortEscolhido1 == "4" or sortEscolhido2 == "4" or sortEscolhido3 == "4" or sortEscolhido4 == "4" or sortEscolhido5 == "4":
            print("Opção 4 MergeSort selecionada.")
            execucaoMergeSort(array)
        if sortEscolhido1 == "5" or sortEscolhido2 == "5" or sortEscolhido3 == "5" or sortEscolhido4 == "5" or sortEscolhido5 == "5":
            print("Opção 5 QuickSort selecionada.")
            execucaoQuickSort(array)
        if sortEscolhido1 == "6" or sortEscolhido2 == "6" or sortEscolhido3 == "6" or sortEscolhido4 == "6" or sortEscolhido5 == "6":
            print("Opção 6 SelectSort selecionada.")
            execucaoSelectSort(array) 
        elif sortEscolhido1 == '7' or sortEscolhido2 == '7' or sortEscolhido3 == "7" or sortEscolhido4 == "7" or sortEscolhido5 == "7": 
            print("Voltando ao menu Listas")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True