class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []
        nums = range(1,10)
        def dfs(i,cur, tot):
            nonlocal nums, ans
            if tot == n and len(cur) == k:
                ans.append(cur)
                return
            if tot > n: return
            if i < len(nums):
                if tot + nums[i] <= n and len(cur) < k:
                    dfs(i+1, cur + [nums[i]], tot + nums[i])
                if len(cur) < k:
                    dfs(i+1, cur, tot)            
        dfs(0,[],0)
        return ans

print(Solution().combinationSum3(3,7))