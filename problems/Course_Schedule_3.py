'''
Course Schedule 1
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.
'''

from heapq import heappop, heappush


class Solution:
    class Node:
        def __init__(self, value) -> None:
            self.value = value
            self.nxt = []
            self.visited = 0

        def __repr__(self) -> str:
            return str(self.value)

    def canFinish(self, numCourses, prerequisites): #detect cycles
        nodesdic = {}
        nodesarr = []
        prereq = prerequisites
        for i in range(numCourses):
            temp = self.Node(i)
            nodesdic[i] = temp
            nodesarr.append(temp)

        for [a,b] in prereq:
            nodesdic[b].nxt.append(nodesdic[a])
        print(nodesarr)

        ans = []
        for node in nodesarr:
            if not self.dfs(node, ans): return False
        ans.reverse()
        print(ans)
        return True

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]: #find topological order
        nodesdic = {}
        nodesarr = []
        prereq = prerequisites
        for i in range(numCourses):
            temp = self.Node(i)
            nodesdic[i] = temp
            nodesarr.append(temp)

        for [a,b] in prereq:
            nodesdic[b].nxt.append(nodesdic[a])
        ##print(nodesarr)

        ans = []
        for node in nodesarr:
            if not self.dfs(node, ans): return []
        #print(ans)
        ans.reverse()
        return ans
            
    def dfs(self, node: Node, ans):
        if node.visited == -1: return False #if a link node revisits any other node in its chain then there is cycle
        elif node.visited == 1: return True 
        else:
            node.visited = -1 # -1 means that the current node has been visited but its links have not  
            for link in node.nxt:
                if not self.dfs(link, ans): return False
            node.visited = 1 # 1 means that the current node and all of its links have been visited
            ans.append(node)
            return True
            
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        crs = sorted(courses, key=lambda x: x[1])
        hep = []
        tot = 0
        for dur, end in crs:
            heappush(hep, -dur)
            tot += dur
            if tot > end:
                over = heappop(hep) # remove the largest time duration course to make room for other courses
                tot += over

        return len(hep)





ques = Solution()
#print(ques.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
print(ques.scheduleCourse( [[5,5],[4,6],[2,6]] ))
