class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"<-{self.value}"


class Queue:
    def __init__(self, value=None):
        self.front = Node(value=value) if value else None
        self.back = self.front
        self.size = 1 if self.front else 0

    def __str__(self):
        temp = self.front
        out = ""

        while temp:
            out += str(temp)
            temp = temp.next

        return out

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node
        self.size += 1
        return True

    def dequeue(self):
        temp = self.front
        if temp is None:
            return

        self.front = temp.next
        temp.next = None

        if self.front is None:
            # queue was size 1
            self.back = None
        elif self.front.next is None:
            # queue was size 2
            self.back = self.front

        self.size -= 1
        return temp
