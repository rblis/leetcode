from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo, hi = 0, 0
        dic = {}
        ans = 0
        while hi < len(s):
            val = s[hi]
            if val not in dic:
                dic[val] = hi                
            else:
                target = dic[val]
                while lo <= target:
                    dic.pop(s[lo])
                    lo += 1
                dic[val] = hi
            hi += 1
            ans = max(ans, hi-lo)
        return ans

sol = Solution()
print(sol.lengthOfLongestSubstring("abba"))