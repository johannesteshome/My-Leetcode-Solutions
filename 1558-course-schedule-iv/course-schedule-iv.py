class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrix = [[False for _ in range(numCourses)] for _ in range(numCourses)]

        for pre in prerequisites:
            matrix[pre[0]][pre[1]] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
        
        answer = []
        for q in queries:
            answer.append(matrix[q[0]][q[1]])
        return answer