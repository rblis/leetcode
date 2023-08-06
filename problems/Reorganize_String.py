from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = [''] * len(s)
        counts = Counter(s)
        def findMax(counts):
            most = 0
            val = 'A'
            for c in counts:
                if most < counts[c]:
                    val = c
                    most = counts[c]
            return val
        def findMin(counts):
            least = float('inf')
            val = 'A'
            for c in counts:
                if least > counts[c]:
                    val = c
                    least = counts[c]
            return val
        i = 0
        top = findMax(counts)
        while i < len(s):
            ans[i] = top
            counts[top] -= 1
            i += 2
            if counts[top] == 0:
                counts.pop(top)
                top = findMax(counts)
        i = 1
        bot = findMin(counts)
        while i < len(s):
            ans[i] = bot
            counts[bot] -= 1
            i += 2
            if counts[bot] == 0:
                counts.pop(bot)
                bot = findMax(counts)
        return ''.join(ans)
        
print(Solution().reorganizeString("cocgcickmlmsmtbwbxoz"
))