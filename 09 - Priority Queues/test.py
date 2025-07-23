#!/usr/bin/python3

from heapq import heapify, heappush


a: list = []

heapify(a)

heappush(a, (1, [3, 4]))
heappush(a, (0, [1, 2]))

print(a[0])
