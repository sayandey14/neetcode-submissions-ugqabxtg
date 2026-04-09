class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = {}
        longest = 0
        streak = 0

        l=0
        r=0

        while(r<len(s)):
            if(s[r] not in hashset):
                hashset[s[r]] = 0
                r+=1
                streak+=1
            else:
                while(s[r] in hashset):
                    hashset.pop(s[l])
                    l+=1
                    streak-=1
            longest = max(longest, streak)
        return longest                
                