from math import ceil
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        min_time = float('inf')

        while left <= right:
            mid = (left + right) // 2
            time_to_consume = self.canEat(piles, mid)

            if time_to_consume <= h:
                right = mid - 1 
                min_time = mid
            elif time_to_consume > h:
                left = mid + 1 

        return min_time
            
    

    def canEat(self, piles: List[int], rate) -> int:
        how_many_hours = 0

        for pile in piles: 
            how_many_hours += ceil(pile / rate)
        
        return how_many_hours
 