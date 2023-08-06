class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        back = nums[::-1]
        for i in range(1,len(nums)):
            nums[i] *= nums[i -1] or 1
            back[i] *= back[i-1] or 1
        return max(nums + back)

print(Solution().maxProduct([2,-5,-2,-4,3]))