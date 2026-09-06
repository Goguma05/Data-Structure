class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
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
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def appendleft(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self._size += 1

    def pop(self):
        if self.head is None:
            return

        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self._size -= 1
        return data

    def popleft(self):
        if self.head is None:
            return

        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self._size -= 1
        return data

    def extend(self, lst):
        for v in lst:
            self.append(v)

    def extendleft(self, lst):
        lst = lst[::-1]

        for v in lst:
            self.appendleft(v)

    def rotate(self, n):
        if self.head is None or self._size <= 1:
            return

        n = n % self._size

        if n > 0:
            for _ in range(n):
                target = self.tail
                self.tail = self.tail.prev
                self.tail.next = None

                target.prev = None
                target.next = self.head
                self.head.prev = target
                self.head = target
        elif n < 0:
            for _ in range(n*(-1)):
                target = self.head
                self.head = self.head.next
                self.head.prev = None

                target.next = None
                target.prev = self.tail
                self.tail.next = target
                self.tail = target

        
    def size(self):
        return self._size


