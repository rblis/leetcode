import collections
#create adjacency list where every course has a list of prereqs
#do a dfs until we reach a node without any prereqs
#maintain a path set to check for cycles
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        visited, cycle = set(), set()
        def dfs(course):
            nonlocal visited, cycle, adj
            if course in visited: return True
            if course in cycle: return False
            cycle.add(course)
            for crs in adj[course]:
                if not dfs(crs): return False
            cycle.remove(course)
            visited.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True

print(Solution().canFinish(3,
[[0,1],[0,2],[1,2]]
))