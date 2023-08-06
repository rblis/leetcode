from audioop import add
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        mono = deque()
        def que(x):
            nonlocal mono
            while mono and mono[-1] < x:
                mono.pop()
            mono.append(x)
        
        for i in range(k):
            que(nums[i])
        ans.append(mono[0])
        lo = 0
        for hi in range(k, len(nums)):
            que(nums[hi])            
            if nums[lo] == mono[0]: mono.popleft()
            lo += 1
            ans.append(mono[0])
        return ans



print(Solution().maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4))

