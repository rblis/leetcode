class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        valid = [True]*len(nums)
        def recurse(res):
            nonlocal ans, valid
            if len(res) == len(nums):
                ans.append(res)
                return
            for i in range(len(nums)):
                if valid[i]:
                    valid[i] = False
                    recurse(res+[nums[i]])
                    valid[i] = True
        recurse([])
        return ans

sol = Solution()
print(sol.permute([1,2,3]))