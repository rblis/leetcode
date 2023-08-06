from collections import deque



def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:

    grid = obstacleGrid
    if grid[-1][-1] or grid[0][0]:
        return 0
    if len(grid[0]) == 1 and len(grid) == 1:
        return 1


    for k in range(len(grid)):
        if not grid[k][0]:
            grid[k][0] = -1
        else:
            break
    for k in range(1,len(grid[0])):
        if not grid[0][k]:
            grid[0][k] = -1
        else:
            break
    for row in range(1,len(grid)):
        for col in range(1, len(grid[row])):
            if grid[row][col] <1:                           
                if grid[row-1][col] < 1:
                    grid[row][col] += grid[row-1][col]
                if grid[row][col-1] < 1:
                    grid[row][col] += grid[row][col-1]
    return -grid[-1][-1]
                
    
    # que = deque()#bfs
    # que.append([0,0])
    # row, col = 0,0
    # while len(que):
    #     xy = que[0]
    #     que.popleft()
    #     row = xy[0]
    #     col = xy[1]
    #     if row < len(grid)-1 and grid[row+1][col] < 1:
    #         grid[row+1][col] -= 1
    #         que.append([row+1, col])
    #     if col < len(grid[row])-1 and grid[row][col+1] < 1:
    #         grid[row][col+1] -= 1
    #         que.append([row, col+1])
    # return -grid[-1][-1]

print(uniquePathsWithObstacles(0, [[0,0,0],[0,1,0],[0,0,0]]))