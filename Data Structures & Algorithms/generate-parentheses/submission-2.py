class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open, close, path):
            if open == close == n:
                res.append(''.join(path))
                return
            if open < n:
                path.append('(')
                dfs(open + 1, close, path)
                path.pop()
            if close < open:
                path.append(')')
                dfs(open, close + 1, path)
                path.pop()
        dfs(0, 0, [])
        return res
