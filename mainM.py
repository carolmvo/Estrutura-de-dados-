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
from menuArvore import *


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
        array = menu_internoArquivos()
        menu_internoArvore(array)
    elif opcao == "6":
        print("Opção 6 selecionada.")
        print("Selecione duas estruturas para comparar seus desempenhos")
        while True:
            array = menu_internoArquivos()
            print("Opção 1: Executar a árvore binária de pesquisa")
            print("Opção 2: Executar a árvore AVL")
            print("Opção 3: Executar a pesquisa binária ")
            print("Opção 4: Executar a pesquisa sequencial")
            print("Opção 5: Voltar ao menu inicial")
            selecaoMista1 = input("Escolha uma opção: ")
            selecaoMista2 = input("Escolha outra opção: ")
            num = int(input("Digite o número que deseja procurar "))
            if selecaoMista1 == '1' or selecaoMista2 == '1':
                print("Árvore Binária de Busca:")
                arvoreBinaria(array, num)
            if selecaoMista1 == '2' or selecaoMista2 == '2':
                print("Árvore AVL:")
                arvore_AVL(array, num)
            if selecaoMista1 == '3' or selecaoMista2 == '3':
                print("Pesquisa binária:")
                execucaoPesquisaBinaria(array, num)
            if selecaoMista1 == '4' or selecaoMista2 == '4':
                print("Pesquisa sequencial:")
                execucaoPesquisaSequencial(array, num)
            if selecaoMista1 == '5' or selecaoMista2 == '5':
                print("Voltando ao menu principal")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
            return True
        
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

