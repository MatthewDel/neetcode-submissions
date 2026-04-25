class Solution:
        
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        for key in freq:
            heapq.heappush(heap, (-1 * freq[key]))

        queue = deque()

        time = 0
        while heap or queue:
            time += 1
            if not heap:
                time = queue[0].time
            else:
                curr = (heapq.heappop(heap)) + 1
                if curr:
                    queue.append(Node(time + n, curr))
            if queue and queue[0].time == time:
                heapq.heappush(heap, queue.popleft().freq)
        return time
        



class Node:
    def __init__(self, time, freq):
        self.time = time
        self.freq = freq



        
