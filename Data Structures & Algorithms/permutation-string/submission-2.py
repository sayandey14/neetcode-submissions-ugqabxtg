class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}

        for i in s1:
            hashmap[i] = 1+hashmap.get(i, 0)

        print(hashmap)
        
        extra = len(s1)

        for i in range(len(s2)-extra+1):
            hashtemp = {}
            for j in range(extra):
                hashtemp[s2[i+j]] = 1+hashtemp.get(s2[i+j], 0)
            if hashtemp==hashmap:
                return True
        return False
