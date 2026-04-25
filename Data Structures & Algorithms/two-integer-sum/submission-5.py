class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
 
        hashmap = {}

        for index, num in enumerate(nums):

            hashmap[num] = index
        
        for i in range(0, len(nums)):

            if (target - nums[i]) in hashmap and hashmap[target - nums[i]] != i:

                return [min(hashmap[target - nums[i]],i),max(hashmap[target - nums[i]],i)]
            
            else:
                
                hashmap[nums[i]] = i 

        return []
            
            