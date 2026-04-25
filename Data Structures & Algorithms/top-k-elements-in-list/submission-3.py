

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num,0)
        
        heap = []
        for key in hashmap:
            heapq.heappush(heap, [hashmap[key], key])

            if len(heap) > k:
                heapq.heappop(heap)
        
        sol = []
        for i in range(k):
            sol.append(heapq.heappop(heap)[1])

        return sol 


        
        
