class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        values = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i, j, visited, word, board):
            if word == "":
                return True 
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or (i,j) in visited or board[i][j] != word[0]:
                return False 
            visited.add((i,j))
            result = False
            for tup in values:
                result = result or dfs(i + tup[0], j + tup[1],visited,word[1::], board)
            visited.remove((i,j))
            return result


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, set(), word, board):
                        return True

        return False 