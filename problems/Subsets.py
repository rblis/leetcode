
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def recurse(index, res):
            nonlocal ans
            if index >= len(nums):                
                ans.append(res)
                return
            recurse(index+1, res+[nums[index]])                
            recurse(index+1, res)

        recurse(0,[])
        return ans 

sol = Solution()
print(sol.subsets([1,2,3]))