'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
def binary_search(nums, target, lo, hi):
    while (lo <= hi):
        mid = (hi + lo) >> 1
        if nums[mid][0] == target:
            return mid
        elif nums[mid][0] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def twoSum(nums: list[int], target: int):
    siz = len(nums)
    nums = list(zip(nums, range(siz)))
    nums.sort()
    
    for i in range(siz-1):
        rem = target - nums[i][0]
        if i+1 == siz-1:
            return [nums[i][1] ,nums[-1][1]] 
        res = binary_search(nums, rem, i + 1, siz-1)
        if res != -1:
            return [nums[i][1], nums[res][1]]
    return []

print(twoSum([3,2,4], 6))