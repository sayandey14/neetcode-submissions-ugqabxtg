class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)

        if(slen!=tlen):
            return False
        
        slist = []
        for i in s:
            slist.append(i)
        slist.sort()
        
        tlist = []
        for i in t:
            tlist.append(i)
        tlist.sort()

        for i in range(0,slen):
            if(slist[i]!=tlist[i]):
                return False
        return True
        