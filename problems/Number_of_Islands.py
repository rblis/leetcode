# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally
#  or vertically. You may assume all four edges of the grid are all surrounded by water.





def recurse(grid, row, col):
    grid[row][col] = 'x'
    
    if row + 1 < len(grid) and grid[row + 1][col] == '1':
        recurse(grid, row + 1, col)
    if row - 1 >= 0 and grid[row - 1][col] == '1':
        recurse(grid, row - 1, col)
    if col + 1 < len(grid[0]) and grid[row][col+1] == '1':
        recurse(grid, row , col+ 1)
    if col - 1 >= 0 and grid[row][col - 1] == '1':
        recurse(grid, row , col - 1)
    

def numIslands(grid) -> int:
    count = 0;
    print(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                count += 1
                recurse(grid, i, j)
    print(grid)
    return count





print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))




# def recurse(grid, row, col, count):
#     grid[row][col] = str(count)
#     if row < len(grid)-1:
#         if grid[row+1][col] == '1':
#             recurse(grid, row+1, col, count)
#     if row > 0:
#         if grid[row-1][col] == '1':
#             recurse(grid, row-1, col, count)
#     if col < len(grid[row])-1:
#         if grid[row][col+1] == '1':
#             recurse(grid, row, col+1, count)
#     if col > 0:
#         if grid[row][col-1] == '1':
#             recurse(grid, row, col-1, count)
    




# def numIslands(grid) -> int:
#     count = 1
#     for row in range(len(grid)):
#         for col in range(len(grid[row])):
#             if grid[row][col] == '1':
#                 count += 1
#                 recurse(grid, row, col, count)
                

#     return count-1

# print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

