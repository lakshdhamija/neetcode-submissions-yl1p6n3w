class Solution:
    def calculate(self, s: str) -> int:
        total = prev = num = 0
        op, i = '+', 0
        while i <= len(s):
            ch = s[i] if i < len(s) else '+'
            if ch == ' ':
                i += 1
                continue
            if ch.isdigit(): num = num * 10 + int(ch)
            else:
                if op == '+':
                    total += num
                    prev = num
                elif op == '-':
                    total -= num
                    prev = -num
                elif op == '*':
                    total -= prev
                    total += prev * num
                    prev = num * prev
                else:
                    total -= prev
                    total += int(prev / num)
                    prev = int (prev / num)
                num = 0
                op = ch
            i += 1
        return total