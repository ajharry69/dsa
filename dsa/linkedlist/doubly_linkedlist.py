class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"<-{self.value}->"


class LinkedList:
    def __init__(self, value=None):
        node = Node(value) if value else None
        self.head = node
        self.tail = node
        self.length = 1 if node else 0

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

        self.tail = temp.prev
        if self.tail is None:
            # linked-list only had one item, both head and tail should be reset to none
            self.head = None
        else:
            self.tail.next = None
            temp.prev = None

        self.length -= 1

        return temp

    def pop_first(self):
        # temp = self.head
        #
        # if temp is None:
        #     return
        #
        # self.head = temp.next
        #
        # if self.head is not None:
        #     self.head.prev = None
        # else:
        #     self.tail = None
        #
        # temp.next = None
        # self.length -= 1
        #
        # return temp
        return self.remove(0)

    def append(self, value):
        node = Node(value)

        if self.head is None:
            # empty linkedlist, set it up afresh
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
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
        #     temp.prev = self.head

        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.length += 1
        return True

    set_head = prepend

    def set_value(self, index, value):
        node = self.get(index)
        if node is None:
            return False

        node.value = value
        return True

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
        #         if temp.prev is None:
        #             self.head = node
        #         else:
        #             temp.prev.next = node
        #
        #         temp.prev = node
        #         self.length += 1
        #     return True
        #
        # return False
        if index < 0: return False

        if index == 0: return self.prepend(value)

        before = self.get(index - 1)
        if before is None: return False

        node = Node(value)
        node.prev = before
        node.next = before.next
        before.next = node

        if node.next is None: self.tail = node

        self.length += 1
        return True

    def get(self, index):
        # if index < 0 or index >= self.length:
        #     return None
        # temp = self.head
        # if index < self.length / 2:
        #     for _ in range(index):
        #         temp = temp.next
        # else:
        #     temp = self.tail
        #     for _ in range(self.length - 1, index, -1):
        #         temp = temp.prev
        # return temp
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
            self.tail = temp.prev
        else:
            temp.next.prev = temp.prev

        if temp.prev is None:
            # we are removing an item from the start (head) of the list
            self.head = temp.next
        else:
            temp.prev.next = temp.next

        temp.prev = None
        temp.next = None

        self.length -= 1

        return temp

    def reverse(self):
        # temp = self.head
        # self.head = self.tail
        # self.tail = temp
        #
        # before = None
        #
        # while temp is not None:
        #     after = temp.next
        #     temp.next = before
        #     temp.prev = after
        #     before = temp
        #     temp = after
        #
        # if self.head is not None:
        #     self.head.prev = None
        # if self.tail is not None:
        #     self.tail.next = None
        ##############
        # APPROACH 2 #
        ##############
        temp = self.head
        while temp is not None:
            # swap the prev and next pointers of node points to
            temp.prev, temp.next = temp.next, temp.prev

            # move to the next node
            temp = temp.prev # prev was changed to `temp.next` above

        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.head


    def swap_first_last(self):
        if self.head is None:
            return
        head_value = self.head.value
        self.head.value = self.tail.value
        self.tail.value = head_value

    def is_palindrome(self):
        start = self.head

        if start is None:
            return True

        end = self.tail
        while start is not None and start != end:
            if start.value != end.value:
                return False

            start = start.next
            end = end.prev

        return True

    def swap_pairs(self):
        first = second = self.head

        if second is None:
            return

        second = second.next

        if second is not None:
            self.head = second

        while second is not None:
            temp = first
            temp_prev = temp.prev

            first.prev = first.next
            first.next = second.next

            if second.next is not None:
                # will be used in subsequent pair swap
                second.next.prev = first

            second.next = second.prev
            second.prev = temp_prev

            if temp_prev:
                # update next reference of the most recent pair
                temp_prev.next = second

            first = first.next
            # none - will be encountered for odd number of nodes in the list
            second = None if first is None else first.next
