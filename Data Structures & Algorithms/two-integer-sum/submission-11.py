class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, val in enumerate(nums):
            dif = target - val
            if dif in hashMap:
                return [hashMap[dif], index]
            hashMap[val] = index
        return False

