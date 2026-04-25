class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            sol  = [] 
            index_left = 0
            index_right = 0
            while index_left < len(left) and index_right < len(right):
                if left[index_left] <= right[index_right]:
                    sol.append(left[index_left])
                    index_left += 1
                else:
                    sol.append(right[index_right])
                    index_right += 1
            while index_left < len(left):
                sol.append(left[index_left])
                index_left += 1
            while index_right < len(right):
                sol.append(right[index_right])
                index_right += 1 
            print(sol)
            return sol

        def mergeSort(nums):
            if not nums or len(nums) == 1:
                return nums
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)
        return mergeSort(nums)
        
        