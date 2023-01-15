class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, 0
        
        while(i < len(matrix)):
            if(matrix[i][j] == target):
                return True
            elif(matrix[i][j] > target and i != 0):
                while(j < len(matrix[0])):
                    if(matrix[i-1][j] == target):
                        return True
                    j+=1
                return False
            elif(i+1 == len(matrix)):
                # print("here")
                while(j < len(matrix[0])):
                    if(matrix[i][j] == target):
                        return True
                    j+=1
                return False
            else:
                i+=1