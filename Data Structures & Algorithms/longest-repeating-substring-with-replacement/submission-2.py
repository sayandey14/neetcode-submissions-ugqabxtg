class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        count = {}
        streak = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) #updates most frequent character

            while (r-l+1) - maxf >k:
                count[s[l]] -= 1
                l += 1
            streak = max(streak, r-l+1)
        return streak
            




            