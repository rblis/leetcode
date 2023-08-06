# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sz = len(nums)
        if sz < 3:
            return []
        nums.sort()
        sums = set()
        ans = []
        for i in range(sz-2):
            lo, hi = i + 1, sz-1
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            while lo < hi:
                triple = nums[i] + nums[lo] + nums[hi]

                if triple < 0:
                    lo += 1
                    while nums[lo] == nums[lo-1]:
                        lo += 1
                    
                elif triple > 0:
                    hi -= 1
                    while nums[hi] == nums[hi+1]:
                        hi-= 1
                else:
                    if (nums[i] , nums[lo] , nums[hi]) not in sums:
                        ans.append([nums[i], nums[lo], nums[hi]])
                    sums.add((nums[i] , nums[lo] , nums[hi]))
                    lo +=1
                    hi -= 1
        return ans
sol = Solution()
print(sol.threeSum([-2,0,1,1,2]))





























# nums = [-4,-1,-1,0,1,2]#[-1,0,1,2,-1,-4]
# nums.sort()
# size = len(nums)
# ans = []
# sols = set()
# for left in range(0, size-2):
#     mid, right = left + 1, size-1
#     while mid < right:
#         sum = nums[left] + nums[mid] + nums[right]
#         if sum < 0:
#             mid += 1
#         elif sum > 0:
#             right -= 1
#         else:
#             triple = (nums[left], nums[mid], nums[right])
#             if triple not in sols:
#                 sols.add((nums[left], nums[mid], nums[right]))
#                 sols.add((nums[left], nums[right], nums[mid]))
#                 sols.add((nums[mid], nums[left], nums[right]))
#                 sols.add((nums[mid], nums[right], nums[left]))
#                 sols.add((nums[right], nums[mid], nums[right]))
#                 sols.add((nums[right], nums[left], nums[mid]))

#                 ans.append([nums[left], nums[mid], nums[right]])
#             mid += 1
#             right -= 1
# print(ans)
        