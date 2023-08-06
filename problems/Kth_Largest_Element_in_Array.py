from heapq import heappop, heappush


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heep = []
        for num in nums:
            heappush(heep, -num)
        for i in range(k-1):
            heappop(heep)
        return -heappop(heep)
