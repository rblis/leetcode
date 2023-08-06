class Solution:
    def checkValidString(self, s: str) -> bool:
        left,stars = 0,0
        for c in s:
            if c == '(':
                left += 1
                stars += 1
            elif c == ')':
                left -= 1
                stars -= 1
            else:
                left -= 1
                stars += 1
            if stars < 0:
                return False
            if left < 0:
                left = 0
        return True if left == 0 else False



print(Solution().checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())()))"
))

'''
        stack = []
        stars = 0
        for c in s:
            if c == ')':
                if stack:
                    stack.pop()
                elif stars > 0:
                    stars -= 1
                else:
                    return False
            elif c == '*':
                if len(stack) > 0:
                    stack.pop()
                else:
                    stars += 1
            else:
                stack.append(c)
        print(stack)
        return True if len(stack) == 0 else False
'''