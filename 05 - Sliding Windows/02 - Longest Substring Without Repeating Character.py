#!usr/bin/python

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        index = set()
        current_length = 0
        left = 0

        for right in range(len(s)):

            while s[right] in index:
                index.remove(s[left])
                left += 1

            index.add(s[right])
            if current_length < len(index):
                current_length = len(index)

        return current_length
