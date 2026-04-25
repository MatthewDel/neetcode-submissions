class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0 
        num_of_fruits = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    num_of_fruits += 1 
                
        directions = [(0,1), (1,0), (0,-1), (-1, 0)]
        while q:
            rotted = False
            for i in range(len(q)):
                curr = q.popleft()
                x = curr[0]
                y = curr[1]
                if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == 0 or grid[x][y] == 3:
                    continue
                if grid[x][y] == 1:
                    rotted = True 
                    num_of_fruits -= 1
                grid[x][y] = 3
                for tup in directions:
                    q.append((x + tup[0], y + tup[1]))
            if rotted:
                minutes += 1
        
        if num_of_fruits == 0:
            return minutes
        else:
            return -1 