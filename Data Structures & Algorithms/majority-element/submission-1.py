class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        popular = nums[0]
        votes = 1
        for i in range(len(nums)):
            if nums[i] != popular:
                votes -= 1
                if votes == 0:
                    popular = nums[i]
                    votes = 1
            else:
                votes += 1
        return popular