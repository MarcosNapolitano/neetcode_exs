#!/usr/bin/python3

# son copiadas, no termino de entender como funcionan

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        res = []

        def backtrack(i):
            if i >= len(nums):
                res.append(nums[:])

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return res

    def permute2(self, nums: list[int]) -> list[list[int]]:

        result = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute2(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result


obj = Solution()

print(obj.permute2([1, 2, 3]))
