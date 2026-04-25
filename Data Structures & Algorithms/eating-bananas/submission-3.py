from math import ceil
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)

        def can_consume(rate):
            nonlocal h
            hours = 0
            for i in range(len(piles)):
                hours += ceil(piles[i] / rate)
            return hours <= h 


        while left <= right:
            mid = (left + right) // 2 
            result = can_consume(mid)

            if result:
                right = mid - 1
            else:
                left = mid + 1
        
        return left 
                