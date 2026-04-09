class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sset = {}
        tset = {}

        for i in s:
            sset[i] = 1 + sset.get(i,0)
        for i in t:
            tset[i] = 1 + tset.get(i,0)

        return sset==tset