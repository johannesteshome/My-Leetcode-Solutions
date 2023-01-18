class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
      
        answers = []

        if(r*c != len(mat)*len(mat[0])):
            return mat

        R = 0
        C = 0

        answer = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if(C < c):
                    answer.append(mat[i][j])
                    C = C + 1
                elif(C == c):
                    answers.append(answer)
                    C = 0
                    R = R + 1
                    answer = []
                    answer.append(mat[i][j])
                    C = C +1
        answers.append(answer)
        return answers