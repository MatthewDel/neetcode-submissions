class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        amount_of_fresh = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    amount_of_fresh += 1
        
        time = 0
        while queue and amount_of_fresh > 0:
            for i in range(len(queue)):
                x,y = queue.popleft()
                for dir_x, dir_y in directions:
                    if (x + dir_x) >= 0 and (x + dir_x) < len(grid) and (y + dir_y) >= 0 and (y + dir_y) < len(grid[0]) and grid[(x + dir_x)][(y + dir_y)] == 1: 
                        grid[(x + dir_x)][(y + dir_y)] = 2
                        queue.append(((x + dir_x), (y + dir_y)))
                        amount_of_fresh -= 1
            time += 1
        
        if amount_of_fresh == 0:
            return time
        else:
            return -1
                        

