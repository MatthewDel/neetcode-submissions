class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        heap = []
        for key in freq:
            heapq.heappush(heap, (freq[key], key))
            if(len(heap) > k):
                heapq.heappop(heap)
        
        sol = []
        for i in range(k):
            sol.append(heapq.heappop(heap)[1])
        
        return sol