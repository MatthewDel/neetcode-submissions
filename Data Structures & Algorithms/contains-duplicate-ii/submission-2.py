class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Sliding window: I need to make sure that the range does not excees k or that the sliding window is no larger than k 
        #I could maintain a set for the sliding window, if the number appears twice, then return true 
        if k == 0:
            return False 
            
        left = 0 
        right = 1
        dups = set()
        dups.add(nums[0])
        while right < len(nums):
            while right < len(nums) and abs(right - left) <= k:
                if nums[right] in dups:
                    return True 
                dups.add(nums[right])
                right += 1
            while left < right and abs(right - left) > k:
                dups.remove(nums[left])
                left += 1
        return False 

