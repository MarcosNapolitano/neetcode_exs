#!/usr/bin/python3

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        results: list[list[int]] = []
        subres: list[int] = []

        def recurive(index, subtotal):
            if subtotal == target:
                results.append(subres.copy())
                return

            if index >= len(candidates) or subtotal > target:
                return

            # repeat the number
            subres.append(candidates[index])
            recurive(index, subtotal + candidates[index])

            # dont repeat the number
            subres.pop()
            recurive(index + 1, subtotal)

        recurive(0, 0)

        return results


obj = Solution()

print(obj.combinationSum([2, 3, 6, 7], 7))
