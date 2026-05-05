class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs: res += str(len(s)) + '#' + s
        print(res)
        return res
    
    def decode(self, s: str) -> List[str]:
        i, j, res = 0, 0, []
        while i < len(s) and j < len(s):
            while s[j] != '#': j += 1
            strLen = int(s[i:j])
            res.append(s[j + 1: j + 1 + strLen])
            i = j + 1 + strLen
            j = i
        return res
