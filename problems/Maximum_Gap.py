nums = [3,6,9,1]
buckets = [ [] for x in range(len(nums)-1)]
lo, hi = float('inf'), float('inf')
for num in nums:
    if num > hi:
        hi = num
    if num < lo:
        lo = num
for num in nums:
    index = (num-lo)*(len(nums)-1)//(hi-lo)
    buckets[index].append(num)
