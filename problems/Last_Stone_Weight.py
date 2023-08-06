from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heep = []
        for stone in stones:
            heappush(heep,-stone)
        while len(heep) > 1:
            y,x = heappop(heep), heappop(heep)
            if x != y:
                heappush(heep, y-x)
        return -heep[0] if len(heep) else 0

