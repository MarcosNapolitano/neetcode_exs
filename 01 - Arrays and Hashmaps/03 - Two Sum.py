#!usr/bin/python

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = {}
        length = len(nums)

        for i in range(length):
            index[nums[i]] = i

        for i in range(length):
            value = target - nums[i]
            try:
                if index[value] == i:
                    continue

                return [i, index[value]]

            except TypeError:
                continue
