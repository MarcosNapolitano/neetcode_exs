#!/usr/bin/python3

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        results: list[list[int]] = []
        subres: list[int] = []
        index: dict = {}

        def recurive(i):

            if i >= len(nums):
                element = subres.copy()
                element.sort()
                print(subres)
                key = ''

                for i in element:
                    key += str(i) + ","

                if index.get(key):
                    return

                index[key] = 1
                results.append(element)
                return

            # include the number
            subres.append(nums[i])
            recurive(i + 1)

            # don't include the number
            subres.pop()
            recurive(i + 1)

        recurive(0)

        return results


obj = Solution()

print(obj.subsets([4, 1, 0]))
