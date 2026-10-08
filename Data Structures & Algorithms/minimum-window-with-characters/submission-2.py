class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(t) > len(s)):
            return ""
        
        if s==t:
            return s
        
        chars_of_T = {}

        window = {}

        l=0

        ret = [0,0]

        for i in t:
            chars_of_T[i] = chars_of_T.get(i, 0) + 1
        
        need = len(chars_of_T)
        cur = 0
        longest = float("infinity")

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if(s[r] in chars_of_T and window[s[r]] == chars_of_T[s[r]]):
                cur+=1
            
            while(cur == need):
                if(r-l+1 < longest):
                    ret = [l, r]
                    longest = r-l+1
                
                window[s[l]]-=1

                if(s[l] in chars_of_T and window[s[l]] < chars_of_T[s[l]]):
                    cur-=1
                l+=1
        
        l=ret[0]
        r=ret[1]

        if(longest == float("infinity")):
            return ""
        else:
            return s[l:r+1]
                
        