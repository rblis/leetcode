class Solution:
    def sumZero(self, n: int) -> list[int]:
        ans = []
        if n == 1:
            return [0]
        if n%2: #even
            lo,hi = -n,n
            while n-3 > 0:
                ans.append(lo)
                ans.append(hi)
                lo += 1
                hi -= 1
                n-= 2
            ans.append(1)
            ans.append(2)
            ans.append(-3)
        else:
            lo,hi = -n,n
            while n > 0:
                ans.append(lo)
                ans.append(hi)
                lo += 1
                hi -= 1
                n-= 2
        return ans

print(Solution().sumZero(2))