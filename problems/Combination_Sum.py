class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        def dfs(i,cur, tot):
            if tot == target:
                ans.append(cur.copy())
                return
            if i < len(candidates):
                if candidates[i] + tot <= target:
                    dfs(i, cur + [candidates[i]], tot + candidates[i])
                dfs(i+1, cur, tot)
        dfs(0,[], 0)
        return ans


sol = Solution()
print(sol.combinationSum([2,3,5,7], 800))