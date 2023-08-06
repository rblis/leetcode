class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        def dfs(start, cur):
            if len(cur) >= k:
                ans.append(cur.copy())
                return
            if start < n + 1:
                cur.append(start)
                dfs(start + 1, cur)
                cur.pop()
                dfs(start + 1, cur)
        dfs(1,[])
        return ans