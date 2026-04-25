class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_value =  0
        left = 0 
        right = len(heights)-1 
        while left < right:
            max_value = max(max_value, min(heights[left],heights[right]) * (right-left))
            if heights[right] <= heights[left]:
                right -= 1
            if heights[right] > heights[left]:
                left += 1
        return max_value