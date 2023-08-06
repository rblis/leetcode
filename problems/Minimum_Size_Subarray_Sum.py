class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        lo,hi = 0, 0
        tot = 0
        ans = len(nums) + 1
        while lo <= hi and hi < len(nums):
            if tot < target:
                tot += nums[hi]                
                hi += 1
            else:
                #ans = min(ans, hi-lo +1)
                while tot >= target:
                    ans = min(ans, hi-lo)
                    tot -= nums[lo]
                    lo += 1
        while tot >= target:
            ans = min(ans, hi-lo)
            tot -= nums[lo]
            lo += 1
        return ans if ans <= len(nums) else 0

print(Solution().minSubArrayLen(15, [1,2,3,4,5]))