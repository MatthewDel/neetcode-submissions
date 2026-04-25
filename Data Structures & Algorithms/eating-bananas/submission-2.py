class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(speed): 
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / speed)
            return hours <= h

        min_speed = 0
        left = 1 
        right = max(piles)

        while left<=right:
            mid = (left + right) // 2
            if canEat(mid):
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return min_speed


                