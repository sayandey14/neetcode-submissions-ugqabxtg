class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2) < len(s1)):
            return False


        hash1 = {}
        hash2 = {}

        for i in s1:
            hash1[i] = hash1.get(i, 0) + 1
        
        for i in range(len(s1)):
            hash2[s2[i]] = hash2.get(s2[i], 0) + 1
        
        l=0
        r = len(s1) - 1

        while(r < len(s2)):
            if(hash2 == hash1):
                return True
            else:
                hash2[s2[l]] -= 1
                if hash2[s2[l]] == 0:
                    del hash2[s2[l]]
                l+=1
                r+=1
                if r < len(s2):
                    hash2[s2[r]] = hash2.get(s2[r], 0) + 1
        
        return False
            
