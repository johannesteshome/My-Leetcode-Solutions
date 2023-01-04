class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = list(zip(*grid))
        count = 0
        for index in range(len(cols)):
            cols[index] = list(cols[index])
        
        for i in range(len(grid)):
            if(grid[i] in cols):
                count += cols.count(grid[i])
        # print(cols)
        return count