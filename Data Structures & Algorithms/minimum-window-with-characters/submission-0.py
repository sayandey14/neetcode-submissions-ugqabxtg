class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if (len(t) > len(s)):
            return ""
        
        if s==t:
            return s
        
        #find all "substrings" of t in s
        #return the one with the smallest length 

        charsT = {}

        window = {}

        for i in t:
            charsT[i] = 1 + charsT.get(i, 0)
        
        curChars = 0
        neededChars = len(charsT)
        l=0
        ret = [0,0]
        streak = float("infinity") #max possible number 
        

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in charsT and charsT[s[r]] == window[s[r]]:
                curChars += 1
            
            while curChars == neededChars:
                if (r-l+1) < streak:
                    ret = [l, r]
                    streak = r-l+1
                
                window[s[l]] -=1
                
                if s[l] in charsT and window[s[l]] < charsT[s[l]]:
                    curChars -=1
                l+=1
        
        l = ret[0]
        r = ret[1]

        if (streak == float("infinity")):
            return ""
        else:
            return s[l:r+1]

            

        


