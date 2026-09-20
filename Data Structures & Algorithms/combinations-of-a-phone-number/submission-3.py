class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digToStr = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        res = []
        def dfs(i, word):
            if i == len(digits):
                res.append(word)
                return
            for c in digToStr[int(digits[i])]: dfs(i + 1, word + c)
        dfs(0, "")
        return res