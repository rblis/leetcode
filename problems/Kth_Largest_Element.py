import heapq #min priority que, to use max priority que, multiply every element by -1 or change the comparison 
#methods for the ADT

def solve(nums, k):
    heapq.heapify(nums)
    hep = nums
    answer = 0
    for i in range(k-1):
        heapq.heappop(hep)
    return hep[0]

print(solve([1,19,3,17,5,15,7,13,9,11], 2))
        