from cmath import inf


class Solution:
    def totalStrength(self, strength: list[int]) -> int:
        ans = 0
        strn = strength
        size = len(strn)
        psum = [0]*size
        psum[0] = strn[0]
        for i in range(1,size):
            psum[i] = psum[i-1] +strn[i]
        
        for i in range(len(strength)):
            tot = 0
            minv = float('inf')
            for j in range(i,len(strength)):
                tot = psum[j]-psum[i]+strn[i]
                minv = min(minv, strn[j])
                ans += tot*minv
            
        return ans % (10**9 + 7)


print(Solution().totalStrength([1,3,1,2]))

'''
        def recurse(i, tot, minv):
            nonlocal ans
            if i < len(strength):
                if strength[i] < minv:
                    minv = strength[i]
                tot += strength[i]
                val = minv*tot
                ans += val
                recurse(i+1, tot, minv)
        for i in range(len(strength)):
            recurse(i,0,float('inf'))

'''
#9476