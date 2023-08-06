class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        roots, ranks = [x for x in range(n+1)], [1]*(n+1)

        def find(i):
            nonlocal roots
            while i != roots[i]:
                roots[i] = roots[roots[i]]
                i  = roots[i]
            return i

        def union(a,b):
            nonlocal ranks, roots
            aa,bb = find(a), find(b)
            if aa == bb:
                return False
            if ranks[aa] > ranks[bb]:
                roots[bb] = aa
                ranks[aa] += ranks[bb]
            else:
                roots[aa] = bb
                ranks[bb] += ranks[aa]
            return True
        eject = []
        for x,y in edges:
            if not union(x,y): eject.append([x,y])
        return eject[-1]


print(Solution().findRedundantConnection([[1,2],[2,3],[1,3]]))
#[[1,2],[2,3],[3,4],[1,4],[1,5]]