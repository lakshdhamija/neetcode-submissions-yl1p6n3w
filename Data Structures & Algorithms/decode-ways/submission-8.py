class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1 # empty string is valid
        dp[1] = 1 # 1st digit is valid
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0': dp[i] += dp[i - 1] # 1 digit
            if 10 <= int(s[i-2:i]) <= 26: dp[i] += dp[i - 2] # 2 digit
        return dp[len(s)]