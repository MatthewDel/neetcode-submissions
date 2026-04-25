class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]]+=1
            else:
                hash_map[nums[i]]=1
        for key in hash_map:
            heapq.heappush(heap, (-hash_map[key], key))
        
        sol = []
        for i in range(k):
            sol.append(heapq.heappop(heap)[1])
        return sol