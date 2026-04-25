class Solution:
    def sortColors(self, nums: List[int]) -> None:
        bucket = [0] * 3
        for i in range(len(nums)):
            bucket[nums[i]] += 1

        index = 0 
        for i in range(3):
            while bucket[i]:
                nums[index] = i
                index += 1
                bucket[i] -= 1
        
        return
        
        