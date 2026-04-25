class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1 

        while left < right:
            sum_of_values = numbers[left] + numbers[right]
            if (sum_of_values > target):
                right -= 1
            elif (sum_of_values < target):
                left += 1
            else:
                return [left + 1, right + 1]