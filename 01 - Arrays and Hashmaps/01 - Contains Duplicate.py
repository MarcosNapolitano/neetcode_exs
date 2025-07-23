#!usr/bin/python

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        index = {}

        for i in nums:
            try:
                index[i]
                return True
            except IndexError:
                index[i] = 1

        return False
