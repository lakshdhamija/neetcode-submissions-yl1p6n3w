class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(openCnt, closeCnt, curStr):
            if openCnt == closeCnt == n:
                res.append(curStr)
                return
            if openCnt < n:
                curStr += '('
                backtracking(openCnt + 1, closeCnt, curStr)
                curStr = curStr[:len(curStr) - 1]
            if closeCnt < openCnt:
                curStr += ')'
                backtracking(openCnt, closeCnt + 1, curStr)
                curStr = curStr[:len(curStr) - 1]
        backtracking(0, 0, "")
        return res