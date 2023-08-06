class Solution():
    def solve(self, n: int):
        start = 1
        val = ""
        while start <= n:
            val += str(start)
            print(val)
            start += 1
        start -= 2
        while start > 0:
            print(val[:start])
            start -= 1

Solution().solve(3)


