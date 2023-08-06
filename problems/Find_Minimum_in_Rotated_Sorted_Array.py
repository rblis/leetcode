class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] < nums[-1]: return nums[0]
        hi,lo = len(nums)-1, 0
        while hi >= lo:
            mid = hi + lo >> 1
            print(lo, mid, hi)
            if mid == len(nums)-1 or nums[mid+1] > nums[mid] < nums[mid-1]: 
                return nums[mid]
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid - 1
        

print(Solution().findMin([9,10,2,4,5,6,7,8]))
# print(Solution().findMin([5,1,2,3,4]))
# print(Solution().findMin([3,4,5,1,2]))