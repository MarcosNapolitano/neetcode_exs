#!usr/bin/python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        index = {}

        for i in s:
            try:
                index[i] += 1
            except TypeError:
                index[i] = 1

        for i in t:
            try:
                if index[i] == 0:
                    return False

                index[i] -= 1
            except TypeError:
                return False

        return True
