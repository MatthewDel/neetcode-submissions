class Solution:
    def climbStairs(self, n: int) -> int:
        right = 1
        left = 1
        if n == 1:
            return 1 

        ttl = 0
        for i in range(n - 2, -1, -1):
            ttl = left + right 
            right = left
            left = ttl
        
        return ttl 