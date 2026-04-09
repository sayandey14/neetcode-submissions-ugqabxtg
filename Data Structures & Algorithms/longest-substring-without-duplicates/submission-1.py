class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l=0
        r=0
        hashset = set()
        streak = 0
        while(r<len(s)):
            if(s[r] not in hashset):
                hashset.add(s[r])
                r+=1
                streak +=1
                longest = max(longest, streak)
            else:
                hashset.remove(s[l])
                l+=1
                streak-=1
        
        return longest
                