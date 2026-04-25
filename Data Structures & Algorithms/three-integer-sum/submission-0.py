class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
       
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            left = i+1 
            right = len(nums) -1 
            while left < right:
                res = nums[left] + nums[right] + nums[i]
                if res == 0:
                    sol.append([nums[left],nums[right],nums[i]])
                    temp = nums[left]
                    while left < right and nums[left] == temp:
                        left += 1
                    temp = nums[right]
                    while left < right and nums[right] == temp:
                        right -= 1
                elif res > 0:
                    right -= 1 
                else:
                    left += 1
            
        return sol 
                    
                