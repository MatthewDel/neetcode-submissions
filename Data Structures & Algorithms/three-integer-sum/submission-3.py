class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        for i in range(len(nums)-2):

            if i!=0 and nums[i] == nums[i-1]:
                continue
            left = i + 1 
            right =  len(nums)-1
            while left<right:
                calc = nums[i] + nums[left] + nums[right]
                if calc == 0:
                    sol.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif calc < 0:
                    left += 1
                else:
                    right -= 1
        return sol

                
                