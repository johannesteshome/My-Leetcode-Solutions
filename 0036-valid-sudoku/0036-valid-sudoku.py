class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        hashSets = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if(board[i][j] != "."):
                    if board[i][j] in rowMap[i]:
                        return False
                    else:
                        rowMap[i].add(board[i][j])
                    if board[i][j] in colMap[j]:
                        return False
                    else:
                        colMap[j].add(board[i][j])
                    if(board[i][j] in hashSets[(i//3, j//3)]):
                        return False
                    else:
                        hashSets[(i//3, j//3)].add(board[i][j])
                        
        return True