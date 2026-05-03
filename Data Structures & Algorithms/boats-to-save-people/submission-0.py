class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # index is the weight of the ith
        # infinite boats
        # each boat can carry a max weight limit 
        # max two people in each boat, but their sum needs to be <= limit 
        # min number of boats

        count = 0
        people.sort()
        left = 0
        right = len(people) - 1

        while left <= right:
            added = people[left] + people[right]
            
            if added > limit:
                right -= 1
            else:
                left += 1
                right -= 1

            count += 1
        return count

