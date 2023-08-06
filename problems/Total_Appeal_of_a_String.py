import collections


class Solution:
    def appealSum(self, s: str) -> int:
        res, cur, prev = 0, 0, collections.defaultdict(lambda: -1)
        for i, ch in enumerate(s):
            cur += i - prev[ch]
            prev[ch] = i
            res += cur
        return res  

print(Solution().appealSum('abc'))