class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        hashmap = {}
        maxF = 0
        longest = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            maxF = max(maxF, hashmap[s[r]])

             
            while((r-l+1) - maxF > k):
                hashmap[s[l]] -= 1
                l+=1
            
            longest = max(longest, (r-l+1))
        
        return longest
    
            
