class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}->"


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
        temp = self.head

        if not temp:
            # empty list
            return

        self.head = temp.next
        temp.next = None

        if self.head is None:
            # list contained only one item
            self.tail = self.head

        self.length -= 1

        return temp

    def pop(self):
        temp = self.head

        count = 1
        while temp is not None:
            if count == 1 and temp.next is None:
                # list contained one item
                self.tail = None
                self.head = None
            elif temp.next is not None and temp.next.next is None:
                self.tail = temp
                temp = temp.next
                self.tail.next = None
            else:
                count += 1
                temp = temp.next
                continue
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

    # def set_value(self, index, value):
    #     if index < 0:
    #         return False
    #
    #     before = self.get(index - 1)
    #
    #     if before is None:
    #         return False
    #
    #     node = Node(value)
    #
    #     temp = before.next
    #     if temp is not None:
    #         node.next = temp.next
    #         temp.next = None
    #
    #     before.next = node
    #
    #     self.length += 1
    #
    #     return True

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
        if index < 0 or index > self.length - 1:
            # 2nd condition is not necessary, but an optimal step for avoiding unnecessary loop
            return

        temp = self.head

        i = 0
        while temp is not None:
            if i == index:
                return temp

            temp = temp.next
            i += 1

    def reverse(self):
        # temp = self.head
        # self.head = self.tail
        # self.tail = temp
        # before = None
        #
        # # for _ in range(self.length):
        # #     after = temp.next
        # #     temp.next = before
        # #     before = temp
        # #     temp = after
        #
        # while temp is not None:
        #     after = temp.next
        #     temp.next = before
        #     before = temp
        #     temp = after
        #
        # if self.tail is not None:
        #     self.tail.next = None

        temp = self.head
        self.tail = temp
        before = None

        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        self.head = before

    def reverse_between(self, start_index, end_index):
        temp = self.head

        if not temp or not temp.next:
            # If the linked list is empty or has only one node,
            # return None.
            return

        i = 0
        start = before = before_start = None

        while temp and i <= end_index:
            if i + 1 == start_index:
                # we'll use to update next reference to point to the
                # last reversed item
                before_start = temp

            if i == start_index:
                # we'll update the next reference for this node
                # (start.next) when we reach the end of the
                # requested reverse position.
                # For example, given 1,2,3,4,5 and we are asked to
                # reverse btwn 1 and 3, start will be 2. When we
                # reverse upto 4th item (4), we'll update start.next
                # to point to 5 (5th item) instead of 1, which is
                # used by default in the reversal process
                start = temp

            after = temp.next
            if i >= start_index:
                # it is at this point that actual reversal takes
                # place.
                # we only want to start reversing when we reach
                # our start index.
                temp.next = before
            before = temp

            if i == end_index:
                start.next = after
                if before_start is None:
                    # reversing from index 0 - 1st position.
                    self.head = temp
                else:
                    # reversing from position 2 onwards
                    before_start.next = temp
            temp = after
            i += 1

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next if fast.next else None

        return slow

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next

    def has_loop(self):
        """
        Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm) to detect the loop.
        """
        slow = fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def find_kth_from_end(self, k):
        slow = fast = self.head

        # while True:
        #     for _ in range(k):
        #         if fast is None:
        #             return
        #         fast = fast.next
        #     if slow is not None:
        #         slow = slow.next
        #     if fast is None:
        #         return slow

        for _ in range(k):
            if fast is None:
                return
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow

    def partition_list(self, x):
        """
        if not self.head:
            return None

        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head

        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next

        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next

        self.head = dummy1.next
        """
        # "j" will always be right behind "k"
        i = j = self.head

        if j is None:
            return

        k = j.next

        while k is not None:
            # if i.value < x and k.value >= x:
            if i.value < x <= k.value:
                # 3, 8, 5
                # x = 5
                # i = 3; j = 3; k = 8
                i = i.next
                j = k
                k = j.next
            elif i.value >= x and k.value >= x:
                # 3, 8, 5, 10, 2, 1
                # x = 5
                # i = 8; j = 8; k = 5
                # OR
                # i = 8; j = 5; k = 10
                j = k
                k = j.next
            elif i == j:
                # 3, 1, 4
                # x = 3
                # i = 3; j = 3; k = 1
                # swap values of i and k
                n = i.value
                i.value = k.value
                k.value = n

                # increment the positions of "i", "j" and "k"
                i = j = k
                k = k.next
            else:
                # 3, 8, 5, 10, 2, 1
                # x = 5
                # i = 8; j = 10; k = 2

                # prepare to push "i" forward (to leave space for k)
                n = Node(value=i.value)
                n.next = i.next
                # replace value of "i" with that of "k" as new "i" (to avoid creating new node)
                i.value = k.value
                # push (old) "i" forward (ahead of (new) "i")
                i.next = n
                # prepare to remove "k" from the list
                j.next = k.next

                # increment the position of "i"
                i = i.next
                # "k" is still pointing to the "k"-node that we are removing in the next line
                # no need to reposition "j" since we removed "k" that was just swapped
                k = k.next

    def remove_duplicates(self):
        duplicates = set()

        before = None
        current = self.head

        while current is not None:
            if current.value in duplicates:
                before.next = current.next
            else:
                duplicates.add(current.value)
                before = current
            current = current.next

    def binary_to_decimal(self):
        result = 0
        temp = self.head

        i = 0
        while temp is not None:
            i += 1
            result += pow(2, self.length - i) * temp.value
            temp = temp.next
        return result

    def bubble_sort(self):
        n = self.length
        while n > 1:
            j = 1
            node = self.head
            while j < n:
                next_node = node.next
                if node.value > next_node.value:
                    v = node.value
                    node.value = next_node.value
                    next_node.value = v
                node = next_node
                j += 1
            n -= 1

    def selection_sort(self):
        node = self.head

        while node and node.next:
            min_node = node

            next_node = node.next

            while next_node:
                if next_node.value < min_node.value:
                    min_node = next_node
                next_node = next_node.next

            node.value, min_node.value = min_node.value, node.value

            node = node.next

    def insertion_sort(self):
        """
        i = 1
        n = len(my_list)
        while i < n:
            j = i
            while j > 0 and my_list[j] < my_list[j - 1]:
                my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
                j -= 1
            i += 1
        ---------------------------------------------------------------------
        start = self.head
        if not start:
            return
        next_node = start.next
        i = 1
        n = self.length
        while i < n:
            previous = start
            node = next_node
            j = i
            while j > 0 and node.value < previous.value:
                node.value, previous.value = previous.value, node.value
                j -= 1
            i += 1
        """
        if self.length < 2:
            return

        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None

        while unsorted_list_head is not None:
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next

            if current.value < sorted_list_head.value:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current

        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp
