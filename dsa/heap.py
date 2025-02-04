class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)

        i = len(self.heap) - 1
        pi = self._parent(i)
        while pi >= 0 and self.heap[i] < self.heap[pi]:
            self._swap(i, pi)
            i = pi
            pi = self._parent(i)

    def remove(self):
        size = len(self.heap)
        if size == 0:
            return

        last = self.heap.pop()
        size -= 1
        if size == 0:
            return last

        temp = self.heap[0]
        self.heap[0] = last

        self._sink_down(size)

        return temp

    def _sink_down(self, size):
        i = 0
        while True:
            li = self._left_child(i)
            ri = self._right_child(i)
            if li < size and ri < size and self.heap[li] > self.heap[ri]:
                si = ri
            elif li < size:
                si = li
            else:
                break

            if self.heap[i] > self.heap[si]:
                self._swap(i, si)
                i = si
            else:
                break


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, n):
        self.heap.append(n)

        i = len(self.heap) - 1
        pi = self._parent(i)
        while pi >= 0 and self.heap[pi] < self.heap[i]:
            self._swap(i, pi)
            i = pi
            pi = self._parent(i)

    def remove(self):
        if len(self.heap) == 0:
            return

        last = self.heap.pop()
        size = len(self.heap)
        if size == 0:
            return last

        temp = self.heap[0]
        self.heap[0] = last

        self._sink_down(size)
        # self._sink_down_1(size)

        return temp

    def _sink_down(self, size):
        i = 0
        while True:
            left_index = self._left_child(i)
            right_index = self._right_child(i)
            if left_index < size and right_index < size and self.heap[left_index] < self.heap[right_index]:
                max_index = right_index
            elif left_index < size:
                max_index = left_index
            else:
                break

            if self.heap[i] < self.heap[max_index]:
                self._swap(i, max_index)
                i = max_index
            else:
                break

    def _sink_down_1(self, size):
        index = 0
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < size and
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < size and
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return


def find_kth_smallest(nums, k):
    heap = MaxHeap()
    for n in nums:
        heap.insert(n)
        if len(heap.heap) > k:
            heap.remove()

    return heap.remove()


# def stream_max(nums):
#     response = []
#     for i in range(1, len(nums) + 1):
#         heap = MaxHeap()
#         for n in nums[:i]:
#             heap.insert(n)
#         response.append(heap.remove())
#
#     return response

def stream_max(nums):
    max_heap = MaxHeap()
    max_stream = []

    for num in nums:
        max_heap.insert(num)
        max_stream.append(max_heap.heap[0])

    return max_stream