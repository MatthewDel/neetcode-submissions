class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
 
        preserve = []

        for index, num in enumerate(nums):
            preserve.append([num,index])

        preserve = sorted(preserve)

        left = 0

        right = len(preserve)-1 

        while left < right:

            if (preserve[left][0] + preserve[right][0]) == target:
                return [min(preserve[left][1], preserve[right][1]),max(preserve[left][1], preserve[right][1])]
            if (preserve[left][0] + preserve[right][0]) > target:
                right = right - 1 
            else:
                left = left + 1
        return -1 
            