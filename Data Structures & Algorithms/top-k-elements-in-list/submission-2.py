class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num,0)
        
        arr = []
        for key in hashmap:
            arr.append([hashmap[key], key])
        
        arr.sort();

        sol = []

        for i in range(k):
            sol.append(arr.pop()[1])
        
        return sol

