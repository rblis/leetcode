class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        def pivot():
            lo,hi = 0, len(nums)-1
            while lo <= hi:
                mid = lo + hi >> 1
                if len(nums)-1 == mid or nums[mid-1] > nums[mid] < nums[mid+1]:
                    return mid
                elif nums[mid] < nums[hi]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        mid = pivot()
        lo,hi = 0,mid
        if nums[lo] > target or mid == lo:
            lo,hi = mid, len(nums)-1
        while lo <= hi:
            mid = hi + lo >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
        



sol = Solution()
print(sol.search([5,1,2,3,4], 1))






































































# nums = [4,5,1,2,3]  # [5,1,2,3,4] 1 [4,5,6,7,8,1,2,3] 8
# target = 1
# ans = -1
# high = len(nums)-1
# low = 0
# while high > low:# find the pivot point where the array was shifted
#     mid = (low & high) + ((low ^ high) >> 1)
#     arr = nums[low:high+1]
#     lo, mi, hi = nums[low], nums[mid], nums[high]
#     if nums[mid] > nums[high]:
#         #high = mid - 1
#         low = mid + 1 
#     else:
#         #low = mid + 1 
#         high = mid 
# # print(low)
# if nums[low ] <= target <= nums[-1]: #determine which side the target value falls in
#     low, high = low , len(nums)-1
# else:
#      high, low = low , 0
# # print(low, high)
# while high >= low:#regular binary search
#     mid = (high + low) // 2
#     arr = nums[low:high+1]
#     lo, mi, hi = nums[low], nums[mid], nums[high]
#     if target > nums[mid]:
#         low = mid + 1
#     elif target < nums[mid]:
#         high = mid - 1
#     else:
#         ans = mid
#         break
# if low==high:
#     ans = low
# print(ans)

'''
while low <= high:
    mid = (high + low) // 2
    arr = nums[low:high+1]
    lo, mi, hi = nums[low], nums[mid], nums[high]
    
    if nums[mid] > target:
        if nums[low] > target \
            and nums[high] >= target:
            low = mid + 1
        else:
            high = mid - 1
    elif nums[mid] < target:
        if nums[high] < target \
            and nums[low] >= target:
            high = mid - 1
        else:
            low = mid + 1 
    else:
        ans = mid
        break


    while low <= high:
    mid = (high + low) // 2
    arr = nums[low:high+1]
    lo, mi, hi = nums[low], nums[mid], nums[high]
    
    if nums[mid] > target: #target on the left
        if nums[mid] > nums[low] and nums[low] <= target: #left is ordered
            high = mid -1
        else:
            if target < nums[low] and nums[high] < target:
                #low = mid + 1
                high = mid - 1
            else:
                low = mid + 1
                #high = mid - 1
    elif nums[mid] < target: #target on the right
        if nums[mid] < nums[high] and nums[high] >= target: # right side is ordered
            low = mid + 1
        else:
            if target > nums[high] and nums[low] < target:# |4,5,6,|7|,8,1,2,3| or |8 1 2 |3| 4 5 6 7| 
                low = mid + 1
                #high = mid - 1
            else:
                #low = mid + 1
                high = mid - 1
    else:
        ans = mid
        break
'''