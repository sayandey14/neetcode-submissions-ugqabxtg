class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()

        l=0
        maxStreak = 0
        streak = 0
        for r in range(len(s)):
            while(s[r] in hashset):
                streak -= 1
                hashset.remove(s[l])
                l+=1
            streak += 1
            hashset.add(s[r])
            maxStreak = max(maxStreak, streak)
        
        return maxStreak