class Solution:
    def solve(self, board: List[List[str]]) -> None:

        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        #multisource bfs on the edge nodes
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i == 0 or i == len(board)-1 or j == 0  or j == len(board[0]) - 1):
                    q.append((i,j))
            
        while q:
            x,y = q.popleft()
            if board[x][y] == "O":
                board[x][y] = "T"
            for tx, ty in directions:
                nx, ny = x + tx, y + ty
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == "O":
                    q.append((nx, ny))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        
