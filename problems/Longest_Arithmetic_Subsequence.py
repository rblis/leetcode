class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0
        def recurse(i, diff, last, sz):
            nonlocal ans
            if i >= len(nums):
                ans = max(ans, sz)
                return 
            if last > -1:
                if diff == -1:
                    recurse(i+1, nums[i]-last, nums[i], 2)
                else:
                    if nums[i]-last == diff:
                        recurse(i+1, diff, nums[i], sz + 1)
                    else:
                        recurse(i+1, diff, last, sz)
            else:
                recurse(i+1, diff, nums[i], 1)
        
        for i in range(len(nums)):
            recurse(i,-1,-1, 0)
        return ans

print(Solution().longestArithSeqLength( [20,1,15,3,10,5,8] ))

#need DP Solution