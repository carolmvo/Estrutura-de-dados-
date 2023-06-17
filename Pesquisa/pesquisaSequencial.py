from buscaEmDesordenacao import NOT_FOUND

def scanSequencial(alist, key):
    N = len(alist)
    for i in range(0,N):
        if key == alist[i]:
            return i
        elif key < alist[i]:
            return NOT_FOUND
    return NOT_FOUND
    

with open('./txt/arquivo ordenado grande.txt', 'r') as arquivo:
    conteudoOrdenadoGrande = arquivo.read()

valoresOrdenadoGrande = conteudoOrdenadoGrande.split(',')
listaNumericaOrdenadoGrande = [int(valor.strip()) for valor in valoresOrdenadoGrande]

print(scanSequencial(listaNumericaOrdenadoGrande, 66))