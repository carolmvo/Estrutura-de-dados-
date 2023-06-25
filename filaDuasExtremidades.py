class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.size() == []

    def addFront(self, item):
        self.items.insert(0,item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def rear(self):
        return self.items[self.size()-1]

    def front(self):
        return self.items[0]