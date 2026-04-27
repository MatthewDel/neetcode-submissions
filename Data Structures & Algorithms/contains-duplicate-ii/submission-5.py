class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        running_set = set()

        for i in range(len(nums)):
            if (i - left) > k:
                running_set.remove(nums[left])
                left += 1

            if nums[i] in running_set:
                return True 
            
            running_set.add(nums[i])
        return False
            