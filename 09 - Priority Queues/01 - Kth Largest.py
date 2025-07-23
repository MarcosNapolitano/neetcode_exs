#!/usr/bin/python3
from heap_2 import min_heap


class KthLargest:

    def __init__(self, k: int, nums: list[int]):

        self.nums: list = nums
        self.limit: int = k
        self.heap: min_heap = min_heap()

        for i in nums:

            if not self.__remove_check(i):
                continue

            self.heap.add(i)

    def add(self, item: int or float) -> int or float:

        if self.__remove_check(item):
            self.heap.add(item)

        return self.heap.data[0]

    def __remove_check(self, item: int or float) -> bool:

        if self.limit == self.heap.length:
            if item > self.heap.data[0]:
                self.heap.delete()
                return True
            return False

        return True


q = KthLargest(7, [-10, 1, 3, 1, 4, 10, 3, 9, 4, 5, 1])
