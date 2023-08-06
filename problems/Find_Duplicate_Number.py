class Solution:
    def findDuplicate(self, nums: list) -> int:
        slow, fast = nums[0],nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
        ans = nums[0]
        while slow != ans:
            slow, ans = nums[slow], nums[ans]
        return ans


print(Solution().findDuplicate([1,3,4,2,2]))