class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n, memo):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            elif n < 0:
                return 0
        
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            memo[n] = result
            return result
        return helper(n, {})
