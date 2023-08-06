from collections import deque

class MinStack:
#trick is to store a minimum value at each point in the stack
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.stack.append((val, self.min))

    def pop(self) -> None:
        self.stack.pop()
        if not len(self.stack):
            self.min = float('inf')
        else:
            self.min = self.getMin()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

stk = MinStack()
stk.push(1)
stk.push(0)
print(stk.getMin())