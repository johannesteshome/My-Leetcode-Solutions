class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(0, length//2):
            for j in range(i, length-(i+1)):
                newi = j
                newj = (length-i)-1
                # print(newi, newj, "another")
                temp = matrix[newi][newj]
                matrix[newi][newj] = matrix[i][j]
                # print(matrix)
                for _ in range(4):
                    anotheri = newi
                    anotherj = newj
                    newi = anotherj
                    newj = (length-anotheri)-1
                    # print(newi, newj, "here")
                    temp1 = matrix[newi][newj]
                    matrix[newi][newj] = temp
                    # print(matrix)
                    temp = temp1
                