class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validate(k):
            count = 0 
            for pile in piles:
                count += math.ceil(pile  / k)
            if count > h:
                return False 
            else:
                return True 
        latest = -1
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2 
            res = validate(mid)
            if res:
                latest = mid
                right = mid - 1 
            elif not res:
                left = mid + 1
        return latest 
