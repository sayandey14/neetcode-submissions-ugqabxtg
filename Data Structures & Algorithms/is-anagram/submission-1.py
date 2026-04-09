class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashsetS = defaultdict(int)
        hashsetT = defaultdict(int)
        for i in s:
            if i not in hashsetS:
                hashsetS[i] = 0
            else:
                hashsetS[i] +=1
        
        for i in t:
            if i not in hashsetT:
                hashsetT[i] = 0
            else:
                hashsetT[i] +=1
        
        return (hashsetT==hashsetS)