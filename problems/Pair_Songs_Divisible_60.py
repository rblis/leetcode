class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        dic = [0]*60
        ans = 0
        for t in time:
            rem = t%60
            if rem == 0:
                ans += dic[rem]
            else:
                ans += dic[60-rem]
            dic[rem] += 1        
        
        # for key in range(0,31):
        #     if key == 0 or key == 30:
        #         ans += (dic[key]-1)*(dic[key])//2
        #     else:
        #          ans += dic[key]*dic[60-key]
            

        return ans

sol = Solution()
print(sol.numPairsDivisibleBy60([60,60,60]
))
#print(sol.numPairsDivisibleBy60([418,204,77,278,239,457,284,263,372,279,476,416,360,18]))
