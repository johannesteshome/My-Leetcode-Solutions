class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mat = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        # print(mat)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # print(i, j)
                mat[j][i] = matrix[i][j]
        
        return mat