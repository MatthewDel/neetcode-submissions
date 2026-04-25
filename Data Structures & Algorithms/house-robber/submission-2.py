class Solution:
    def rob(self, nums: List[int]) -> int:
        tabulation = [0] * (len(nums) + 3)
        for i in range(len(nums) - 1, -1, -1):
            tabulation[i] = nums[i] + max(tabulation[i+2], tabulation[i+3])
        print(tabulation)
        return max(tabulation[0], tabulation[1])

        
        

        