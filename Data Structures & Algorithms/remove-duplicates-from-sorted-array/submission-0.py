class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        point_of_insertion = 1
        curr_number = nums[0]
        for i in range(len(nums)):
            if nums[i] != curr_number:
                nums[point_of_insertion] = nums[i]
                point_of_insertion += 1
                curr_number = nums[i]
        return point_of_insertion

            
            
            