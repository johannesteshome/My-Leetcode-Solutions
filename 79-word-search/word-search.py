class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # helper fucntion to check if my search is inbound
        # iterate throgugh the grid and check if the first character matches with the current cell
        # start my dfs search
            # keep track path cells
            # once I found the next char in the word, I will go deep
            # if I find the word then I imediately return True
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        maxX = len(board)
        maxY = len(board[0])

        def inbound(x, y):
            return 0 <= x < maxX and 0 <= y < maxY
        
        def dfs(x, y, strIndex):


            if strIndex == len(word):
                return True

            if (x, y) in path:
                return

            if not inbound(x,y):
                return
            
            if board[x][y] != word[strIndex]:
                return
            
            # print(x,y,strIndex,path, board[x][y])
            path.add((x, y))
            
            for dir in directions:
                newX = x + dir[0]
                newY = y + dir[1]

                if dfs(newX, newY, strIndex + 1):
                    return True
            
            path.remove((x,y))
        

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    path = set()
                    if dfs(i, j, 0):
                        return True
        
        return False
            