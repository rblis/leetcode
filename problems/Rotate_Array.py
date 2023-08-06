class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%(len(nums))
        if k == 0: return
        lo, hi = 0, len(nums)-k
        i = 0
        while i < k:
            nums[lo],nums[hi] = nums[hi], nums[lo]
            hi+=1
            lo += 1
            i += 1
        return nums

print(Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3))
#unsolved