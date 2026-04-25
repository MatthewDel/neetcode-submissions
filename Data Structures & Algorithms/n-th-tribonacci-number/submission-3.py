class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1 
        
        three, two, one = 0, 1, 1

        for i in range(3, n + 1):
            temp = one + two + three
            three = two 
            two = one 
            one = temp
        return one