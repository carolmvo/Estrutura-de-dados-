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




