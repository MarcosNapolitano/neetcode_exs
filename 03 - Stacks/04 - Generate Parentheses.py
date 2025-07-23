#!/usr/bin/python3

class Solution:
    def generateParenthesis(self, n):

        stack = []
        curr_str = []

        # open siempre tiene que ser mayor a closed
        # base case is closed==n

        def generate(p_open, p_close):

            if p_close == n:
                stack.append("".join(curr_str))
                return

            if p_open < n:
                curr_str.append("(")
                generate(p_open+1, p_close)
                curr_str.pop()

            if p_close < p_open:
                curr_str.append(")")
                generate(p_open, p_close+1)
                curr_str.pop()

        generate(0, 0)
        
        return stack

Sol = Solution()
print(Sol.generateParenthesis(3))
