from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ss, pp = defaultdict(int), defaultdict(int)
        if len(s) < len(p): return []
        for i in range(len(p)):
            pp[p[i]] += 1
            ss[s[i]] += 1
        ans = []
        if ss == pp: ans.append(0)
        for i in range(len(p), len(s)):
            start = i -len(p)
            ss[s[i]] += 1
            ss[s[start]] -= 1
            if ss[s[start]] == 0:
                ss.pop(s[start])
            if ss == pp: 
                ans.append(start+1)
        return ans

print(Solution().findAnagrams('cbaebabacd', 'abc'))