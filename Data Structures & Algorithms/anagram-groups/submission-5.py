class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listDict  = {}
        for s in strs:
            strSorted = "".join(sorted(s))
            if strSorted in listDict: listDict[strSorted].append(s)
            else: listDict[strSorted] = [s]
        return [v for v in listDict.values()]