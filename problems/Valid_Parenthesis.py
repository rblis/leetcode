from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = deque()
        
        for let in s:
            if let == ')':
                if not len(stack) or stack.pop() != '(':
                    return False
            elif let == ']':
                if not len(stack) or stack.pop() != '[':
                    return False
            elif let == '}':
                if not len(stack) or stack.pop() != '{':
                    return False
            else:
                stack.append(let)
        return len(stack) == 0

sol = Solution()
print(sol.isValid('()'))