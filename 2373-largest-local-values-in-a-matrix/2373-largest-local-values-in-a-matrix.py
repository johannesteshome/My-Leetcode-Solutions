class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in range(1, len(grid) - 1):
            row =[]
            for j in range(1, len(grid[0]) - 1):
                max0 = max(grid[i-1][j-1:j+2])
                max1 = max(grid[i][j-1:j+2])
                max2 = max(grid[i+1][j-1:j+2])
                row.append(max(max0, max1, max2))
            answer.append(row)
            
        return answer