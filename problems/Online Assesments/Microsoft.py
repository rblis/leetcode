'''
There is an array A made of N integers. Your task is to choose as many intergers from A as possible so that, when they are put in ascending order, all of the differences between all pairs of consecutive integers are equal

ie. A = [4,3,5,1,4,4] ans = [1,3,5] or [4,4,4]
'''
def equal_differences(nums: list[int]):
    nums.sort()
    ans = []
    