from troca import swap

def selectSort(alist):
    N = len(alist)
    for i in range(0,N-1):
        positionOfMin = i
        for j in range(i+1,N):
            if alist[j]<alist[positionOfMin]:
                positionOfMin = j
        swap(alist,i,positionOfMin)
    return alist
