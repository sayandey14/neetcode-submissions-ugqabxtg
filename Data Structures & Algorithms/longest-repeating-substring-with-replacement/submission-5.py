class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        max_freq_char_cnt = 0
        l=0
        streak = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            max_freq_char_cnt = max(max_freq_char_cnt, hashmap[s[r]])

            
            while(r-l+1 - max_freq_char_cnt > k):
                hashmap[s[l]]-=1
                l+=1
            
            streak = max(streak, r-l+1)
        
        return streak