class NodoArvore:
    def __init__(self, chave=None, esquerda = None, direita = None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
    
    def __repr__(self):
        return'%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)
    
def em_ordem(raiz):
    if not raiz:
        return
    em_ordem(raiz.esquerda)
    print(raiz.chave)
    em_ordem(raiz.direita)

def insere(raiz, nodo):
    if raiz is None:
        raiz = nodo
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else: 
            insere(raiz.direita, nodo)
    else:
        if raiz.esquerda is None:
            raiz.esqueda = nodo
        else:
            insere(raiz.esquerda, nodo)


def busca(raiz, chave):
    if raiz is None:
        return None
    if raiz.chave == chave:
        return raiz
    if raiz.chave < chave:
        return busca(raiz.direita, chave)
    return busca(raiz.esquerda, chave)


'''Copiar para implementação de busca'''
arr = [22, 63, 54, 71, 19, 37]
raiz = NodoArvore(40)
for chave in arr:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)

elementoBusca = [-50, 54, 71, 19, 100]
for chave in elementoBusca:
    resultado = busca(raiz, chave)
    if resultado:
        print("Busca pela chave {}: Sucesso!".format(chave))
    else:
        print("Busca pela chave {}: Falha!".format(chave))
