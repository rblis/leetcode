class Solution:
    def convert(self, s: str, numRows: int) -> str:
        size = len(s)
        if size < 3 or numRows == 1:
            return s
        ans = ""
        jump = numRows*2-2
        for row in range(numRows):
            index = row
            while index < size:
                if row == 0 or row == numRows-1:
                    ans += s[index]
                    index += jump
                else:
                    ans += s[index]
                    index += jump - row*2
                    if index >= size: break
                    ans += s[index]
                    index += row*2
        return ans

print(Solution().convert('WAT', 1))
