import random

from Ordenacao import bubbleSort
from Ordenacao import heapSort
from Ordenacao import insertSort
from Ordenacao import mergeSort
from Ordenacao import quickSort
from Ordenacao import selectSort
import time


class Relatorio:
    def __init__(self):
        self.lista = []
        self.listaDesordenadosGrande = []

        with open('../txt/arquivoDesordenadoGrande.txt', 'r') as arquivo:
            arquivoLista = [int(valor.strip()) for valor in list(arquivo.read().split(','))]
            bubbleSort.bubbleSort(arquivoLista)
            arquivo.close()
            self.listaDesordenadosGrande = arquivoLista

    def calcularTempoBubbleSort(self):
        inicio = time.time()
        bubbleSort.bubbleSort(self.listaDesordenadosGrande)
        fim = time.time()
        tempo = fim - inicio
        self.appendLista("bubble_sort", tempo)
        return tempo

    def calcularTempoHeapSort(self):
        inicio = time.time()
        heapSort.heapSort(self.listaDesordenadosGrande)
        fim = time.time()
        tempo = fim - inicio
        self.appendLista("heap_sort", tempo)
        return tempo

    def calcularTempoInsertSort(self):
        inicio = time.time()
        insertSort.insertSort(self.listaDesordenadosGrande)
        fim = time.time()
        tempo = fim - inicio
        self.appendLista("insert_sort", tempo)
        return tempo

    def calcularTempoMergeSort(self):
        inicio = time.time()
        mergeSort.mergeSort(self.listaDesordenadosGrande)
        fim = time.time()
        tempo = fim - inicio
        self.appendLista("merge_sort", tempo)
        return tempo

    def calcularTempoQuickSort(self):
        inicio = time.time()
        quickSort.quickSort(self.listaDesordenadosGrande)
        fim = time.time()
        tempo = fim - inicio
        self.appendLista("quick_sort", tempo)
        return tempo

    def calcularTempoSelectSort(self):
        inicio = time.time()
        selectSort.selectSort(self.listaDesordenadosGrande)
        fim = time.time()
        tempo = fim - inicio
        self.appendLista("select_sort", tempo)
        return tempo

    def calcularMaiorTempo(self):
        maiorTempo = self.lista[0]["tempo"]
        for i in self.lista:
            if i["tempo"] > maiorTempo:
                maiorTempo = i["tempo"]

        return maiorTempo

    def calcularMenorTempo(self):
        menorTempo = self.lista[0]["tempo"]
        for i in self.lista:
            if i["tempo"] < menorTempo:
                menorTempo = i["tempo"]
        return menorTempo

    def appendLista(self, metodo, tempo):
        existe = False
        for i in self.lista:
            if(i["metodo"] == metodo):
                existe = True
                break

        if not existe:
            self.lista.append({"metodo": metodo, "tempo": tempo})
        else:
            raise Exception("já existe esse metodo")


    def inserirEOrdernar(self, metodoOrdernacao, item, array):

        inicio = time.time()
        array.append(item)

        match metodoOrdernacao:

            case "merge_sort":
                mergeSort.mergeSort(array)
            case "quick_sort":
                quickSort.quickSort(array)
            case "heap_sort":
                heapSort.heapSort(array)
            case "select_sort":
                selectSort.selectSort(array)
            case "insert_sort":
                insertSort.insertSort(array)
            case "bubble_sort":
                bubbleSort.bubbleSort(array)
            case _:
                print("valor invalido")

        fim = time.time()
        return fim - inicio

    def removerEOrdernar(self, metodoOrdernacao, item, array):

        inicio = time.time()
        array.remove(item)

        match metodoOrdernacao:

            case "merge_sort":
                mergeSort.mergeSort(array)
            case "quick_sort":
                quickSort.quickSort(array)
            case "heap_sort":
                heapSort.heapSort(array)
            case "select_sort":
                selectSort.selectSort(array)
            case "insert_sort":
                insertSort.insertSort(array)
            case "bubble_sort":
                bubbleSort.bubbleSort(array)
            case _:
                print("valor invalido")

        fim = time.time()
        return fim - inicio


    def maiorTempoInserirEOrdernar(self, lista):
        try:
            maiorTempo = lista[0]
            for i in self.lista:
                tempo = self.inserirEOrdernar(i['metodo'], random.randint(-10000, 10000), lista)
                if(tempo > maiorTempo):
                    maiorTempo = tempo

            return maiorTempo
        except Exception as ex:
            print(ex)

    def menorTempoInserirEOrdenar(self, lista):
        try:
            menorTempo = lista[0]
            for i in self.lista:
                tempo = self.inserirEOrdernar(i['metodo'], random.randint(-10000, 10000), lista)
                if(tempo < menorTempo):
                    menorTempo = tempo

            return menorTempo
        except Exception as ex:
            print(ex)


    def maiorTempoRemoverEOrdernar(self, lista, itemToRemove):
        try:
            maiorTempo = lista[0]
            for i in self.lista:
                tempo = self.removerEOrdernar(i['metodo'], itemToRemove, lista)
                lista.append(itemToRemove)
                if(tempo > maiorTempo):
                    maiorTempo = tempo

            return maiorTempo
        except Exception as ex:
            print(ex)

    def menorTempoRemoverEOrdenar(self, lista, itemToRemove):
        try:
            menorTempo = lista[0]
            for i in self.lista:
                tempo = self.removerEOrdernar(i['metodo'], itemToRemove, lista)
                lista.append(itemToRemove)
                if(tempo < menorTempo):
                    menorTempo = tempo

            return menorTempo
        except Exception as ex:
            print(ex)





relatorio = Relatorio()
bubbleSortTempo = relatorio.calcularTempoBubbleSort()
heapSortTempo = relatorio.calcularTempoHeapSort()
selectSortTempo = relatorio.calcularTempoSelectSort()
quickSortTempo = relatorio.calcularTempoQuickSort()
insertSortTempo = relatorio.calcularTempoInsertSort()
mergeSortTempo = relatorio.calcularTempoMergeSort()

menorTempo = relatorio.calcularMenorTempo()
maiorTempo = relatorio.calcularMaiorTempo()

print(maiorTempo)
print(menorTempo)
print(relatorio.listaDesordenadosGrande)

print(relatorio.inserirEOrdernar("insert_sort", 89, relatorio.listaDesordenadosGrande))
print(relatorio.maiorTempoInserirEOrdernar(relatorio.listaDesordenadosGrande))
print(relatorio.menorTempoInserirEOrdenar(relatorio.listaDesordenadosGrande))
print(relatorio.removerEOrdernar("insert_sort", -1980, relatorio.listaDesordenadosGrande))
print(relatorio.menorTempoRemoverEOrdenar(relatorio.listaDesordenadosGrande, 355))
print(relatorio.maiorTempoRemoverEOrdernar(relatorio.listaDesordenadosGrande, 355))
