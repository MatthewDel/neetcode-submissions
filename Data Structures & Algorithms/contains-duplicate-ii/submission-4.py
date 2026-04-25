class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Sliding window: I need to make sure that the range does not excees k or that the sliding window is no larger than k 
        #I could maintain a set for the sliding window, if the number appears twice, then return true 
        hashset = set()
        left = 0
        for right in range(len(nums)):
            if right - left > k :
                hashset.remove(nums[left])
                left += 1 
            if nums[right] in hashset:
                return True 
            hashset.add(nums[right])
        return False 

