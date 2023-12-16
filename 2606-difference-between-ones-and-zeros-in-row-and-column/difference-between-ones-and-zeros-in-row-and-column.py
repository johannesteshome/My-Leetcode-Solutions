class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        cols = list(zip(*grid))
        onesRow = []
        onesCol = []
        zerosRow = []
        zerosCol = []
        
        for grids in grid:
            onesRow.append(grids.count(1))
            zerosRow.append(grids.count(0))
        
        for col in cols:
            onesCol.append(col.count(1))
            zerosCol.append(col.count(0))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
                
        return grid