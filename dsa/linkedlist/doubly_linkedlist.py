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
        return self.remove(0)

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

    set_head = prepend

    def set(self, index, value):
        # temp = self.head
        # i = -1
        # while i + 1 <= index:
        #     i += 1
        #     if i != index:
        #         if temp is None:
        #             # unknown index...
        #             break
        #         temp = temp.next
        #         continue
        #
        #     node = Node(value)
        #     node.next = temp
        #
        #     if temp is None:
        #         self.append(value)
        #     else:
        #         if temp.previous is None:
        #             self.head = node
        #         else:
        #             temp.previous.next = node
        #
        #         temp.previous = node
        #         self.length += 1
        #     return True
        #
        # return False
        if index < 0: return False

        if index == 0: return self.prepend(value)

        before = self.get(index - 1)
        if before is None: return False

        node = Node(value)
        node.previous = before
        node.next = before.next
        before.next = node

        if node.next is None: self.tail = node

        self.length += 1
        return True

    def get(self, index):
        c = 0
        temp = self.head
        while temp is not None:
            if c == index:
                return temp
            if c > index:
                break
            temp = temp.next
            c += 1

    def remove(self, index):
        temp = self.get(index)

        if temp is None:
            return

        if temp.next is None:
            # we are removing an item from the end (tail) of the list
            self.tail = temp.previous
        else:
            temp.next.previous = temp.previous

        if temp.previous is None:
            # we are removing an item from the start (head) of the list
            self.head = temp.next
        else:
            temp.previous.next = temp.next

        temp.previous = None
        temp.next = None

        self.length -= 1

        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None

        while temp is not None:
            after = temp.next
            temp.next = before
            temp.previous = after
            before = temp
            temp = after

        if self.head is not None:
            self.head.previous = None
        if self.tail is not None:
            self.tail.next = None
