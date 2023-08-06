class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        ans = 0
        lo = 0
        most = 0
        for hi in range(len(s)):
            dic[s[hi]] = 1 + dic.get(s[hi], 0) #leading pointer increases dic frq count
            most = max(most, dic[s[hi]]) #either the leading pointer encountered a new most frequent letter or there was a previous max frequency letter
            if hi - lo + 1 - most > k: #determine if the window can be fixed with k swaps
                dic[s[lo]] -= 1 
                lo += 1 #contracts the window by one, so that the most variable doesn't go out of sync
            ans = max(ans, hi - lo + 1)
        return ans

sol = Solution()
print(sol.characterReplacement("AABABBA", 1))
