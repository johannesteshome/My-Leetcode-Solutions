class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        length = len(mat)

        for i in range(length):
            answer += mat[i][i]
        
        for i in range(length):
            if i != (length - 1)-i:
                answer += mat[i][(length - 1)-i]
        
        return answer
        