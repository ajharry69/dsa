class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}\n"


class Stack:
    def __init__(self, value=None):
        self.top, self.size = (Node(value=value), 1) if value else (None, 0)

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
        if c == "(":
            if stack.peek() is None or stack.peek().value != ")":
                # account for ""
                return False
            else:
                # account for "()"
                stack.pop()
        elif c == ")":
            stack.push(c)

    return stack.is_empty()


def reverse_string(string):
    stack = Stack()

    for c in string:
        stack.push(c)

    out = ""

    while not stack.is_empty():
        out += stack.pop().value

    return out


def sort_stack(stack):
    new_stack = Stack()  # will serve as a staging/holding area.

    # copy values to a new stack so that we are able
    # to modify the original stack in-place
    while not stack.is_empty():
        new_stack.push(value=stack.pop().value)

    while not new_stack.is_empty():
        if stack.is_empty() or new_stack.peek().value <= stack.peek().value:
            # since we are sorting in ascending order, we want to push the
            # smallest or equal element at the top of the sorted stack
            value = new_stack.pop().value
            stack.push(value=value)
        else:
            value = new_stack.pop().value

            while not stack.is_empty() and value > stack.peek().value:
                new_stack.push(value=stack.pop().value)

            stack.push(value=value)
