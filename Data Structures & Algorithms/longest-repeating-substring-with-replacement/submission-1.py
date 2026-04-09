class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_of_chars = {}

        max_freq_chars = 0

        l=0
        ret = 0

        for r in range(len(s)): #iterate through all possible values of r
            count_of_chars[s[r]] = 1 + count_of_chars.get(s[r], 0) #add to char count table
            max_freq_chars = max(max_freq_chars, count_of_chars[s[r]]) #update most frequent char
            

            while((r-l+1)-max_freq_chars > k): #if the window size has too many unique chars (more than k)
                count_of_chars[s[l]]-=1 #edit char count table accordingly
                l+=1 #make l move up (sliding window)
            ret = max(ret, r-l+1) #window length
        
        return ret