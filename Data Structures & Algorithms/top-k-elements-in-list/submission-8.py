

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = defaultdict(int)

        # Iterate through the numbers and populate a map of value => frequency
        for num in nums:
            frequency_map[num] += 1

        # Uses bucket sort to map frequency => values at that frequency
        bucket_sort = [[] for i in range(len(nums))]
        for key, value in frequency_map.items():
            bucket_sort[value-1].append(key)

        # Iterate backward through that solution collecting k items
        sol = []
        for i in range(len(bucket_sort)-1, -1, -1):
            for num in bucket_sort[i]:
                if k == 0:
                    return sol
                sol.append(num)
                k -= 1
            
        return sol 




        
        
