class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        answer = [[1],[1,1]]

        def pascal(arr, level):
            print(arr, level)
            if level == numRows:
                return
        
            newArr = [1]
            for i in range(len(arr) - 1):
                newArr.append(arr[i] + arr[i+1])
            newArr.append(1)
            arr = newArr
            
            answer.append(arr)
            pascal(arr, level+1)
        
        pascal([1,1], 2)
        return answer