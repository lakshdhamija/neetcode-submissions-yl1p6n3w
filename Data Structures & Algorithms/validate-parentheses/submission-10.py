class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in ['[', '{', '(']: st.append(c)
            else:
                if not len(st): return False
                if c == ']' and st.pop() != '[': return False
                if c == '}' and st.pop() != '{': return False
                if c == ')' and st.pop() != '(': return False
        return True if not len(st) else False