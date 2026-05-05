class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        for st in strs:
            ctMap = [0] * 26
            for c in st: ctMap[ord(c) - ord('a')] += 1
            if str(ctMap) in strMap: strMap[str(ctMap)].append(st)
            else: strMap[str(ctMap)] = [st]
        return [val for val in strMap.values()]
