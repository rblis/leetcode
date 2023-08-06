import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        lo,hi = 1, max(piles)
        k = 0
        while lo <= hi:
            mid = hi + lo >> 1
            tot=0
            for num in piles:
                tot += math.ceil(num/mid)
            if tot <= h:
                k = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return k
#print(3+6>>1)
sol = Solution()
vals = [332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]


h = 823855818
print(sol.minEatingSpeed(vals, h))