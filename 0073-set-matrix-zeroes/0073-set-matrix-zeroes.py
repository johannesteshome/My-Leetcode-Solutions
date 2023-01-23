class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        setOfZeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == 0):
                    setOfZeroes.append([i,j])
        
        
        for zero in setOfZeroes:
            yindex = 0      
            xindex = 0
            while(yindex < len(matrix[0])):
                matrix[zero[0]][yindex] = 0
                yindex+=1
            while(xindex < len(matrix)):
                matrix[xindex][zero[1]] = 0
                xindex+=1
        