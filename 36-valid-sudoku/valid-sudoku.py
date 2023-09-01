class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudokoSize = {
            0: "q1",
            1: "q1",
            2: "q1",
            3: "q2",
            4: "q2",
            5: "q2",
            6: "q3",
            7: "q3",
            8: "q3"
        }

        cols = defaultdict(set)
        rows = defaultdict(set)
        sudokos = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in cols[i]:
                    cols[i].add(board[i][j])
                else: return False
                if board[i][j] not in rows[j]:
                    rows[j].add(board[i][j])
                else: return False
                if board[i][j] not in sudokos[(sudokoSize[i], sudokoSize[j])]:
                    sudokos[(sudokoSize[i], sudokoSize[j])].add(board[i][j])
                else: return False
        
        return True
