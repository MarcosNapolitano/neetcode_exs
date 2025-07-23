#!/usr/bin/python3

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        results: list[list[int]] = []
        subres: list[int] = []

        def recurive(index):

            if index >= len(nums):
                results.append(subres.copy())
                return

            # include the number
            subres.append(nums[index])
            recurive(index + 1)

            # don't include the number
            subres.pop()
            recurive(index + 1)

        recurive(0)

        return results


obj = Solution()

print(obj.subsets([4, 1, 0]))
