import time

def ler_arquivo(nome_arquivo):
    matriz = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            valores = linha.strip().split(',')
            linha_convertida = [int(valor) for valor in valores]
            matriz.append(linha_convertida)
    return matriz

def somaDiagPrinc (matriz):
    inicio_sequencial = time.time()
    diagonalP = 0
    for i in range(len(matriz)):
        diagonalP += matriz[i][i]
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    print(f'O somatório da diagonal principal é {diagonalP} e seu cálculo demorou {tempo_sequencial}')

def numDiagPrinc (matriz):
    inicio_sequencial = time.time()
    diagonalPLista = []
    for i in range(len(matriz)):
        diagonalPLista.append(matriz[i][i])
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    print(f'Os números na diagonal principal são {diagonalPLista} e seu cálculo demorou {tempo_sequencial}')

def somaDiagSec (matriz):
    inicio_sequencial = time.time()
    diagonalS = 0
    for i in range(len(matriz)):
        diagonalS += matriz[i][len(matriz)-1-i]
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    print(f'O somatório da diagonal principal é {diagonalS} e seu cálculo demorou {tempo_sequencial}')

def numDiagSec (matriz):
    inicio_sequencial = time.time()
    diagonalSLista = []
    for i in range(len(matriz)):
        diagonalSLista.append(matriz[i][len(matriz)-1-i])
    fim_sequencial = time.time()
    tempo_sequencial = fim_sequencial - inicio_sequencial
    print(f'Os números na diagonal principal são {diagonalSLista} e seu cálculo demorou {tempo_sequencial}')

def menu_internoMatriz(array):
    while True:
        print("Você deseja: ")
        print("Opção 1: Somar a diagonal principal")
        print("Opção 2: Imprimir a diagonal principal")
        print("Opção 3: Somar a diagonal secundária")
        print("Opção 4: Imprimir a diagonal secundária")
        print("Opção 5: Voltar ao menu inicial")
        selecaoMatriz = input("Escolha uma opção: ")
        matriz = ler_arquivo(array)

        if selecaoMatriz == '1':
            print("1 - Somar a diagonal principal")
            somaDiagPrinc(matriz)
        elif selecaoMatriz == '2':
            print("2 - Números na diagonal principal")
            numDiagPrinc(matriz)
        elif selecaoMatriz == '3':
            print("3 - Somar a diagonal secundária")
            somaDiagSec(matriz)
        elif selecaoMatriz == '4':
            print("4 - Números a diagonal secundária")
            numDiagSec(matriz)
        elif selecaoMatriz == '5':
            print("Voltando ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True