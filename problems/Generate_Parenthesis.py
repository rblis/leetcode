class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def recurse(pars: str, left:int, right:int):
            if left == right  == n:
                ans.append(pars)
                return
            if left < n:
                pars += '('
                recurse(pars, left + 1, right)
            if right < left:
                pars += ')'
                recurse(pars, left, right + 1)
                
        recurse("",0,0)
        return ans

sol = Solution()
print(sol.generateParenthesis(2))