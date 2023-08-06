class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []
        maps = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
            }
        ans = []
        def dfs(i, curr):
            nonlocal ans, maps
            if i == len(digits):
                ans.append(''.join(curr))
                return
            for c in maps[digits[i]]:
                curr.append(c)
                dfs(i+1,curr)
                curr.pop()
        dfs(0,[])

        return ans

print(Solution().letterCombinations(''))