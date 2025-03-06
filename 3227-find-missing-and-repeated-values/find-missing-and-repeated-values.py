class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashmap = defaultdict(int)
        answer = [0,0]

        for i in range(1, len(grid) * len(grid) + 1):
            hashmap[i] = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                hashmap[grid[i][j]] += 1
        
        for i in range(1, len(grid) * len(grid) + 1):
            if hashmap[i] == 0:
                answer[1] = i
            elif hashmap[i] == 2:
                answer[0] = i
        
        return answer