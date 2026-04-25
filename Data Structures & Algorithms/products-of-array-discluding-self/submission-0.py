class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        right_product = []
        running_product = 1
        for i in range(len(nums)):
            running_product = nums[i]*running_product
            left_product.append(running_product)
        
        running_product = 1
        for i in range(len(nums)-1,-1,-1):
            running_product = nums[i]*running_product
            right_product.append(running_product)
        
        
        right_product = right_product[::-1]
        print(left_product)
        print(right_product)
        sol = []
        for i in range(len(nums)):
            if i == 0:
                sol.append(right_product[i+1])
            elif i == len(nums)-1:
                sol.append(left_product[i-1])
            else:
                sol.append(left_product[i-1] * right_product[i+1])
        return sol