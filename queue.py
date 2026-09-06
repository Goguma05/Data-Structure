class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def isEmpty(self):
        return self.head is None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def popleft(self):
        if self.isEmpty():
            return
        
        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        self._size -= 1
        return data

    def peek(self):
        if self.isEmpty():
            return None
        return self.head.data

    def size(self):
        return self._size