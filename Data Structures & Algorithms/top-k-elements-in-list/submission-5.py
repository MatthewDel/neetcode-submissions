

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        buckets = [[] for i in range(len(nums))]

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        for key in hashmap:
            buckets[hashmap[key] - 1].append(key)
        
        sol = []

        for i in range(len(buckets)-1, -1, -1):
            for j in range(len(buckets[i])):
                if k == 0:
                    return sol 
                sol.append(buckets[i][j])
                k -= 1
        
        return sol 



        
        
