#!/usr/bin/python3

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        # el truco esta en ordenarlo y elegir entre repetir el numero
        # o skipearlo completamente, es decir si hay un numero repetido
        # se utiliza y varias veces o no se utiliza jamas
        # al ordernar el array esto se logra sin usar un hashmap
        candidates.sort()

        subres: list[int] = []
        res: list[int] = []

        def recurive(index, subtotal):
            if subtotal == target:

                res.append(subres.copy())
                return

            # keep the boundaries and keep ourselves below target
            if index >= len(candidates) or subtotal > target:
                return

            subres.append(candidates[index])
            recurive(index + 1, subtotal + candidates[index])

            while index < len(candidates) - 1:
                if candidates[index] != candidates[index + 1]:
                    break
                index += 1

            subres.pop()
            recurive(index + 1, subtotal)

        recurive(0, 0)

        return res


obj = Solution()

print(obj.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
