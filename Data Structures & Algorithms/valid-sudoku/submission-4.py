class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets, colSets, sqSets = {}, {}, {}
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if ((r in rowSets and board[r][c] in rowSets[r]) or
                        (c in colSets and board[r][c] in colSets[c]) or
                        ((r // 3, c // 3) in sqSets and board[r][c] in sqSets[(r // 3, c // 3)])):
                        return False
                    if r not in rowSets: rowSets[r] = set()
                    if c not in colSets: colSets[c] = set()
                    if (r // 3, c // 3) not in sqSets: sqSets[(r // 3, c // 3)] = set()
                    rowSets[r].add(board[r][c])
                    colSets[c].add(board[r][c])
                    sqSets[(r // 3, c // 3)].add(board[r][c])
        return True

        