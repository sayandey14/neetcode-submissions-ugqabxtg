class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ret = 0
        l=0
        maxf=0
        #window is r-l+1
        for r in range(len(s)):
            count[s[r]] = 1+count.get(s[r],0)
            maxf = max(maxf, count[s[r]]) #track most frequent char in window

            while (r-l+1-maxf) > k: # while window is invalid, shift l up
                count[s[l]] -=1
                l+=1
            ret = max(ret, r-l+1)
        
        return ret


