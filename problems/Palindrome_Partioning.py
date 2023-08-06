class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        dp = set()
        def check(pal):
            nonlocal dp
            if pal in dp: return True
            le,ri = 0, len(pal)-1
            while le < ri:
                if pal[le] != pal[ri]:
                    return False
                le+=1
                ri -= 1
            dp.add(pal)
            return True
        
        def part(i, curr):
            nonlocal ans
            if i >= len(s): 
                ans.append(curr.copy())
                return
            for j in range(i, len(s)):
                pal = s[i:j+1]
                if check(pal):
                    curr.append(pal)
                    part(j+1,curr)
                    curr.pop()
        part(0, [])
        return ans

sol = Solution()
print(sol.partition('aab'))
