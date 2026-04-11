class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        
        l1 = [0]*26
        l2 = [0]*26

        for i in s1:
            l1[ord(i) - ord('a')] +=1
        
        for i in range(len(s1)):
            l2[ord(s2[i]) - ord('a')] +=1
        

        l=0
        
        matches = 0
        for i in range(26):
            if(l1[i] == l2[i]):
                matches+=1
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            #right extend
            index = ord(s2[r]) - ord('a')
            l2[index] += 1
            if(l2[index] == l1[index]):
                matches +=1
            elif(l1[index] + 1 == l2[index]):
                matches -=1 #gained one

            #left extend
            index = ord(s2[l]) - ord('a')
            l2[index] -=1
            if(l2[index] == l1[index]):
                matches +=1
            elif(l1[index] - 1 == l2[index]):
                matches -=1 #lost one
            l+=1
        return matches == 26
