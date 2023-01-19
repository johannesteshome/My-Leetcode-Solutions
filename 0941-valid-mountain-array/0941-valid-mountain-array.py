class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if(len(arr) < 3):
            return False
        greatest = max(arr)
        greatestIndex = arr.index(greatest)
        
        if(greatestIndex == 0 or greatestIndex == len(arr) - 1):
            return False
        
        for i in range(greatestIndex):
            if(arr[i] >= arr[i+1]):
                return False
        for i in range(greatestIndex, len(arr)-1):
            if(arr[i] <= arr[i+1]):
                return False
        return True