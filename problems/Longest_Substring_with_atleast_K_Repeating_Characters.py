class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        hi,lo = 0,0
        dic = {}
        ans = 0
        while hi < len(s):
            fval, bval = s[hi],s[lo]
            dic[fval] = dic.get(fval,0) + 1