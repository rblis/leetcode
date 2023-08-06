class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        front, back, ans = [1]*len(nums), [1]*len(nums), [1]*len(nums)
        front[0], back[-1] = nums[0], nums[-1]
        for i in range(1,len(nums)):
            front[i] = nums[i]*front[i-1]
            back[len(nums)-i-1] = nums[len(nums)-i-1]*back[len(nums)-i]
        ans[0], ans[-1] = back[1], front[-2]
        for i in range(1, len(nums)-1):
            ans[i] = front[i-1] * back[i+1]
        return ans
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))


'''
class Solution:
    def productExceptSelf(self, nums):
        ans, suf, pre = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre               # prefix product from one end
            pre *= nums[i]
			ans[-1-i] *= suf            # suffix product from other end
			suf *= nums[-1-i]
        return ans
'''