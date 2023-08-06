class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = nums[0]
        cur = nums[0]
        for i in range(1,len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[i]
            ans = max(ans, cur)
        return ans

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))






































# def maxSubArray(self, nums: [int]) -> int:
#     temp = 0
#     maxx = -1*float('inf')
#     for k in range(len(nums)):
#         temp = max(nums[k], nums[k] + temp) #cur sum ? cur sum + new elem
#         maxx = max(temp, maxx)
#     Kadame's Algorithm
#     sums = [0]*len(nums)
#     sums[0] = nums[0]
#     maxx = sums[0]
#     for k in range(1, len(nums)):
#         sums[k] = nums[k] + sums[k-1]
#     start, end = 1,0
#     while start < len(nums):
#         window = sums[start] - sums[end] + nums[end]

#         if window > maxx:
#             maxx = window

#         if window <= 0 or nums[end] < 0:
#             if nums[start] > 0:
#                 end = start
#             else:
#                 end = start + 1
#                 start += 1
        
#         start += 1

#     for end in range(len(nums)):
#         for start in range(end+1, len(nums)):
#             window = sums[start] - sums[end] + nums[end]
#             if window > maxx: 
#                 maxx=window
    
#     return maxx


# print(maxSubArray(0, [-2,1,-3,4,-1,2,1,-5,4] ))