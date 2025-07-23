#!/usr/bin/python3

from heap_2 import min_heap


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        heap: object = min_heap()

        for i in nums:
            if k == heap.length:
                if i > heap.data[0]:
                    heap.delete()
                else:
                    continue
            heap.add(i)

        return heap.data[0]


q = Solution()
print(q.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
