import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        ans, visit, cycle = [], set(), set()
        def dfs(course):
            nonlocal ans, visit, cycle, adj
            if course in cycle: return False
            if course in visit: return True
            cycle.add(course)
            for crs in adj[course]:
                if not dfs(crs): return False
            visit.add(course)
            cycle.remove(course)
            ans.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i): return []
        return ans


print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
[[1,0],[2,0],[0,2]]
