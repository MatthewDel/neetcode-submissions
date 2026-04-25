class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for i in range(len(stones)):
            heapq.heappush(max_heap, -1 * stones[i])
        while len(max_heap) > 1:
            x = -1 * heapq.heappop(max_heap)
            y = -1 * heapq.heappop(max_heap)
            if x == y: 
                continue 
            if x > y:
                heapq.heappush(max_heap, -1 * (x - y))
        
        if max_heap:
            return max_heap[0] * -1 
        else:
            return 0