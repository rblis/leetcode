'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
'''

class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        ans, i = 1, 0
        while i < len(nums): #goal is to shift the i pointer based on the best jump available
            max_jump, index, j, end = float('-inf'), i, i+1, i+nums[i] + 1
            if end >= len(nums): return ans
            while j < end:
                #the farthest combined index + jump position found 
                if j + nums[j] >= index + max_jump:
                    max_jump, index = nums[j], j
                j += 1
            i = index
            ans += 1
        return ans

'''
3 cases
[1] from start jump to end == 1 jump
[2] from start find an index that jumps to the end == 2 jumps
[3] from start find maximal distance that doens't reach the last index

more efficient version

jumps, end, longest = 0, 0, 0
for i in range(len(nums)-1):
    longest = max(longest, i + nums[i])
    if i == end:
        end = longest
        jumps += 1

'''