class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        edges = 0
        ans = []
        rows,cols = len(matrix), len(matrix[0])
        def right(start,end, row):
            nonlocal ans
            while start < end:
                ans.append(matrix[row][start])
                start += 1
        def left(start,end, row):
            nonlocal ans
            while start >= end:
                ans.append(matrix[row][start])
                start -= 1
        def down(start,end, col):
            nonlocal ans
            while start < end:
                ans.append(matrix[start][col])
                start += 1
        def up(start,end, col):
            nonlocal ans
            while start >= end:
                ans.append(matrix[start][col])
                start -= 1
        while edges <= min(rows//2, cols//2):
            right(edges, cols-edges, edges)
            if len(ans) == rows*cols: break
            down(edges+1, rows-edges-1, cols-edges-1)
            if len(ans) == rows*cols: break
            left( cols-edges-1, edges, rows-edges-1)
            if len(ans) == rows*cols: break
            up( rows-edges-2,edges+1, edges)
            edges += 1

        return ans

print(Solution().spiralOrder(matrix = [[0]]))