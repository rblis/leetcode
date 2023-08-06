class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [0]*len(nums) #keeps track of the longest subsequence at each point
        ans = float('-inf')
        for i in range(len(nums)-1,-1,-1):#iterate backwards
            res = 1
            for j in range(i+1, len(nums)):#iterate through the backwards subsequence
                if nums[i] < nums[j]: #if the start of the sequence is smaller than any subsequent values in the sequence
                    res= max(res, dp[j]+1) #we set it as the res if it is the largest val
            dp[i] = res #we set the max increasing subsequence at this point in nums
            ans = max(res, ans) #update ans to be longest subsequence
        return ans


print(Solution().lengthOfLIS([4,10,4,3,8,9]))