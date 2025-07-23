#!/usr/bin/python3

class min_heap:

    def __init__(self):

        self.length: int = 0
        self.data: list = []

    def add(self, item: int or float) -> None:
        self.data.append(item)
        self.__heapify_up(self.length)
        self.length += 1

        return None

    def delete(self) -> int or float:

        if self.length == 0:
            return -1

        deleted: int or float = self.data[0]
        self.length -= 1

        if self.length == 0:
            self.data = []
            return deleted

        self.data[0] = self.data.pop()

        if self.length == 1:
            return deleted

        self.__heapify_down(0)

        return deleted

    def __heapify_down(self, index: int) -> None:

        left_index = self.__left(index)
        right_index = self.__right(index)

        if left_index == self.length-1:
            if self.data[left_index] < self.data[index]:
                temp = self.data[left_index]
                self.data[left_index] = self.data[index]
                self.data[index] = temp
            return

        if left_index >= self.length:
            return

        left_value = self.data[left_index]
        right_value = self.data[right_index]
        index_value = self.data[index]

        if left_value >= right_value and index_value > right_value:
            self.data[right_index] = index_value
            self.data[index] = right_value
            self.__heapify_down(right_index)

        elif right_value >= left_value and index_value > left_value:
            self.data[left_index] = index_value
            self.data[index] = left_value
            self.__heapify_down(left_index)

    def __heapify_up(self, index: int) -> None:

        if index == 0:
            return

        index_value = self.data[index]
        parent_index = self.__parent(index)
        parent_value = self.data[parent_index]

        if index_value < parent_value:
            self.data[index] = self.data[parent_index]
            self.data[parent_index] = index_value
            self.__heapify_up(parent_index)

    def __parent(self, index: int) -> int:
        return (index - 1) // 2

    def __left(self, index: int) -> int:
        return 2 * index + 1

    def __right(self, index: int) -> int:
        return 2 * index + 2
