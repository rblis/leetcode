class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = []
        cet = set()
        def recurse(index, res):
            nonlocal ans
            if index >= len(nums):
                res.sort()
                tup = tuple(res)
                if tup not in cet:
                    ans.append(res)
                    cet.add(tup)
                return
            recurse(index + 1, res + [nums[index]])
            recurse(index + 1, res)
        recurse(0,[])
        return ans

sol = Solution()
print(sol.subsetsWithDup([1,2,2,2]))


        