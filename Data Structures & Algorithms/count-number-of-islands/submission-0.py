class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j,grid):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for tup in directions:
                dfs(i+tup[0], j+tup[1], grid)
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i,j,grid)
        return islands