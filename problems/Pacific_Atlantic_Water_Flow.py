class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ans = []
        anset = set()
        pac, atl = False, False
        def dfs(row: int, col: int, visit: set):
            nonlocal pac, atl, anset
            if (row,col) in anset: return True
            if row == 0 or col == 0: pac = True
            if row == len(heights)-1 or col == len(heights[0])-1: atl = True
            if pac and atl: return True
            if (row,col) in visit: return False
            visit.add((row,col))
            if col < len(heights[0])-1 and heights[row][col+1] <= heights[row][col] and dfs(row, col+1, visit.copy()): return True
            if row < len(heights)-1 and heights[row+1][col] <= heights[row][col] and dfs(row+1, col, visit.copy()): return True
            if col > 0 and heights[row][col-1] <= heights[row][col] and dfs(row, col-1, visit.copy()): return True
            if row > 0 and heights[row-1][col] <= heights[row][col] and dfs(row-1, col, visit.copy()): return True
            return False
        for row in range(len(heights)):
            for col in range(len(heights[row])):
                pac, atl = False, False
                if dfs(row, col, set()):
                    ans.append([row,col])
                    anset.add((row,col))
        
        return ans

print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))