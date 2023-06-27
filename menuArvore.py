import time
import sys
sys.path.append('./Arvore')
import arvoreBinariaBusca
import arvoreAVL


def menu_internoArvore(array):
    while True:
        print("Opção 1 - Listas selecionada.")
        print("Escolha uma opção: ")
        print("1. Árvore Binária")
        print("2. Árvore AVL")
        print("3. Comparativo entre as duas árvores")
        print("4. Imprimir árvore Binária")
        print("4. Voltar ao menu inicial")
        selecaoArvore = input("Escolha uma opção: ")

        if selecaoArvore == '1':
            num = int(input("Digite qual número procura "))
            arvoreBinaria(array, num)
        elif selecaoArvore == '2':
            num = int(input("Digite qual número procura "))
            arvore_AVL(array, num)
        elif selecaoArvore == '3':
            num = int(input("Digite qual número procura "))
            arvoreBinaria(array, num)
            arvore_AVL(array, num)
        elif selecaoArvore == '4':
            arvoreBinariaImpressao(array)
        elif selecaoArvore == '5':
            print("Voltando ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True

def arvoreBinaria(array, num):
    inicio_sequencialBinaria = time.time()
    n = array[0]
    raiz = arvoreBinariaBusca.NodoArvore(n)
    print("1. Árvore Binária de Busca")
    for chave in array[1:]:
        nodo = arvoreBinariaBusca.NodoArvore(chave)
        arvoreBinariaBusca.insere(raiz, nodo)
    search = arvoreBinariaBusca.busca(raiz, num)
    if search.chave == num:
        print ("O número existe na árvore")
    else:
        print("O número não se encontra na árvore")
    fim_sequencialBinaria = time.time()
    tempo_sequencialBinaria = fim_sequencialBinaria - inicio_sequencialBinaria
    print(f"O tempo de execução foi de: {tempo_sequencialBinaria}")


def arvore_AVL(array, elementoBusca):
    inicio_sequencialAVL = time.time()
    print("2. Árvore AVL")
    raiz = None
    for i in array:
        raiz = arvoreAVL.inserir(raiz, arvoreAVL.NodoAVL(i))
    resultado = arvoreAVL.busca(raiz, elementoBusca)
    fim_sequencialAVL = time.time()
    tempo_sequencialAVL = fim_sequencialAVL - inicio_sequencialAVL
    if resultado is not None:
        print(f"Elemento {elementoBusca} foi encontrado na árvore.")
    else:
        print(f"Elemento {elementoBusca} não foi encontrado na árvore.")
    print(f"O tempo de execução foi de: {tempo_sequencialAVL}")


def arvoreBinariaImpressao(array):
    inicio_sequencialBinaria = time.time()
    n = array[0]
    raiz = arvoreBinariaBusca.NodoArvore(n)
    print("Árvore Binária de Busca - impressão")
    for chave in array[1:]:
        nodo = arvoreBinariaBusca.NodoArvore(chave)
        arvoreBinariaBusca.insere(raiz, nodo)
    arvoreBinariaBusca.em_ordem(raiz)
    print(" ")
    fim_sequencialBinaria = time.time()
    tempo_sequencialBinaria = fim_sequencialBinaria - inicio_sequencialBinaria
    print(f"O tempo de execução foi de: {tempo_sequencialBinaria}")