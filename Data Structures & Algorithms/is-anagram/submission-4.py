class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        hashsets = {}
        hashsett = {}


        for i in range(len(s)):
            hashsets[s[i]] = 1+hashsets.get(s[i],0)
            hashsett[t[i]] = 1+hashsett.get(t[i],0)

        return hashsets==hashsett

