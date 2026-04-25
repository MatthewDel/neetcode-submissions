class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        for index, value in enumerate(position):

            position[index] = (value, index)
        
        position = sorted(position)

        print(position)

        carFleet = 0

        currentFleet = 0

        for i in range(len(position)-1, -1, -1):

            top = position.pop()

            pos =  top[0]

            index = top[1]

            spd = speed[index]

            targetTime =  (target - pos) / spd

            print(pos,spd, targetTime)

            if targetTime > currentFleet:

                carFleet+=1

                currentFleet = targetTime 
        
        return carFleet
            
