class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i,j, memo):
            if i < 0 or j < 0 or i == m or j == n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if i == m - 1 and j == n - 1:
                return 1
            memo[(i,j)] = helper(i + 1, j,memo) + helper(i, j + 1,memo)
            return memo[(i,j)]
        return helper(0,0, {})