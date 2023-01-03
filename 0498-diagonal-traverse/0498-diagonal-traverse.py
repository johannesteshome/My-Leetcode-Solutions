class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = 0
        n = 0
        
        sizeM = len(mat)
        sizeN = len(mat[0])
        answer = []
        
        [upDiagonal, downDiagonal, right, down] = [(-1, 1), (1, -1), (0, 1), (1, 0)]
        
        goUp = True
        
        while not ( ( sizeM-1) == m and (sizeN-1) == n):
            # print(m, n)
            answer.append(mat[m][n])
            if goUp:
                if(not self.outOfBound(m + upDiagonal[0], n + upDiagonal[1], sizeM, sizeN)):
                    m += upDiagonal[0]
                    n += upDiagonal[1]
                else:
                    goUp = False
                    if(not self.outOfBound(m + right[0], n + right[1], sizeM, sizeN)):
                        m += right[0]
                        n += right[1]
                    else: 
                        m += down[0]
                        n += down[1]     
            else:
                if(not self.outOfBound(m + downDiagonal[0], n + downDiagonal[1], sizeM, sizeN)):
                    m += downDiagonal[0]
                    n += downDiagonal[1]
                else:
                    goUp = True
                    if(not self.outOfBound(m + down[0], n + down[1], sizeM, sizeN)):
                        m += down[0]
                        n += down[1]
                    else:
                        m += right[0]
                        n += right[1]
        
        answer.append(mat[m][n])
        
        return answer
            
            
            
    def outOfBound(self, m, n, sizeM, sizeN):
        return m < 0 or m >= sizeM or n < 0 or n >= sizeN