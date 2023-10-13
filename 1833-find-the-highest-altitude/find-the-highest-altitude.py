class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        Max = 0
        temp = 0

        for i in range(len(gain)):
            temp = temp + gain[i]
            Max = max(Max, temp)

        
        return Max
        