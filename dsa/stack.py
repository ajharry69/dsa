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

    def peek(self):
        return self.top

    def is_empty(self):
        return self.size == 0


def is_balanced_parentheses(data):
    stack = Stack()
    for c in reversed(data):
        if c == '(':
            if stack.peek() is None or stack.peek().value != ')':
                # account for ""
                return False
            else:
                # account for "()"
                stack.pop()
        elif c == ')':
            stack.push(c)

    return stack.is_empty()
