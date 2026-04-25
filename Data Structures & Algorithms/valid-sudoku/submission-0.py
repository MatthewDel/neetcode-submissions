class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row check
        for row in range(len(board)):
            hash_set = set()
            for column in range(len(board[0])):
                if board[row][column] != "." and board[row][column] in hash_set:
                    return False
                else:
                    hash_set.add(board[row][column])
            #print(hash_set)
        
        # Column Check 
        for column in range(len(board[0])):
            hash_set = set()
            for row in range(len(board)):
                if board[row][column] != "." and board[row][column] in hash_set:
                    return False
                else:
                    hash_set.add(board[row][column])
            #print(hash_set)
        
        
        
        #box check 
            for bound_one in range(0,9,3):
                for bound_two in range(0,9,3):
                    hash_set = set()
                    for i in range(3):
                        for j in range(3):
                            if board[bound_one+i][bound_two+j] != "." and board[bound_one+i][bound_two+j] in hash_set:
                                return False
                            else:
                                hash_set.add(board[bound_one+i][bound_two+j])
                    


        return True 

        #box