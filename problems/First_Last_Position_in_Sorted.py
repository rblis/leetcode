nums = [1,1]
target = 1
rng = [-1,-1]
low, high = 0, len(nums) -1 
if len(nums) == 0:
    rng
if nums[0] == target:
    rng[0] = 0
else:
    while high >= low:
        mid = (high & low) + ((low ^ high) >> 1)
        # arr = nums[low:high+1]
        # lo, mi, hi = nums[low], nums[mid], nums[high]
        if target < nums[mid]:
            high = mid - 1
            if mid+1 < len(nums) and nums[mid+1] == target:
                rng[0] = mid -1
                break
        elif target > nums[mid]:
            low = mid + 1
            if mid + 1 < len(nums) and nums[mid+1] == target:
                rng[0] = mid+1
                break
        else:
            low -= 1
low, high = rng[0], len(nums)-1
if nums[-1] == target:
    rng[1] = len(nums)-1
else:
    while high >= low:
        mid = (high & low) + ((low ^ high) >> 1)
        # arr = nums[low:high+1]
        # lo, mi, hi = nums[low], nums[mid], nums[high]
        if target < nums[mid]:
            high = mid - 1
            if mid-1 >= 0 and nums[mid-1] == target:
                rng[1] = mid -1
                break
        elif target > nums[mid]:
            low = mid + 1
            if mid - 1 >= 0 and nums[mid-1] == target:
                rng[1] = mid+1
                break
        else:
            high += 1
# if rng[0] == -1 and rng[1] !=-1:
#     rng[1] = len(nums)-1
# elif rng[0] != -1 and rng[1] == -1:
#     rng[0] = 0
print(rng)