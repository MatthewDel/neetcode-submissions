class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)] 
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, value in count.items():
            freq[value].append(num)
        
        sol = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                sol.append(num)
                if len(sol) == k:
                    return sol
        
        return -1