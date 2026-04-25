class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(len(points)):
            heapq.heappush(max_heap, (-1 * (points[i][0] ** 2 + points[i][1] ** 2), points[i]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [point[1] for point in max_heap] 