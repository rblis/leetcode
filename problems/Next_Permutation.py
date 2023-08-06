class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        if index == -1:
            nums.sort()
        else:
            for i in range(index + 1, len(nums)):
                if nums[i] <= nums[index]:
                    nums[i-1], nums[index] = nums[index], nums[i-1]
                    break
                if i == len(nums)-1:
                    nums[i], nums[index] = nums[index], nums[i]
            start, end = index + 1, len(nums) -1
            while start < end:
                nums[start],nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        return nums

print(Solution().nextPermutation([1,5,1]))