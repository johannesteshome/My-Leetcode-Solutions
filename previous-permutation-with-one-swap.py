class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1, 0, -1):
            if arr[i] < arr[i-1]:
                index = i
                temp = arr[i]
                for j in range(i, len(arr)):
                    if arr[j] > arr[i] and arr[j] < arr[i-1]:
                        temp = arr[j]
                        index = j
                        
                arr[index] = arr[i-1]
                arr[i-1] = temp
                break
        
        return arr