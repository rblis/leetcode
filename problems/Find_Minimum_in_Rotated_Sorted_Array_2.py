class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        lo,hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + hi >> 1
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] < nums[hi]:
                lo = mid + 1
            else:
                if hi != 0 and nums[hi] >= nums[hi-1]:
                    hi -=1
                else:
                    return nums[hi]
            


print(Solution().findMin( [2,0,0,1]  ))