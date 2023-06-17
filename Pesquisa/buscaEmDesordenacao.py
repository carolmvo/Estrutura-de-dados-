global NOT_FOUND
NOT_FOUND = -1

def find (alist, key):
    for i in range(0, len(alist)):
        if key == alist[i]:
            return i
    return NOT_FOUND

