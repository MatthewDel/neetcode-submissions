class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        column_dict = defaultdict(set)
        square_dict = defaultdict(set)

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] != "." and (board[row][column] in row_dict[row] or board[row][column] in column_dict[column] or board[row][column] in square_dict[(row//3,column//3)]):
                    return False
                row_dict[row].add(board[row][column])
                column_dict[column].add(board[row][column])
                square_dict[(row//3,column//3)].add(board[row][column])
        return True