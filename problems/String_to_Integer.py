class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ''
        pos = True
        sign = ''
        start = False
        minval, maxval = -2**31, 2**31-1
        for c in s:
            if not start:
                if c == '-':
                    pos = not pos
                    if sign != '':
                        return 0
                    sign = '-'
                elif c == '+':
                    if sign != '':
                        return 0
                    sign = '+'
                elif c.isdigit():
                    start = True
                    ans = c
                elif c == ' ': 
                    if sign != '':
                        return 0
                    
                else:
                    return 0
            else:
                if c.isdigit():
                    ans += c
                else:
                    break
        if not start:
            return 0
        ans = int(ans) if pos else -int(ans)
        if ans < minval:
            return minval
        elif ans > maxval:
            return maxval
        else:
            return ans 


print(Solution().myAtoi("+1"
))