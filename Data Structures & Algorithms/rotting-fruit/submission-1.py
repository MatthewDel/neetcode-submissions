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
                if grid[x][y] == 1:
                    rotted = True 
                    num_of_fruits -= 1
                grid[x][y] = 2
                for tup in directions:
                    if x + tup[0] < 0 or x + tup[0] == len(grid) or y + tup[1] < 0 or y + tup[1] == len(grid[0]) or grid[x + tup[0]][y + tup[1]] == 0 or grid[x + tup[0]][y + tup[1]] == 2:
                        continue
                    q.append((x + tup[0], y + tup[1]))
            if rotted:
                minutes += 1
        
        if not num_of_fruits:
            return minutes
        else:
            return -1 