from deque import Deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        new_node = Node(value)

        queue = Deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()

            if not current.left:
                current.left = new_node
                break
            else:
                queue.append(current.left)

            if not current.right:
                current.right = new_node
                break
            else:
                queue.append(current.right)

    def delete(self, value):
        queue = Deque()
        queue.append(self.root)

        target_node = None
        last_node = None
        parent_of_last = None

        while queue:
            current = queue.popleft()

            if current.value == value:
                target_node = current

            if current.left:
                parent_of_last = current
                last_node = current.left
                queue.append(current.left)

            if current.right:
                parent_of_last = current
                last_node = current.right
                queue.append(current.right)

        if target_node:
            target_node.value = last_node.value

            if parent_of_last.left == last_node:
                parent_of_last.left = None
            else:
                parent_of_last.right = None


    def preOrder(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)
    
    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print(node.value, end=" ")
            self.inOrder(node.right)

    def postOrder(self, node):
        if node is not None:
            self.preOrder(node.left)
            self.preOrder(node.right)
            print(node.value, end=" ")

    def levelOrder(self, node):
        if not node:
            return

        queue = Deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            print(current.value, end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.appnd(current.right)
    


        