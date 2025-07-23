#!/usr/bin/python3

from heapq import heapify, heapreplace, heappush, heappop


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        heap: list[int] = []
        results: list[list[int]] = []

        heapify(heap)
        # if x1 * x1 + y1 * y1 < al head entonces pushear

        for i in points:

            result: int = i[0] ** 2 + i[1] ** 2
            if len(heap) == k:
                if result < heap[0][0] * -1:
                    heapreplace(heap, (result * -1, i))

                continue

            heappush(heap, (result * -1, i))

        while heap:
            current: list[int] = heappop(heap)[1]
            results.append(current)

        return results


obj = Solution()
print(obj.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
