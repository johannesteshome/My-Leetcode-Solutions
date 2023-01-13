class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #creating the dictionary
        diagonals = defaultdict(list)
        #populating the dictionary with the values of the subtracttion of their index
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diagonals[i-j].append(matrix[i][j])
                
        #traversing the dictionary to check if they fulfill the condition
        for value in diagonals.values():
            res = value.count(value[0]) == len(value)
            if(not res):
                return False
        
        return True