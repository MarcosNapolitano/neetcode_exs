#!usr/bin/python

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        max_profit = 0
        high = None
        low = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
                high = None
            else:
                if not high or high < prices[i]:
                    high = prices[i]
                    if high - low > max_profit:
                        max_profit = high - low

        return max_profit
