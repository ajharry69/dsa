class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}\n"


class Stack:
    def __init__(self, value=None):
        self.top = Node(value=value) if value else None
        self.size = 1 if self.top else 0

    def __str__(self):
        temp = self.top
        out = ""

        while temp:
            out += str(temp)
            temp = temp.next

        return out

    def push(self, value):
        node = Node(value=value)
        node.next = self.top
        self.top = node

        self.size += 1

        return True

    def pop(self):
        temp = self.top
        if temp is None:
            return

        self.top = temp.next
        temp.next = None
        self.size -= 1

        return temp
