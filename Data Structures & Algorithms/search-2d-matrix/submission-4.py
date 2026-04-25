class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2 
            if matrix[mid][0] < target:
                left = mid + 1 
            elif matrix[mid][0] > target:
                right = mid - 1 
            else:
                return True 
    
        row = right
        
        left = 0 
        right = len(matrix[0])-1
        while left<=right:
            mid = (left + right) // 2 
            if matrix[row][mid] < target:
                left = mid + 1 
            elif matrix[row][mid] > target:
                right = mid - 1 
            else:
                return True 
        
        return False