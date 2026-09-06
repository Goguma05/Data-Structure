class Stack:
    def __init__(self, capacity = 100):
        self.data
        self.top = 0
        self.capacity = capacity

    def isEmpty(self):
        return (self.top == 0)

    def isFull(self):
        return (self.top >= self.capacity - 1)

    def push(self, value):
        if self.isFull():
            return
        self.data[self.top] = value
        self.top += 1

    def pop(self):
        if self.isEmpty():
            return
        data = self.data[self.top]
        self.top -= 1
        return data

    def peek(self):
        return self.data[self.top]

    def size(self):
        return self.top
    