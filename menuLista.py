import time
from tratamentoDados import *
from fila import Queue
from filaDuasExtremidades import Deque
from pilha import Stack
stack = Stack

def menu_internoLista(array):
    while True:
        print("Opção 1 - Listas selecionada.")
        print("Escolha uma opção: ")
        print("1. Pilha")
        print("2. Fila de uma extremidade")
        print("3. Fila de duas extremidades")
        print("4. Voltar ao menu inicial")
        selecaoLista = input("Escolha uma opção: ")
        if selecaoLista == '1':
            menu_internoPilha(array)
        elif selecaoLista == '2':
            menu_internoFila(array)
        elif selecaoLista == '3':
            menu_internoFilaDuasExt(array)
        elif selecaoLista == '4':
            print("Voltando ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True


def menu_internoPilha(array):
    while True:
        vetor = array
        j = 0
        print("Escolha uma opção: ")
        print("1. Adicionar a pilha")
        print("2. Excluir da pilha")
        print("3. Voltar ao menu anterior")
        selecaoPilha = input("Escolha uma opção: ")
        if selecaoPilha == '1':
            print("Você escolheu adicionar a pilha")
            num = int(input("Digite o número que quer incrementar a pilha "))
            inicio_sequencial = time.time()
            vetor = stack.push(num)
            fim_sequencial = time.time()
            tempo_sequencial = fim_sequencial - inicio_sequencial
            print (vetor)
            print(f"O tempo de execução foi de {tempo_sequencial}")
        elif selecaoPilha == '2':
            print("Você escolheu remover da pilha")
            inicio_sequencial = time.time()
            for j in len(array):
                vetor = Stack.pop(array[j])
            fim_sequencial = time.time()
            tempo_sequencial = fim_sequencial - inicio_sequencial
            print (vetor)
            print(f"O tempo de execução foi de {tempo_sequencial}")
        elif selecaoPilha == '3':
            print("Voltando ao menu Listas")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True

def menu_internoFila(array):
    while True:
        vetor = []
        print("Escolha uma opção: ")
        print("1. Adicionar a fila")
        print("2. Excluir da fila")
        print("3. Voltar ao menu anterior")
        selecaoPilha = input("Escolha uma opção: ")
        if selecaoPilha == '1':
            print("Você escolheu adicionar a fila")
            inicio_sequencial = time.time()
            for j in len(array):
                vetor = Queue.enqueue()
                j+=1
            fim_sequencial = time.time()
            tempo_sequencial = fim_sequencial - inicio_sequencial
            print (vetor)
            print(f"O tempo de execução foi de {tempo_sequencial}")
        elif selecaoPilha == '2':
            print("Você escolheu remover da fila")
            inicio_sequencial = time.time()
            for j in len(array):
                vetor = Queue.dequeue(j)
                j+=1
            fim_sequencial = time.time()
            tempo_sequencial = fim_sequencial - inicio_sequencial
            print (vetor)
            print(f"O tempo de execução foi de {tempo_sequencial}")
        elif selecaoPilha == '3':
            print("Voltando ao menu Listas")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True

def menu_internoFilaDuasExt(array):
     while True:
        vetor = []
        print("Escolha uma opção: ")
        print("1. Adicionar a fila pela frente")
        print("2. Adicionar a fila por trás")
        print("3. Excluir da fila pela frente")
        print("4. Excluir da fila por trás")
        print("5. Voltar ao menu anterior")
        selecaoPilha = input("Escolha uma opção: ")
        if selecaoPilha == '1':
            print("Você escolheu adicionar a fila pela frente")
            inicio_sequencial = time.time()
            for j in len(array):
                vetor = Deque.addFront
                j+=1
            fim_sequencial = time.time()
            tempo_sequencial = fim_sequencial - inicio_sequencial
            print (vetor)
            print(f"O tempo de execução foi de {tempo_sequencial}")
        elif selecaoPilha == '2':
            print("Você escolheu adicionar a fila por trás")
            inicio_sequencial = time.time()
            for j in len(array):
                vetor = Deque.addRear
                j+=1
            fim_sequencial = time.time()
            tempo_sequencial = fim_sequencial - inicio_sequencial
            print (vetor)
            print(f"O tempo de execução foi de {tempo_sequencial}")
        elif selecaoPilha == '3':
            print("Você escolheu remover da pilha pela frente")
            inicio_sequencial = time.time()
            for j in len(array):
                vetor = Deque.removeFront()
                j+=1
            fim_sequencial = time.time()
            tempo_sequencial = fim_sequencial - inicio_sequencial
            print (vetor)
            print(f"O tempo de execução foi de {tempo_sequencial}")
        elif selecaoPilha == '4':
            print("Você escolheu remover da pilha por trás")
            inicio_sequencial = time.time()
            for j in len(array):
                vetor = Deque.removeRear()
                j+=1
            fim_sequencial = time.time()
            tempo_sequencial = fim_sequencial - inicio_sequencial
            print (vetor)
            print(f"O tempo de execução foi de {tempo_sequencial}")
        elif selecaoPilha == '5':
            print("Voltando ao menu Listas")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        return True