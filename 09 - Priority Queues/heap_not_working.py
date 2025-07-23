#!/usr/bin/python3

# children
# left = 2index + 1
# right = 2index + 2

# parent = (index - 1) // 2 -> as 5/2 = 2 not 2.5

class max_heap:
    def __init__(self):
        self.heap: list = []
        self.length: int = -1

    def add(self, item: int or float):

        self.length += 1
        self.heap.append(item)

        if self.length == 0:
            return self.heap

        index: int = self.length

        while self.heap[(index - 1)//2] < self.heap[index]:
            temp: int = self.heap[(index-1)//2]
            self.heap[(index-1)//2] = self.heap[index]
            self.heap[index] = temp

            index = (index-1)//2

            if index <= 0:
                break

        return self.heap

    def remove(self):
        # cambiar cabeza por el ultimo
        # borrarlo
        # heapify down el cambiado
        if self.length <= 0:
            self.heap = []
            self.length = -1
            return None

        self.heap[0] = self.heap.pop()
        self.length -= 1

        if self.length == 0:
            return None

        index: int = 0
        left: int = 2*index + 1
        right: int = 2*index + 2

        while left <= self.length >= right:

            ind_v: int = self.heap[index]
            left_v: int = self.heap[left]
            right_v: int = self.heap[right]

            if left_v >= right_v and ind_v <= left_v:

                self.heap[index] = left_v
                self.heap[left] = ind_v
                index = left

            elif left_v < right_v and ind_v <= right_v:

                self.heap[index] = right_v
                self.heap[right] = ind_v
                index = right

            left = 2*index + 1
            right = 2*index + 2

        if left == self.length:
            temp: int or float = self.heap[index]
            self.heap[index] = self.heap[left]
            self.heap[left] = temp


class min_heap:
    def __init__(self):
        self.heap: list = []
        self.length: int = -1

    def add(self, item: int or float):

        self.length += 1
        self.heap.append(item)

        if self.length == 0:
            return self.heap

        index: int = self.length

        while self.heap[(index - 1)//2] > self.heap[index]:
            temp: int = self.heap[(index-1)//2]
            self.heap[(index-1)//2] = self.heap[index]
            self.heap[index] = temp

            index = (index-1)//2

            if index <= 0:
                break

        return self.heap

    def remove(self):
        # cambiar cabeza por el ultimo
        # borrarlo
        # heapify down el cambiado
        if self.length <= 0:
            self.heap = []
            self.length = -1
            return None

        self.heap[0] = self.heap.pop()
        self.length -= 1

        if self.length == 0:
            return None

        index: int = 0
        left: int = 2*index + 1
        right: int = 2*index + 2

        while left <= self.length >= right:

            ind_v: int = self.heap[index]
            left_v: int = self.heap[left]
            right_v: int = self.heap[right]

            if left_v <= right_v and ind_v >= left_v:

                self.heap[index] = left_v
                self.heap[left] = ind_v
                index = left

            elif left_v > right_v and ind_v >= right_v:

                self.heap[index] = right_v
                self.heap[right] = ind_v
                index = right

            left = 2*index + 1
            right = 2*index + 2

        if left == self.length:
            temp: int or float = self.heap[index]
            self.heap[index] = self.heap[left]
            self.heap[left] = temp


queue = min_heap()
print(queue.add(5))
print(queue.add(5))
print(queue.add(8))
print(queue.remove())
print(queue.heap)
