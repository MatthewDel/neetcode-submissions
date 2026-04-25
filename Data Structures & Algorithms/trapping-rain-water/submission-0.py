class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        sol = 0
        arr = [0] * len(height)
        for i in range(len(height)):
            arr[i] = max_left
            max_left = max(max_left, height[i])
        print(arr)
        
        for i in range(len(height)-1, -1, -1):
            arr[i] = min(arr[i], max_right)
            calc = arr[i] - height[i]
            if calc > 0:
                sol += calc 
            max_right = max(max_right, height[i])
        
        return sol 