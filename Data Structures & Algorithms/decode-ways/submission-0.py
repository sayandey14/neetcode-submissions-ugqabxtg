class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i == len(s):      # decoded the whole string: one valid way
                return 1
            if s[i] == '0':      # nothing starts with 0
                return 0
            if i in memo:
                return memo[i]

            # case 1: take one digit (1–9, already guaranteed non-zero)
            res = dfs(i + 1)
            # case 2: take two digits if they form 10–26
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                res += dfs(i + 2)

            memo[i] = res
            return res

        return dfs(0)