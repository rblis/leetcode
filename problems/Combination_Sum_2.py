from collections import Counter
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        if sum(candidates) < target:
            return []
        ans = []
        candidates.sort()
        def dfs(i,cur, tot):
            nonlocal ans
            if tot == target:
                ans.append(cur.copy())
                return
            if i < len(candidates):
                if candidates[i] + tot <= target:
                    cur.append(candidates[i])
                    dfs(i+1, cur, tot + candidates[i])
                    cur.pop()                
                while i+1 < len(candidates):
                    if candidates[i+1] == candidates[i]:
                        i += 1
                    else:
                        break
                dfs(i+1, cur, tot)
        dfs(0,[], 0)
        return ans
            
sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))

'''
in the case where the current element isn't picked, we remove the element from being picked later down the tree branches. This ensures that the branch is unique
'''






























































# candidates = [10,1,2,7,6,1,5]
# target = 8
# candidates.sort()
# res = []
# def skip(i):
#     while i+1 < len(candidates):
#         if candidates[i+1] == candidates[i]:
#             i+= 1
#         else:
#             return i+1
#     return i+1
# def backtrack(sum, i, ans):    
#     if sum == 0:
#         res.append(ans)
#         #print(ans)
#         return
#     if i >= len(candidates):
#         return
#     if sum-candidates[i]  >= 0:   
#         ans.append(candidates[i])
#         backtrack(sum-candidates[i], i+1, [a for a in ans])
#         ans.pop()
    
#     backtrack(sum, skip(i), [a for a in ans])
    
# backtrack(target, 0, [])
# print(res)