class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def bs():
            lo,hi = 0, len(nums)-1
            while lo <= hi:
                mid = (lo + hi) >> 1
                if target > nums[mid]:
                    lo = mid + 1
                elif target < nums[mid]:
                    hi = mid - 1
                else:
                    return mid
            return -1
        return bs()
