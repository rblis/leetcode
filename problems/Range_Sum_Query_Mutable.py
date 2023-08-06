class NumArray:

    def __init__(self, nums: [int]):
        self.nums= nums
        self.sums = [0]*len(nums)
        self.sums[0] = nums[0]

        for k in range(1,len(nums)):
            self.sums[k] = nums[k] + self.sums[k-1]

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        for k in range(index,len(self.nums)):
            self.sums[k] = self.nums[k] + self.sums[k-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - self.sums[left] + self.nums[left]

obj = NumArray( [1,3,5] )
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))