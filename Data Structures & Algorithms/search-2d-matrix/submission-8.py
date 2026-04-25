class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        right = len(matrix) - 1 

        while left <= right:
            mid = (left + right) // 2 
            value = matrix[mid][0]

            if value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
            else:
                return True 
            
        row_to_binary_search = right 

        left = 0
        right = len(matrix[0]) - 1 

        while left <= right:
            mid = (left + right) // 2
            value = matrix[row_to_binary_search][mid]

            if value < target:
                left = mid + 1 
            elif value > target:
                right = mid - 1
            else:
                return True 

        return False