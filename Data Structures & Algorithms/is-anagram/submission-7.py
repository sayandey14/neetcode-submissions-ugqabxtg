class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sets = {}
        sett = {}

        for i in s:
            sets[i] = 1 + sets.get(i, 0)
        
        for i in t:
            sett[i] = 1 + sett.get(i, 0)
        
        return sets==sett