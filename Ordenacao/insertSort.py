

def insertSort(alist):
    N = len(alist)
    for i in range(1,N):
        aux = alist[i]
        j = i-1
        while(j >= 0 and alist[j] >= aux):
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = aux
    return alist