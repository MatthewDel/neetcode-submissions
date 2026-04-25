class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2 
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1 
        
        row = right 
        left = 0
        right = len(matrix[0]) - 1 

        while left <= right:
            mid = (right + left) // 2 
            if(matrix[row][mid] == target):
                return True 
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False