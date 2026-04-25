class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexOne = 0 
        indexTwo = len(numbers)-1 
        while indexOne<indexTwo:
            computation = numbers[indexOne] + numbers[indexTwo] 
            if computation == target:
                return [indexOne+1, indexTwo+1]
            elif computation > target:
                indexTwo -= 1
            else:
                indexOne += 1 
        return -1