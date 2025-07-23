class Solution:
    def isValid(self, string):
        if len(string) < 2:
            return False

        stack = []

        for i in string:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
                continue

            if len(stack) == 0:
                return False
            if i == ")":
                if stack.pop() == "(":
                    continue
                else:
                    return False
            if i == "]":
                if stack.pop() == "[":
                    continue
                else:
                    return False
            if i == "}":
                if stack.pop() == "{":
                    continue
                else:
                    return False

        if len(stack) > 0:
            return False
        else:
            return True
