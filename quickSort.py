from troca import swap

def quickSort(alist):
    N = len(alist)
    recursiveQuickSort(alist, 0, N-1)

def recursiveQuickSort(alist, posMin, posMax):
    if(posMin<posMax):
        p = partition(alist, posMin, posMax)
        recursiveQuickSort(alist, posMin, p-1)
        recursiveQuickSort(alist, p+1, posMax)
    return alist
def partition(alist, posMin, posMax):
    pivot = alist[posMin]
    i = posMin+1
    j = posMax
    while True:
        while(i < posMax and alist[i] <= pivot):
            i += 1
        while(j > posMin and alist[j] >= pivot):
            j += 1
        if(i < j): swap(alist,i,j)
        if(i >= j): break
    swap(alist, posMin,j)
    return j