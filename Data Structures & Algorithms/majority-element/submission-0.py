class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Democratic voting
        popular = nums[0]
        vote = 1 
        for i in range(1, len(nums)):
            if nums[i] == popular:
                vote += 1 
            else:
                vote -= 1 
                if not vote:
                    popular = nums[i]
                    vote = 1
        return popular