class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dictionary = defaultdict(set)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                dictionary[i-j].add(matrix[i][j])
        
        for key in dictionary:
            if len(dictionary[key]) > 1:
                return False
        
        return True