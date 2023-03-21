class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        posSpeed = []
        carFleets = 0
        for i in range(len(position)):
            posSpeed.append([position[i], speed[i]])
        posSpeed.sort()
        print(posSpeed)

        for i in range(len(posSpeed)-1, -1, -1):
            if not stack:
                speedTop = (target - posSpeed[i][0]) / posSpeed[i][1]
                stack.append([posSpeed[i][0], speedTop])
                carFleets += 1
                continue
            speed = (target - posSpeed[i][0]) / posSpeed[i][1]
            if speed <= stack[-1][1]:
                continue
            else:
                stack.append([posSpeed[i][0], speed])
                carFleets += 1
        return carFleets