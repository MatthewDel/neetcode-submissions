class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)

        runningProduct = nums[0]
        for i in range(1, len(nums)):
            sol[i] = runningProduct 
            runningProduct = runningProduct * nums[i]

        runningProduct = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            sol[i] = sol[i] * runningProduct
            runningProduct = runningProduct * nums[i]

        return sol
