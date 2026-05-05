class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet, colSet, sqSet = [set() for _ in range(9)], [set() for _ in range(9)], defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': continue
                if (board[r][c] in rowSet[r] or
                board[r][c] in colSet[c] or
                board[r][c] in sqSet[(r // 3, c // 3)]): return False

                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                sqSet[(r//3, c//3)].add(board[r][c])
        return True
