from buscaEmDesordenacao import NOT_FOUND

def scan (alist, key):
    for i in range(0,len(alist)):
        print(i)
        if key == alist[i]:
            return i
        if alist[i]>key:
            return NOT_FOUND
    return NOT_FOUND