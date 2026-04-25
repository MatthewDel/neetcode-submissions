class Solution:
    def canShip(self, weights, capacity):
        if max(weights) > capacity:
            return float('inf')
            
        ttlDays = 1
        current_day = 0
        for weight in weights:
            if (current_day + weight) > capacity:
                ttlDays += 1
                current_day = weight
            else:
                current_day += weight

        return ttlDays 

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Within days or hours like koko
        # Each index has a weight
        # conveyor belt eats 

        left = 1 
        right = sum(weights)
        min_time = 0
        while left <= right:
            mid = (left + right) // 2 
            ship_state = self.canShip(weights, mid)
            print(mid, ship_state)
            if ship_state > days:
                left = mid + 1
            else:
                min_time = mid
                right = mid - 1

        return min_time


        
    