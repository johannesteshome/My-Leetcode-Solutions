class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i=0
        while(i < length):
            print(i)
            if(arr[i] == 0):
                # print(arr[i])
                arr.insert(i, 0)
                i = i+2
                # print(arr)
            else:
                i = i+1
        
        for i in range(len(arr) - length):
            arr.pop()