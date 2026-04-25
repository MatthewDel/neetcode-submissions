class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}
        for i in range(len(nums)):
            if target-nums[i] in hash_set:
                return [hash_set[target-nums[i]], i]
            hash_set[nums[i]] = i
        
        return -1