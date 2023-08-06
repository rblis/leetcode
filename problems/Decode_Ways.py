class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        def dfs(i):
            nonlocal dp
            if i in dp: # has been cached already
                return dp[i]
            if s[i] == '0': #bad base case
                return 0
            res = dfs(i+1)
            if i + 1 < len(s) and 9 < int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            dp[i] = res
            return res
        return dfs(0)

print(Solution().numDecodings('106'))


'''Brute Force Recursion
class Solution:
    def numDecodings(self, s: str) -> int:
        ans = 0
        if s[0] == '0': return 0
        def recurse(i):
            nonlocal ans
            if i < len(s):
                if i+1 < len(s)  and 9 < int(s[i:i+2]) <= 26:
                    recurse(i+2)
                if int(s[i]) != 0:
                    recurse(i+1)
            else:
                ans += 1                
        recurse(0)
        return ans
'''