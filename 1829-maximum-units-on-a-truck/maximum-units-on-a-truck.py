class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        newArr = []
        ans = 0

        for boxType in boxTypes:
            newArr.append([boxType[1], boxType[0]])
        
        newArr.sort(reverse=True)

        for boxType in newArr:
            if boxType[1] > truckSize:
                ans += (truckSize * boxType[0])
                return ans
            else:
                ans += (boxType[0] * boxType[1])
                truckSize -= boxType[1]
        
        return ans