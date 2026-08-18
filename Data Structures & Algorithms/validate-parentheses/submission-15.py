class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMapping = { ')':'(', ']':'[', '}':'{' }
        for ch in s:
            if (ch == '(' or ch == '{' or ch == '['): stack.append(ch)
            elif(len(stack) == 0 or (stack.pop() != bracketMapping[ch])): return False
        return len(stack) == 0