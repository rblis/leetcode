class Solution{
    public static void dfs(int[][] grid, int row, int col, int depth) {
		if (grid[row][col] == 0 || grid[row][col] == 2) {
			return;
		} else {
            if (grid[row][col] < depth || grid[row][col] == 1){
                grid[row][col] = depth;
            }
            else{
                return;
            }
		}
        print("");
        printMap(grid);
		if (row < grid.length - 1) {
			dfs(grid, row + 1, col, depth-1);
		}
		if (row > 0) {
			dfs(grid, row - 1, col, depth-1);
		}
		if (col < grid[row].length - 1) {
			dfs(grid, row, col + 1, depth-1);
		}
		if (col > 0) {
			dfs(grid, row, col - 1, depth-1);
		}
	}

	public static int orangesRotting(int[][] grid) {
		int ans = 0;
		for (int row = 0; row < grid.length; row++) {
			for (int col = 0; col < grid[row].length; col++) {
				if (grid[row][col] == 2) {
                    grid[row][col] = -1;
					dfs(grid, row, col, 0);
				}
			}
		}
		for (int row = 0; row < grid.length; row++) {
			for (int col = 0; col < grid[row].length; col++) {
				if (grid[row][col] < 1) {
                    ans = Math.min(ans, grid[row][col]);
				}
                else if(grid[row][col] == 1){
                    return -1;
                }
			}
		}
        
		return -1*ans;
	}
}