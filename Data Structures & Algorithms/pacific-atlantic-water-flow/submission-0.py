class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        def bfs(indices):
            nonlocal directions
            visited = set()
            q = deque(indices)
            for x, y in indices:
                visited.add((x,y))

            while q:
                row, column = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, column + dc
                    if (0 <= nr < len(heights)) and (0 <= nc < len(heights[0])) and (heights[row][column] <= heights[nr][nc]) and (nr,nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr,nc))
            return visited

        pacific_starts = [(i,0) for i in range(len(heights))] + [(0,i) for i in range(len(heights[0]))]
        atlantic_starts = [(i,len(heights[0])-1) for i in range(len(heights))] + [(len(heights)-1, i) for i in range(len(heights[0]))]

        pacific_flow = bfs(pacific_starts)
        atlantic_flow = bfs(atlantic_starts)

        result = list(pacific_flow & atlantic_flow)
        return result
        
