import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        a,b = collections.defaultdict(int), collections.defaultdict(int)
        for c in s: a[c] += 1
        for c in t: b[c] += 1
        return a == b




        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # else:
        #     return False