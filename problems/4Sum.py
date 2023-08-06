class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4: return []
        a,b,c,d = 0,1,2,3
        ans = []
        nums.sort()
        while a < len(nums)-4:
            tot = nums[a] + nums[b] + nums[c] + nums[d]
            if target == tot:
                ans.append([a,b,c,d])
            
