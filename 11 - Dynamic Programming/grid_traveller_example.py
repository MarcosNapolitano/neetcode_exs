#!/usr/bin/python3

def grid_traveller(m, n, memo={}):

    key = f"{m},{n}"

    if memo.get(key):
        return memo.get(key)

    if m == 0 or n == 0:
        return 0

    if m == n == 1:
        return 1

    memo[key] = grid_traveller(m - 1, n, memo) + grid_traveller(m, n-1, memo)

    return memo[key]


print(grid_traveller(18, 18))
