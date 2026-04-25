class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hash_set = set()
        
        for i in range(n):
            if nums[i] in hash_set:
                return True 
            hash_set.add(nums[i])
        
        return False
