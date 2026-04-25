class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hashmaps = [0] * 9 
        col_hashmaps = [0] * 9
        square_hashmaps = [0] * 9

        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                if value == '.':
                    continue

                row_hashmap = row_hashmaps[row]
                col_hashmap = col_hashmaps[col]
                square_hashmap = square_hashmaps[((row // 3) * 3) + (col // 3)]

                value = int(value)
                left_shifted = 1 << value
                if (left_shifted & row_hashmap) or (left_shifted & col_hashmap) or (left_shifted & square_hashmap):
                    print((left_shifted & col_hashmap) == 0)
                    return False
                
                row_hashmaps[row] = left_shifted | row_hashmap
                col_hashmaps[col] = left_shifted | col_hashmap
                square_hashmaps[((row // 3) * 3) + (col // 3)] = left_shifted | square_hashmap
            
        return True
