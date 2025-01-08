class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}->"


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

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

        self.length += 1
        return True

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1
        return True

    set_head = prepend

    def pop_first(self):
        if self.length == 0:
            return

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None

        self.length -= 1
        return temp

    def pop(self):
        if self.length < 2:
            return self.pop_first()

        temp = self.head
        while temp is not None:
            if temp.next == self.tail:
                t = self.tail
                temp.next = None
                self.tail = temp
                temp = t
                break

            temp = temp.next

        self.length -= 1

        return temp

    def remove(self, index):
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        before = self.get(index - 1)
        if before is None:
            return

        temp = before.next
        if temp is None:
            # the index may have been bigger than the length of the linkedlist
            return

        before.next = temp.next
        temp.next = None

        self.length -= 1
        return temp

    def set(self, index, value):
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        before = self.get(index - 1)

        if before is None:
            # applicable when index is out of range i.e.
            # below ZERO or above the length of the list
            return False

        node = Node(value)
        node.next = before.next
        before.next = node

        self.length += 1
        return True

    def get(self, index):
        if index < 0:  # or index >= self.length:
            # 2nd condition is not necessary, but an optimal step for avoiding unnecessary loop
            return

        temp = self.head
        for _ in range(index):
            if temp is None:
                return
            temp = temp.next

        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        # after = temp.next
        # while after is not None:
        #     temp.next = before
        #     before = temp
        #     temp = after
        #     after = temp.next

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next
