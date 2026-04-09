class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        hashmap = {}
        maxfreq = 0
        longest = 0

        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            maxfreq = max(hashmap[s[r]], maxfreq)

            while (r-l+1) - maxfreq > k:
                hashmap[s[l]] -=1
                l+=1
                
            longest = max(longest, r-l+1)
        
        return longest