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

    def dfs_pre_order(self):
        result = []

        def traverse(node):
            result.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        if self.root:
            traverse(node=self.root)
        return result

    def dfs_post_order(self):
        """
        Look left and right of the current node, then write the value to results if no node exists
        """
        result = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            result.append(node.value)

        if self.root:
            traverse(node=self.root)
        return result

    def dfs_in_order(self):
        result = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            result.append(node.value)
            if node.right:
                traverse(node.right)

        if self.root:
            traverse(node=self.root)
        return result

    def is_valid_bst(self):
        values = self.dfs_in_order()
        for i in range(1, len(values)):
            if values[i] < values[i - 1]:
                return False
        return True

    def kth_smallest(self, k):
        if self.root is None or k < 1:
            return
        result = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            result.append(node.value)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        if len(result) < k:
            return
        return result[k - 1]

    def kth_smallest_1(self, k):
        stack = []
        node = self.root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1
            if k == 0:
                return node.value

            node = node.right

        return
