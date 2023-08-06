import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) < 2:
            return tokens[0]
        stack = []
        a,b = 0,0
        for token in tokens:
            if token == '+':
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == '-':
                if len(stack) == 1:
                    stack.append(-stack.pop())
                else:
                    b, a = stack.pop(), stack.pop()
                    stack.append(a-b)
            elif token == '*':
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif token == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[0]
        
sol = Solution()
print(6/132)
#print(sol.evalRPN(['10','5','/']))
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))