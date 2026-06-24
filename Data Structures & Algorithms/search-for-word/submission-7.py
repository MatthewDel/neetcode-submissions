class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [(1,0), (-1,0), (0,-1), (0,1)]

        def helper(x_cord, y_cord, index):
            if index == len(word) - 1:
                return True

            sol = False
            for x_dir, y_dir in directions:
                x_temp = x_cord + x_dir 
                y_temp = y_cord + y_dir
                out_of_bounds = x_temp < 0 or x_temp >= len(board) or y_temp < 0 or y_temp >= len(board[0])
                if out_of_bounds or board[x_temp][y_temp] != word[index + 1] or (x_temp, y_temp) in visited:
                    continue
                visited.add((x_temp, y_temp))
                sol = sol or helper(x_temp, y_temp, index + 1)
                visited.remove((x_temp, y_temp))
            
            return sol 
        
        sol = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    sol = sol or helper(i, j, 0)
                    visited.remove((i,j))
        
        return sol


        #A B C E
        #S F C S
        #A D E E
