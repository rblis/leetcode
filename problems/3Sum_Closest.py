nums = [1,1,1,0]
target = 100
nums.sort()
diff = float('inf')
size = len(nums)
ans = nums[0] + nums[1] + nums[2]
for left in range(size-2):
    mid = left + 1
    right = size - 1
    while mid < right:
        sum = nums[left] + nums[mid] + nums[right]
        if abs(target-sum) < diff:
            diff = abs(target-sum)
            ans = sum
        if sum > target:
            right -= 1
        elif sum < target:
            mid += 1
        else:
            print(sum)
            break
print(ans)