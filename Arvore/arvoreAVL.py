class NodoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 0

    def __repr__(self):
        return'%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)
    

def altura_nodo(nodo):
    if not nodo:
        return 0
    return nodo.altura

def fator_balanceamento(nodo):
    if not nodo:
        return 0
    return altura_nodo(nodo.esquerda) - altura_nodo(nodo.direita)

def rotacao_esquerda(nodo):
    nova_raiz = nodo.direita
    nodo.direita = nova_raiz.esquerda
    nova_raiz.esquerda = nodo
    nodo.altura = max(altura_nodo(nodo.esquerda), altura_nodo(nodo.direita))+1
    nova_raiz.altura = max(altura_nodo(nova_raiz.direita), nodo.altura)+1
    return nova_raiz

def rotacao_direita(nodo):
    nova_raiz = nodo.esquerda
    nodo.direita = nova_raiz.esquerda
    nova_raiz.esquerda = nodo
    nodo.altura = max(altura_nodo(nodo.esquerda), altura_nodo(nodo.direita))+1
    nova_raiz.altura = max(altura_nodo(nova_raiz.esquerda), nodo.altura)+1
    return nova_raiz

def inserir(raiz, nodo):
    if raiz is None:
        return nodo
    if raiz.chave < nodo.chave:
        raiz.direita = inserir(raiz.direita, nodo)
    else:
        raiz.esquerda = inserir(raiz.esquerda, nodo)
    raiz.altura = max(altura_nodo(raiz.esquerda), altura_nodo(raiz.direita))+1
    balanceamento = fator_balanceamento(raiz)
    if balanceamento > 1:
        if nodo.chave < raiz.esquerda.chave:
            return rotacao_direita(raiz)
        else:
            raiz.esquerda = rotacao_esquerda(raiz.esquerda)
            return rotacao_direita(raiz)
    if balanceamento < -1:
        if nodo.chave > raiz.direita.chave:
            return rotacao_esquerda(raiz)
        else:
            raiz.direita = rotacao_direita(raiz.direita)
            return rotacao_esquerda(raiz)
    return raiz

def busca(raiz, chave):
    if raiz is None:
        return None
    if raiz.chave == chave:
        return raiz
    if raiz.chave < chave:
        return busca(raiz.direita, chave)
    return busca(raiz.esquerda, chave)


def em_ordem(raiz):
    if not raiz:
        return
    em_ordem(raiz.esquerda)
    print(raiz.chave)
    em_ordem(raiz.direita)


# print("__________________________")
# elementoBusca = [-50, 54, 71, 19, 100]
# arr = [22, 63, 54, 71, 19, 37]

# raiz = None
# for i in arr:
#     raiz = inserir(raiz, NodoAVL(i))

# print(em_ordem(raiz))

# print(em_ordem(raiz))
# for i in elementoBusca:
#     resultado = busca(raiz, i)
#     if resultado is not None:
#         print(f"Elemento {i} encontrado na árvore.")
#     else:
#         print(f"Elemento {i} não encontrado na árvore.")

