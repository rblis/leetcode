class Solution:
    def canJump(self, nums: list[int]) -> bool:
        jump = nums[0]
        if len(nums) == 1: return True
        for i in range(1,len(nums)):
            if not jump: return False
            jump = max(nums[i], jump-1)
        return True


class Solution1:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1 or nums[0] >= len(nums):
            return True
        if nums[0] == 0:
            return False
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)-1):
            dp[i] = max(nums[i], dp[i-1]-1)
            if dp[i] == 0: return False
        return dp[-2] >= 1


print(Solution().canJump([1,1,1,0]))