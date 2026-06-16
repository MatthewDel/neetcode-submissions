class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []

        frequency = {}

        for task in tasks:
            frequency[task] = frequency.get(task, 0) + 1

        for key in frequency:
            heapq.heappush(heap, (-1 * frequency[key], key))

        queue = deque()

        time = 0 

        while queue or heap:
            time += 1
            if queue and queue[0][0] == time:
                task_meta_data_queue = queue.popleft()
                to_run = task_meta_data_queue[2]
                task = task_meta_data_queue[1]
                heapq.heappush(heap, (to_run, task))

            if heap:
                task_meta_data = heapq.heappop(heap)
                
                to_run = task_meta_data[0] + 1
                task = task_meta_data[1]

                if to_run != 0:
                    queue.append((time + n + 1, task, to_run))
        
        return time



