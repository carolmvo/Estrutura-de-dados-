from troca import swap

def bubbleSort (alist):
    N = len(alist)
    for passnum in range(1, N):
        for i in range(0,N-passnum):
            if alist[i] > alist[i+1]:
                swap(alist, i, i+1)
    return alist

# a= [2,5,9,22,1]

# res = bubbleSort(a)
# print(res)