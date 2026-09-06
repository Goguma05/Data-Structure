class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def popleft(self):
        data = self.head.data
        self.head = self.head.next
        return data

    def search(self, value):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == value:
                return True
            curr_node = curr_node.next
        return False

    def delete(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.data == value:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next