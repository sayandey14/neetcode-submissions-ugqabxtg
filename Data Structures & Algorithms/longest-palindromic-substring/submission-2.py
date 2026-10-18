class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0  # best window, inclusive

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return [l + 1, r - 1]  # last valid window


        for i in range(len(s)):
            l, r = expand(i, i)
            if r - l > end - start:
                start, end = l, r

        for i in range(len(s)):
            l, r = expand(i, i + 1)
            if r - l > end - start:
                start, end = l, r
        return s[start:end + 1]