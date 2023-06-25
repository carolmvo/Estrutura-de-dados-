import sys
# import time
# sys.path.append('./Ordenacao')
# sys.path.append('./Pesquisa')
# sys.path.append('./Arvore')
# import bubbleSort
# import heapSort
# import insertSort
# import mergeSort
# import quickSort
# import selectSort
# import pesquisaBinaria
# import pesquisaSequencial
# import arvoreBinariaBusca
# import arvoreAVL
# import pilha
# import fila
from menuLista import * 
from tratamentoDados import *
from menuOrdenacao import *
from menuPesquisa import *
from menuMatriz import *
from menuArquivos import *


def exibir_menu():
    print("Menu:")
    print("1. Listas")
    print("2. Matriz")
    print("3. Ordenação")
    print("4. Pesquisa e busca")
    print("5. Árvore")
    print("6. Outras opções")
    print("7. Sair")
    print()

def escolher_opcao():
    opcao = input("Escolha uma opção: ")
    return opcao

def processar_opcao(opcao):
    if opcao == "1":
        print("Opção 1 - Listas selecionada.")
        array = menu_internoArquivos()
        menu_internoLista(array)                      
    elif opcao == "2":
        print("Opção 2 - Matriz selecionada.")
        array = menu_internoArquivos()
        menu_internoMatriz(array)
    elif opcao == "3":
        print("Opção 3 - Ordenação selecionada.")
        array = menu_internoArquivos()
        menu_internoOrdenacao(array)   
    elif opcao == "4":
        print("Opção 4 - Pesquisa selecionada.")
        array = menu_internoArquivos()
        menu_internoPesquisa(array)
    elif opcao == "5":
        print("Opção 5 - Árvore selecionada.")
    elif opcao == "6":
        print("Opção 6 selecionada.")
    elif opcao == "7":
        print("Saindo...")
        return False
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    return True

def main():
    executar = True
    while executar:
        exibir_menu()
        opcao = escolher_opcao()
        executar = processar_opcao(opcao)

if __name__ == "__main__":
    main()

