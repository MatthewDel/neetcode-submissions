class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(rate):
            ttl = 0 
            for i in range(len(piles)):
                ttl += math.ceil(piles[i]/rate)
            return ttl <= h
        
        left = 1
        right = max(piles)
        recent = 1
        while left <= right:
            mid = (left + right) // 2
            if canEat(mid):
                recent = mid
                right = mid - 1
            else:
                left = mid + 1
        return recent
                