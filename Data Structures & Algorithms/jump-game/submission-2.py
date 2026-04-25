class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Greedy: At cast from each element I would like to take the largest jump allowed to me
        #Starting at nums[0]
        #I have the possibility to jump to nums[0] elements
        #Of those elements I would like to take the one that pushes me the furthest. To calculate that I would take the current index + nums[i].
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0
