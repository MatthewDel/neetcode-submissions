class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1 

        max_len = 0

        while left < right:
            max_len = max(max_len, (min(heights[right], heights[left]) * (right-left)))
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                right -= 1
        
        return max_len