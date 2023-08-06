import math


class Solution:
    def waysToSplit(self, nums: list[int]) -> int:
        sums = [0]*len(nums)
        sums[0] = nums[0]
        ans = 0
        
        for i in range(1,len(nums)):
            sums[i] = nums[i] + sums[i-1]
        for i in range(len(nums)-2):
            lo, hi = i+1, len(nums)-2
            while lo < hi:
                mid = lo + hi >> 1
                if sums[i] <= sums[mid]-sums[i]:
                    hi = mid
                else:
                    lo = mid + 1
            left = lo
            lo, hi = left, len(nums)-2
            while lo < hi:
                mid = lo + math.ceil((hi - lo)/2)
                if sums[mid]-sums[i] <= sums[-1]-sums[mid]:
                    lo = mid
                else:
                    hi = mid - 1
            right = hi
            if (sums[i] <= sums[left]-sums[i] <= sums[-1]-sums[left] and 
            sums[i] <= sums[right]-sums[i] <= sums[-1]-sums[right]):
                #print(i,left, right)
                ans += right-left + 1 

        return ans % (10**9 + 7)

arr = [2,8,10,0,2]
# sums = [0]*len(arr)
# sums[0] = arr[0]
# sol = 0
# for i in range(1,len(arr)):
#     sums[i] = arr[i] + sums[i-1]
# for i in range(len(arr)-2):
#     for j in range(i+1, len(arr)-1):
#         if sums[i] <= sums[j]-sums[i] <= sums[-1]-sums[j]:
#             print(i,j)
#             print(sums[i], sums[j]-sums[i], sums[-1]-sums[j])
#             sol += 1
# print(sol)


print(Solution().waysToSplit(arr))