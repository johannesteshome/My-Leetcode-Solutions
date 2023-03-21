class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # initializing a stack
        stack = []
        # a list to store both the position and speed in one place
        posSpeed = []
        # the output of the carfleets
        carFleets = 0

        # storing the position and speed in posSpeed and sorting them
        for i in range(len(position)):
            posSpeed.append([position[i], speed[i]])
        posSpeed.sort()

        # iterating through posSpeed form the left
        for i in range(len(posSpeed)-1, -1, -1):
            if not stack:
                # if the stack is empty calculate the time it needs to reach the target and store it at the top of the stack and count it as a car fleet since a single car can be counted as a car fleet
                time = (target - posSpeed[i][0]) / posSpeed[i][1]
                stack.append([posSpeed[i][0], time])
                carFleets += 1
                continue
            # if the stack is not empty calculate the time needed to reach the target of the current array item and compare it the speed of the car at the top of stack
            time = (target - posSpeed[i][0]) / posSpeed[i][1]
            # if the time at the top of the stack is higher it means at some point they will meet and will be counted as single car fleet hence no need to perform additional operation since we counted the car at the top of the stack as a single car fleet - they are both merged together
            if time <= stack[-1][1]:
                continue
            # if the current car's time to reach the target is greater then it can not reach the car front of it hence they will not be merged so it will be counted as a single car fleet 
            else:
                stack.append([posSpeed[i][0], time])
                carFleets += 1
        return carFleets