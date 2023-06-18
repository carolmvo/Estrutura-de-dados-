import sys
sys.path.append('./Ordenacao')
sys.path.append('./Pesquisa')
import bubbleSort
import heapSort
import insertSort
import mergeSort
import quickSort
import selectSort
# import NOT_FOUND
import buscaEmDesordenacao
import buscaEmOrdenacao
# import iterativeBinarySearch
# import scanSequencial
from troca import swap
from tratamentoDados import *


# BubbleSort
    #Arquivo Desordenado Grande
bubbleSort.bubbleSort(listaNumericaDesordenadoGrande)

listaStringBubbleSortGrande = str(listaNumericaDesordenadoGrande)
valoresOrdenadosBubbleSortGrande = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrande)
with open('./resultado/bubbleSort/conteudoDesordenadoGrande.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosBubbleSortGrande)


    #Arquivo Desordenado Grande Positivo
bubbleSort.bubbleSort(listaNumericaDesordenadoGrandePositivo)

listaStringBubbleSortGrandePositivo = str(listaNumericaDesordenadoGrandePositivo)
valoresOrdenadosBubbleSortGrandePositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandePositivo)
with open('./resultado/bubbleSort/conteudoDesordenadoGrandePositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosBubbleSortGrandePositivo)


    #Arquivo Desordenado Grande Negativo
bubbleSort.bubbleSort(listaNumericaDesordenadoGrandeNegativo)

listaStringBubbleSortGrandeNegativo = str(listaNumericaDesordenadoGrandeNegativo)
valoresOrdenadosBubbleSortGrandeNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandeNegativo)
with open('./resultado/bubbleSort/conteudoDesordenadoGrandeNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosBubbleSortGrandeNegativo)


    #Arquivo Desordenado Pequeno
bubbleSort.bubbleSort(listaNumericaDesordenadoPequeno)

listaStringBubbleSortPequeno = str(listaNumericaDesordenadoPequeno)
valoresOrdenadosBubbleSortPequeno = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequeno)
with open('./resultado/bubbleSort/conteudoDesordenadoPequeno.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosBubbleSortPequeno)


        #Arquivo Desordenado Pequeno Positivo
bubbleSort.bubbleSort(listaNumericaDesordenadoPequenoPositivo)

listaStringBubbleSortPequenoPositivo = str(listaNumericaDesordenadoPequenoPositivo)
valoresOrdenadosBubbleSortPequenoPositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoPositivo)
with open('./resultado/bubbleSort/conteudoDesordenadoPequenoPositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosBubbleSortPequenoPositivo)


        #Arquivo Desordenado Pequeno Negativo
bubbleSort.bubbleSort(listaNumericaDesordenadoPequenoNegativo)

listaStringBubbleSortPequenoNegativo = str(listaNumericaDesordenadoPequenoNegativo)
valoresOrdenadosBubbleSortPequenoNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoNegativo)
with open('./resultado/bubbleSort/conteudoDesordenadoPequenoNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosBubbleSortPequenoNegativo)



# HeapSort
    #Arquivo Desordenado Grande
heapSort.heapSort(listaNumericaDesordenadoGrande)

listaStringHeapSortGrande = str(listaNumericaDesordenadoGrande)
valoresOrdenadosHeapSortGrande = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrande)
with open('./resultado/heapSort/conteudoDesordenadoGrande.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosHeapSortGrande)


    #Arquivo Desordenado Grande Positivo
heapSort.heapSort(listaNumericaDesordenadoGrandePositivo)

listaStringHeapSortGrandePositivo = str(listaNumericaDesordenadoGrandePositivo)
valoresOrdenadosHeapSortGrandePositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandePositivo)
with open('./resultado/heapSort/conteudoDesordenadoGrandePositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosHeapSortGrandePositivo)


    #Arquivo Desordenado Grande Negativo
heapSort.heapSort(listaNumericaDesordenadoGrandeNegativo)

listaStringHeapSortGrandeNegativo = str(listaNumericaDesordenadoGrandeNegativo)
valoresOrdenadosHeapSortGrandeNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandeNegativo)
with open('./resultado/heapSort/conteudoDesordenadoGrandeNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosHeapSortGrandeNegativo)


    #Arquivo Desordenado Pequeno
heapSort.heapSort(listaNumericaDesordenadoPequeno)

listaStringHeapSortPequeno = str(listaNumericaDesordenadoPequeno)
valoresOrdenadosHeapSortPequeno = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequeno)
with open('./resultado/heapSort/conteudoDesordenadoPequeno.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosHeapSortPequeno)


        #Arquivo Desordenado Pequeno Positivo
heapSort.heapSort(listaNumericaDesordenadoPequenoPositivo)

listaStringHeapSortPequenoPositivo = str(listaNumericaDesordenadoPequenoPositivo)
valoresOrdenadosHeapSortPequenoPositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoPositivo)
with open('./resultado/heapSort/conteudoDesordenadoPequenoPositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosHeapSortPequenoPositivo)


        #Arquivo Desordenado Pequeno Negativo
heapSort.heapSort(listaNumericaDesordenadoPequenoNegativo)

listaStringHeapSortPequenoNegativo = str(listaNumericaDesordenadoPequenoNegativo)
valoresOrdenadosHeapSortPequenoNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoNegativo)
with open('./resultado/heapSort/conteudoDesordenadoPequenoNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosHeapSortPequenoNegativo)


# InsertSort
    #Arquivo Desordenado Grande
insertSort.insertSort(listaNumericaDesordenadoGrande)

listaStringInsertSortGrande = str(listaNumericaDesordenadoGrande)
valoresOrdenadosInsertSortGrande = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrande)
with open('./resultado/insertSort/conteudoDesordenadoGrande.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosInsertSortGrande)


    #Arquivo Desordenado Grande Positivo
insertSort.insertSort(listaNumericaDesordenadoGrandePositivo)

listaStringInsertSortGrandePositivo = str(listaNumericaDesordenadoGrandePositivo)
valoresOrdenadosInsertSortGrandePositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandePositivo)
with open('./resultado/insertSort/conteudoDesordenadoGrandePositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosInsertSortGrandePositivo)


    #Arquivo Desordenado Grande Negativo
insertSort.insertSort(listaNumericaDesordenadoGrandeNegativo)

listaStringInsertSortGrandeNegativo = str(listaNumericaDesordenadoGrandeNegativo)
valoresOrdenadosInsertSortGrandeNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandeNegativo)
with open('./resultado/insertSort/conteudoDesordenadoGrandeNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosInsertSortGrandeNegativo)


    #Arquivo Desordenado Pequeno
insertSort.insertSort(listaNumericaDesordenadoPequeno)

listaStringInsertSortPequeno = str(listaNumericaDesordenadoPequeno)
valoresOrdenadosInsertSortPequeno = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequeno)
with open('./resultado/insertSort/conteudoDesordenadoPequeno.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosInsertSortPequeno)


        #Arquivo Desordenado Pequeno Positivo
insertSort.insertSort(listaNumericaDesordenadoPequenoPositivo)

listaStringInsertSortPequenoPositivo = str(listaNumericaDesordenadoPequenoPositivo)
valoresOrdenadosInsertSortPequenoPositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoPositivo)
with open('./resultado/insertSort/conteudoDesordenadoPequenoPositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosInsertSortPequenoPositivo)


        #Arquivo Desordenado Pequeno Negativo
insertSort.insertSort(listaNumericaDesordenadoPequenoNegativo)

listaStringInsertSortPequenoNegativo = str(listaNumericaDesordenadoPequenoNegativo)
valoresOrdenadosInsertSortPequenoNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoNegativo)
with open('./resultado/insertSort/conteudoDesordenadoPequenoNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosInsertSortPequenoNegativo)


# MergeSort
    #Arquivo Desordenado Grande
mergeSort.mergeSort(listaNumericaDesordenadoGrande)

listaStringMergeSortGrande = str(listaNumericaDesordenadoGrande)
valoresOrdenadosMergeSortGrande = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrande)
with open('./resultado/mergeSort/conteudoDesordenadoGrande.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosMergeSortGrande)


    #Arquivo Desordenado Grande Positivo
mergeSort.mergeSort(listaNumericaDesordenadoGrandePositivo)

listaStringMergeSortGrandePositivo = str(listaNumericaDesordenadoGrandePositivo)
valoresOrdenadosMergeSortGrandePositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandePositivo)
with open('./resultado/mergeSort/conteudoDesordenadoGrandePositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosMergeSortGrandePositivo)


    #Arquivo Desordenado Grande Negativo
mergeSort.mergeSort(listaNumericaDesordenadoGrandeNegativo)

listaStringMergeSortGrandeNegativo = str(listaNumericaDesordenadoGrandeNegativo)
valoresOrdenadosMergeSortGrandeNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandeNegativo)
with open('./resultado/mergeSort/conteudoDesordenadoGrandeNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosMergeSortGrandeNegativo)


    #Arquivo Desordenado Pequeno
mergeSort.mergeSort(listaNumericaDesordenadoPequeno)

listaStringMergeSortPequeno = str(listaNumericaDesordenadoPequeno)
valoresOrdenadosMergeSortPequeno = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequeno)
with open('./resultado/mergeSort/conteudoDesordenadoPequeno.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosMergeSortPequeno)


        #Arquivo Desordenado Pequeno Positivo
mergeSort.mergeSort(listaNumericaDesordenadoPequenoPositivo)

listaStringMergeSortPequenoPositivo = str(listaNumericaDesordenadoPequenoPositivo)
valoresOrdenadosMergeSortPequenoPositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoPositivo)
with open('./resultado/mergeSort/conteudoDesordenadoPequenoPositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosMergeSortPequenoPositivo)


        #Arquivo Desordenado Pequeno Negativo
mergeSort.mergeSort(listaNumericaDesordenadoPequenoNegativo)

listaStringMergeSortPequenoNegativo = str(listaNumericaDesordenadoPequenoNegativo)
valoresOrdenadosMergeSortPequenoNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoNegativo)
with open('./resultado/mergeSort/conteudoDesordenadoPequenoNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosMergeSortPequenoNegativo)



# QuickSort
    #Arquivo Desordenado Grande
quickSort.quickSort(listaNumericaDesordenadoGrande)

listaStringQuickSortGrande = str(listaNumericaDesordenadoGrande)
valoresOrdenadosQuickSortGrande = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrande)
with open('./resultado/quickSort/conteudoDesordenadoGrande.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosQuickSortGrande)


    #Arquivo Desordenado Grande Positivo
quickSort.quickSort(listaNumericaDesordenadoGrandePositivo)

listaStringQuickSortGrandePositivo = str(listaNumericaDesordenadoGrandePositivo)
valoresOrdenadosQuickSortGrandePositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandePositivo)
with open('./resultado/quickSort/conteudoDesordenadoGrandePositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosQuickSortGrandePositivo)


    #Arquivo Desordenado Grande Negativo
quickSort.quickSort(listaNumericaDesordenadoGrandeNegativo)

listaStringQuickSortGrandeNegativo = str(listaNumericaDesordenadoGrandeNegativo)
valoresOrdenadosQuickSortGrandeNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandeNegativo)
with open('./resultado/quickSort/conteudoDesordenadoGrandeNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosQuickSortGrandeNegativo)


    #Arquivo Desordenado Pequeno
quickSort.quickSort(listaNumericaDesordenadoPequeno)

listaStringQuickSortPequeno = str(listaNumericaDesordenadoPequeno)
valoresOrdenadosQuickSortPequeno = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequeno)
with open('./resultado/quickSort/conteudoDesordenadoPequeno.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosQuickSortPequeno)


        #Arquivo Desordenado Pequeno Positivo
quickSort.quickSort(listaNumericaDesordenadoPequenoPositivo)

listaStringQuickSortPequenoPositivo = str(listaNumericaDesordenadoPequenoPositivo)
valoresOrdenadosQuickSortPequenoPositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoPositivo)
with open('./resultado/quickSort/conteudoDesordenadoPequenoPositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosQuickSortPequenoPositivo)


        #Arquivo Desordenado Pequeno Negativo
quickSort.quickSort(listaNumericaDesordenadoPequenoNegativo)

listaStringQuickSortPequenoNegativo = str(listaNumericaDesordenadoPequenoNegativo)
valoresOrdenadosQuickSortPequenoNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoNegativo)
with open('./resultado/quickSort/conteudoDesordenadoPequenoNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosQuickSortPequenoNegativo)


# SelectSort
    #Arquivo Desordenado Grande
selectSort.selectSort(listaNumericaDesordenadoGrande)

listaStringSelectSortGrande = str(listaNumericaDesordenadoGrande)
valoresOrdenadosSelectSortGrande = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrande)
with open('./resultado/selectSort/conteudoDesordenadoGrande.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosSelectSortGrande)


    #Arquivo Desordenado Grande Positivo
selectSort.selectSort(listaNumericaDesordenadoGrandePositivo)

listaStringSelectSortGrandePositivo = str(listaNumericaDesordenadoGrandePositivo)
valoresOrdenadosSelectSortGrandePositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandePositivo)
with open('./resultado/selectSort/conteudoDesordenadoGrandePositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosSelectSortGrandePositivo)


    #Arquivo Desordenado Grande Negativo
selectSort.selectSort(listaNumericaDesordenadoGrandeNegativo)

listaStringSelectSortGrandeNegativo = str(listaNumericaDesordenadoGrandeNegativo)
valoresOrdenadosSelectSortGrandeNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoGrandeNegativo)
with open('./resultado/selectSort/conteudoDesordenadoGrandeNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosSelectSortGrandeNegativo)


    #Arquivo Desordenado Pequeno
selectSort.selectSort(listaNumericaDesordenadoPequeno)

listaStringSelectSortPequeno = str(listaNumericaDesordenadoPequeno)
valoresOrdenadosSelectSortPequeno = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequeno)
with open('./resultado/selectSort/conteudoDesordenadoPequeno.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosSelectSortPequeno)


        #Arquivo Desordenado Pequeno Positivo
selectSort.selectSort(listaNumericaDesordenadoPequenoPositivo)

listaStringSelectSortPequenoPositivo = str(listaNumericaDesordenadoPequenoPositivo)
valoresOrdenadosSelectSortPequenoPositivo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoPositivo)
with open('./resultado/selectSort/conteudoDesordenadoPequenoPositivo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosSelectSortPequenoPositivo)


        #Arquivo Desordenado Pequeno Negativo
selectSort.selectSort(listaNumericaDesordenadoPequenoNegativo)

listaStringSelectSortPequenoNegativo = str(listaNumericaDesordenadoPequenoNegativo)
valoresOrdenadosSelectSortPequenoNegativo = ', '.join(str(valor) for valor in listaNumericaDesordenadoPequenoNegativo)
with open('./resultado/selectSort/conteudoDesordenadoPequenoNegativo.txt', 'w') as arquivo:
    arquivo.write(valoresOrdenadosSelectSortPequenoNegativo)
