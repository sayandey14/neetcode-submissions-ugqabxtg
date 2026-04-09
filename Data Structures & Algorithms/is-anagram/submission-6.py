class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        hasht = {}

        for i in s:
            hashs[i] = 1 + hashs.get(i, 0)
        for i in t:
            hasht[i] = 1 + hasht.get(i, 0)
        
        return hashs==hasht