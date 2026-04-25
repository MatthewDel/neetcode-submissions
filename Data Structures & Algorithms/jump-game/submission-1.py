class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Greedy: At cast from each element I would like to take the largest jump allowed to me
        #Starting at nums[0]
        #I have the possibility to jump to nums[0] elements
        #Of those elements I would like to take the one that pushes me the furthest. To calculate that I would take the current index + nums[i].
        index = 0
        while index != (len(nums) - 1):
            max_index = index
            max_jump = 0
            for i in range(1, nums[index] + 1):
                if (index + i == (len(nums) - 1)):
                    return True 

                if (index + i + nums[index + i]) > max_jump:
                    max_jump = (index + i + nums[index + i])
                    max_index = index + i 
            if max_jump == 0:
                return False
            if max_jump >= (len(nums) - 1):
                return True 
            index = max_index 
        
        return True 