class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #A conveyor belt produces packages that must be delivered in days (int)
        #The ith package in weights has weight[i]. We load the ship with packages in the order given by weights. Cant exceed the ships weight capacity. 
        #Do a binary search to determine the minium weight capacity. 

        #Left side will start at 1 assuming 1 day 1 lbs 
        #Right side could start at the sum of all the weight. 1 day all the weight
        def can_ship(capacity):
            nonlocal days 
            curr = 1
            cap = 0
            for i in range(len(weights)):
                if (cap + weights[i]) > capacity:
                    cap = weights[i] 
                    curr += 1
                else:
                    cap += weights[i]
            return curr <= days 

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2 
            if can_ship(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left 

