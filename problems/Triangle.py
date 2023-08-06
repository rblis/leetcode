class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        nums = triangle
        for i in range(len(nums)-2,-1,-1):
            for j in range(len(nums[i])):
                nums[i][j] = nums[i][j] + min(nums[i+1][j], nums[i+1][j+1])
        return nums[0][0]

print(Solution().minimumTotal([[-10]]))

