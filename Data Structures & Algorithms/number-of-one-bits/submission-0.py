class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        comparison = 1 
        for i in range(32):
            count += comparison & n
            n = n >> 1
        return count