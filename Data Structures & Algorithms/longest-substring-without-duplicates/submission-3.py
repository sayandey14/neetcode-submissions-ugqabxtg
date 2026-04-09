class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        seen = set()
        longest = 0
        streak = 0

        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                    streak-=1
            seen.add(s[r])
            streak += 1
            longest = max(longest, streak)
        
        return longest