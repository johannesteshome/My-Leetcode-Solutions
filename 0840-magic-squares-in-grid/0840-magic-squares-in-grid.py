class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row, cols = len(grid), len(grid[0])
        nums = defaultdict(int)
        count = 0
        
        for i in range(1,10):
            nums[i]
        
        for i in range(row-2):
            for j in range(cols-2):
                
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if grid[k][l] in nums:
                            nums[grid[k][l]] = 1
                            
                found = True
                for num in nums:
                    if nums[num] != 1:
                        found = False
                        break
                
                if grid[i][j] + grid[i][j+1] + grid[i][j+2] == grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] == grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] == grid[i][j] + grid[i+1][j] + grid[i+2][j] == grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] == grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] == grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] and found:
                    count += 1
                
                for num in nums:
                    nums[num] = 0
        return count
                
                
                
                        