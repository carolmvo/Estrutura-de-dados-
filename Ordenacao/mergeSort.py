

def merge(alist, mid):
    ladoEsq = alist[:mid]
    ladoDir = alist[mid:]
    i = j = k = 0
    while i < len(ladoEsq) and j < len(ladoDir):
        if ladoEsq[i] <= ladoDir[j]:
            alist[k] = ladoEsq[i]
            i += 1
        else:
            alist[k] = ladoDir[j]
            j += 1
        k += 1
    while i < len(ladoEsq):
        alist[k] = ladoEsq[i]
        i += 1
        k += 1
    while j < len(ladoDir):
        alist[k] = ladoDir[j]
        j += 1
        k += 1
    return alist

def mergeSort(alist):
    N = len(alist)
    if len(alist) > 1:
        mid = N//2
        ladoEsq = alist[:mid]
        ladoDir = alist[mid:]
        ladoEsq = mergeSort(ladoEsq)
        ladoDir = mergeSort(ladoDir)
        alist = merge(ladoEsq + ladoDir, mid)
    return alist