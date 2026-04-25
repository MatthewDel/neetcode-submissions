class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        insertion_point = m + n - 1 

        left = m - 1
        right = n - 1

        for i in range(m + n):
            if left >= 0 and right >= 0:
                leftIsGreaterThanRight = nums1[left] >= nums2[right]
                nums1[insertion_point] = max(nums1[left], nums2[right])
                if leftIsGreaterThanRight:
                    left -= 1
                else:
                    right -= 1 
            elif left >= 0:
                nums1[insertion_point] = nums1[left]
                left -= 1
            else:
                nums1[insertion_point] = nums2[right]
                right -= 1
            insertion_point -= 1

            
                
            

        