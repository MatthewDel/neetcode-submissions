class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        inf = 2147483647
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j,0))

        directions = [(0,1),(0,-1), (1,0), (-1,0)]
        while q:
            curr = q.popleft()
            x = curr[0]
            y = curr[1]
            pos = curr[2]
            
            if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == -1 or (grid[x][y] > 0 and grid[x][y] != inf):
                continue 
            if grid[x][y] == inf:
                grid[x][y] = pos
            for tup in directions:
                q.append((x + tup[0], y + tup[1], pos + 1))
        return
                