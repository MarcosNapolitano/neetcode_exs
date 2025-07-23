#!/usr/bin/python3

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):

        results = defaultdict(list)

        for i in strs:
            count = [0] * 26  # cause english

            for j in i:
                count[ord(j) - ord("a")] += 1

            results[tuple(count)].append(i)

        return results.values()


obj = Solution()

print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
