class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        min_length = float('inf')
        running_sum = 0

        for i in range(len(nums)):
            running_sum += nums[i]
            print(running_sum)

            while running_sum >= target:
                min_length = min(min_length, i - left + 1)
                running_sum -= nums[left]
                left += 1

                if running_sum >= target:
                    min_length = min(min_length, i - left + 1)

        return 0 if min_length == float("inf") else min_length
