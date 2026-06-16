class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heapq.heappush(heap, -1 * stone)

        while len(heap) > 1:
            x = -1 * heapq.heappop(heap)
            y = -1 * heapq.heappop(heap)

            if x < y:
                heapq.heappush(heap, -1 * (y - x))
            elif x > y:
                heapq.heappush(heap, -1 * (x - y))
        
        if heap:
            return -1 * heap[0]
        
        return 0