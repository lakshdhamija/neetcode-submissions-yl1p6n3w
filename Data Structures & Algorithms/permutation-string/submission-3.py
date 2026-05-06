class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        countS, countT = [0] * 26, [0] * 26
        for c in s1: countS[ord(c) - ord('a')] += 1
        for c in range(0, len(s1)): countT[ord(s2[c]) - ord('a')] +=  1
        print(countS, countT)
        l , r = 0, len(s1) - 1

        while r < len(s2):
            print(countT, l , r)
            if countS == countT: return True
            countT[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r == len(s2): break
            countT[ord(s2[r]) - ord('a')] += 1
        return False
                
        