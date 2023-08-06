from heapq import heappop, heappush
import math
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        ans = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heappush(heap, (dist,x,y))
        
        for i in range(k):
            d,x,y = heappop(heap)
            ans.append([x,y])
        return ans

sol = Solution()
print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))
