class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0

        for right in range(k, len(arr)):
            left_dist = abs(arr[left] - x)
            right_dist = abs(arr[right] - x)

            if left_dist > right_dist:
                left += 1
            else:
                # only safe to break once arr[right] >= x
                if arr[right] >= x:
                    break

        return arr[left:left + k]