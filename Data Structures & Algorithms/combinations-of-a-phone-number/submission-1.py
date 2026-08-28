class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digitStrMap = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz'
        }
        res = []
        def backtracking(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitStrMap[digits[i]]: backtracking(i + 1, curStr + c)
        backtracking(0, "")
        return res


