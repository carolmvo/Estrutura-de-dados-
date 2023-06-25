
import sys
import time
sys.path.append('./Pesquisa')
import pesquisaBinaria
import pesquisaSequencial
from tratamentoDados import *


def execucaoPesquisaBinaria(array, num):
    inicio_sequencial = time.time()
    buscaBinaria = pesquisaBinaria.iterativeBinarySearch(array, num)
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    if buscaBinaria >= 0:
        print(f"O número {num} se encontra no índice {buscaBinaria}")
        print(f"O tempo de execução foi de {tempo_sequencial}")
    else:
        print(f"O número {num} não se encontra no arquvio")
        print(f"O tempo de execução foi de {tempo_sequencial}")

def execucaoPesquisaSequencial(array, num):
    inicio_sequencial = time.time()
    buscaSequencial = pesquisaSequencial.scanSequencial(array, num)
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    if buscaSequencial >= 0:
        print(f"O número {num} se encontra no índice {buscaSequencial}")
        print(f"O tempo de execução foi de {tempo_sequencial}")
    else:
        print(f"O número {num} não se encontra no arquvio")
        print(f"O tempo de execução foi de {tempo_sequencial}")

def menu_internoPesquisa(array):
    while True:
        print("Você deseja: ")
        print("Opção 1: Executar o algoritmo de pesquisa")
        print("Opção 2: Comparar o tempo de execução das duas pesquisas")
        print("Opção 3: Voltar ao menu inicial")
        selecaoPesquisa = input("Escolha uma opção: ")

        if selecaoPesquisa == "1":
            menu_internoAlgPesquisa(array)
        elif selecaoPesquisa == "2":
            num = int(input("Digite o número que procura: "))
            print("Pesquisa binária:")
            execucaoPesquisaBinaria(array, num)
            print("Pesquisa sequencial:")
            execucaoPesquisaSequencial(array, num)
        elif selecao == '3': 
            print("Voltando ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True
    

def menu_internoAlgPesquisa(array):
    while True:
        print("Opção 1: Pesquisa binária")
        print("Opção 2: Pesquisa sequencial")
        print("Opção 3: Voltar ao menu Pesquisa")
        escolhaPesquisa = input("Escolha uma opção: ")
        if escolhaPesquisa == "1":
            num = int(input("Digite o número que procura: "))
            execucaoPesquisaBinaria(num)
        elif escolhaPesquisa == "2":
            num = int(input("Digite o número que procura: "))
            execucaoPesquisaSequencial(num)
        elif escolhaPesquisa == '3': 
            print("Voltando ao menu Pesquisa")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True
        