from collections import Counter

def check(a,b):
    c = {}
    for key in a:
        c[key] = a[key]
    for key in b:
        if key in c:
            c[key] += b[key]
        else:
            c[key] = b[key]
    odd = False
    for key in c:
        if c[key] % 2 != 0:
            if not odd:
                odd = False
            else:
                return False

def countComplementaryPairs(stringData):
    # Write your code here
    counts = []*len(stringData)
    for word in stringData:
        counts.append(Counter(word))
    ans = 0
    for i in range(len(counts)):
        for j in range(len(counts)):
            if i != j and check(counts[i], counts[j]):
                ans += 1
                
    return ans

#print(countComplementaryPairs(['ball','all','call','bal']))


def MaximumScore(nums: int, k: int) -> int:
    ans = 0
    sums = [0]*len(nums)
    sums[0] = nums[0]

    for i in range(len(nums)):
        sums[i] = nums[i] + sums[i-1]

    lo,hi = 0, len(nums)-1
    for i in range(k-1, -1, -1):
        score = float('-inf')
        index = lo
        nums = nums[lo:hi+1]
        for j in range(lo, hi+1):
            if (nums[j] > score and 
            ((j + i < len(nums) and sums[hi]-sums[j+1] > sums[j-1] - sums[lo - 1]) or j >= i)):
                score = nums[j]
                index = j
        ans += score
        if sums[index-1]-sums[lo] > sums[hi]-sums[index] and index >= i:
            hi = index-1
        else:
            lo = index + 1

    print(sums)

    return ans

print(MaximumScore([4,5,-10,-1,10,-20], 4))
