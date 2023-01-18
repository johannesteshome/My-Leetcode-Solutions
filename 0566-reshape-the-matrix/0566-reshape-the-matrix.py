class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # rows = r
        # cols = c
        
        # if(rows < cols):
        #     answer = [[0*cols] for _ in range(rows) ]
        # else:
        #     answer = [[0]*cols for _ in range(rows)]
        # print(answer)
        
        answers = []

        if(r*c != len(mat)*len(mat[0])):
            return mat
        else:
            R = 0
            C = 0
            
            answer = []
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if(C < c):
                        print(R,C, "first if")
                        answer.append(mat[i][j])
                        C = C + 1
                    elif(C == c):
                        answers.append(answer)
                        C = 0
                        R = R + 1
                        answer = []
                        answer.append(mat[i][j])
                        C = C +1
                        print(R, C, "elif")
            answers.append(answer)
            print(answers)
            return answers
                        