class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return f"<-{self.value}->"


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def __str__(self):
        out = ""
        temp = self.head
        while temp is not None:
            out += str(temp)
            temp = temp.next
        return out

    def pop(self):
        temp = self.tail

        if temp is None:
            # empty linked list
            return

        self.tail = temp.previous
        if self.tail is None:
            # linked-list only had one item, both head and tail should be reset to none
            self.head = None
        else:
            self.tail.next = None
            temp.previous = None

        self.length -= 1

        return temp

    def pop_first(self):
        temp = self.head
        if temp is None:
            return

        if temp.next is not None:
            # temp.next will be the new head and a head cannot have previous reference.
            temp.next.previous = None

        self.head = temp.next
        temp.next = None

        self.length -= 1

        if self.length == 0:
            # the list only had one item, which was set as the head and the tail.
            self.tail = None

        return temp

    def append(self, value):
        node = Node(value)

        if self.head is None:
            # empty linkedlist, set it up afresh
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

        self.length += 1
        return True

    def prepend(self, value):
        # temp = self.head
        #
        # node = Node(value)
        # self.head = node
        # self.head.next = temp
        #
        # if temp is None:
        #     self.tail = node
        # else:
        #     temp.previous = self.head

        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

        self.length += 1
        return True
