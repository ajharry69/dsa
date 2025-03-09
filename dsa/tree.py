from dsa.queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value=None):
        self.root = Node(value) if value else None

    def insert(self, value):
        node = Node(value=value)

        temp = self.root

        if temp is None:
            self.root = node
            return True

        while True:
            if temp.value == value:
                return False

            if temp.value > value:
                if temp.left is None:
                    temp.left = node
                    return True
                temp = temp.left
            elif temp.value < value:
                if temp.right is None:
                    temp.right = node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        if temp is None:
            return False

        while True:
            if value == temp.value:
                return True

            if value > temp.value:
                if temp.right is None:
                    return False
                temp = temp.right
            elif value < temp.value:
                if temp.left is None:
                    return False
                temp = temp.left

    def bfs(self):
        queue = Queue(self.root)
        result = []

        while queue.size > 0:
            node = queue.dequeue().value
            result.append(node.value)
            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

        return result
