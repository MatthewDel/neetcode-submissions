class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        sol = []
        window_size = 0
        
        for i in range(len(nums)):
            window_size += 1
            heapq.heappush(heap, (-1 * nums[i], i))

            if window_size > k:
                window_size -= 1

            if window_size == k:
                while(heap[0][1] <= (i - k)):
                    heapq.heappop(heap)
                sol.append(-1 * heap[0][0])
        
        return sol

