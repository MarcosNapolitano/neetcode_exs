#!/usr/bin/python3

from heapq import heappop, heappush, heapify


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap: list = []
        heapify(heap)

        for i in stones:
            heappush(heap, -1 * i)

        heap.sort()
        while len(heap) > 1:
            heap[1] = heap[0] - heap[1]
            heappop(heap)
            if heap[0] == 0:
                heappop(heap)

            heap.sort()

        if len(heap) == 1:
            return heap[0] * -1

        return 0


obj = Solution()

print(obj.lastStoneWeight([4, 3, 4, 3, 2]))
