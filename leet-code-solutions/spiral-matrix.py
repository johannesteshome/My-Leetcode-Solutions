class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [[0,1], [1,0], [0,-1], [-1, 0] ]
        hashmap = {}
        i, j = 0,0
        index = 0
        hashmap[(0,0)] = matrix[0][0]
        print(hashmap)
        print((0,0) not in hashmap)
        while(len(hashmap) < len(matrix)*len(matrix[0])):
            i = i+direction[index][0]
            j = j+direction[index][1]
            
            if(((i < len(matrix) and i >= 0) and (j < len(matrix[0]) and j >= 0)) and (i, j) not in hashmap):
                hashmap[(i, j)] = matrix[i][j]
                # print(hashmap)
            else:
                i = i-direction[index][0]
                j = j-direction[index][1]
                if(index == len(direction) - 1):
                    index = 0
                else:
                    index += 1
                        
        # print(hashmap)
        answer = list(hashmap.values())
        return answer