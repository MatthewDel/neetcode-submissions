class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.sol = [[]]
        def helper(temp, index):
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                temp.append(nums[i])
                self.sol.append(temp[::])
                helper(temp, i + 1)
                temp.pop()
            return 

        helper([],0)
        return self.sol 