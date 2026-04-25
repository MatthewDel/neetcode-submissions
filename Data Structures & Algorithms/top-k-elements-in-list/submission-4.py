

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums))] 

        for i in range(len(nums)):
            count[nums[i]] =  1 + count.get(nums[i], 0)

        for key in count:
            frequency[count[key]-1].append(key)

        sol = []

        for i in range(len(frequency)-1, -1, -1):
            for num in frequency[i]:
                sol.append(num)
                if len(sol) == k:
                    return sol

        return sol 




        
        
