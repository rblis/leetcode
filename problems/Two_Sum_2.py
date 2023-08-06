import enum


class Solution:
    def twoSumDIC(self, numbers: list[int], target: int) -> list[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [i+1, dic[target-num] + 1]
            dic[num] = i
        return []


    def twoSumBST(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            rem = target - numbers[i]
            res = self.dfs(numbers, rem, i+1, len(numbers)-1)
            if res != -1:
                return [i +1, res +1]
        return []
    
    def dfs(self, nums, target, lo, hi):
        while lo <= hi:
            mid = (hi+lo) >> 1 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1 

sol = Solution()
print(sol.twoSum([2,3,4], 6))