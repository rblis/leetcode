class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        bs = sorted(nums)
        def search(target):
            nonlocal bs
            lo, hi = 0, len(nums)-1
            while lo <= hi:
                mid = lo + hi >> 1
                if bs[mid] < target:
                    lo = mid + 1
                elif bs[mid] > target:
                    hi = mid -1 
                else:
                    return mid
        ans = [0]*len(nums)
        for i,num in enumerate(nums):
            index = search(num)
            ans[i] = len(nums)-1-index
        return ans

print(Solution().countSmaller())

#Doesn't Work