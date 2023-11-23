class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in range(len(image)):
            row = []
            for j in range(len(image[i])-1, -1, -1):
                row.append(abs(image[i][j] - 1)) 
            answer.append(row)

        return answer
        