import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        dic = collections.defaultdict(int)
        for c in s:
            dic[c] += 1
        counts = set()
        ans = 0
        for key in dic:
            while dic[key] > 0 and dic[key] in counts:
                dic[key] -= 1
                ans += 1
            counts.add(dic[key])
        return ans

print(Solution().minDeletions("aaabbbcc"))
