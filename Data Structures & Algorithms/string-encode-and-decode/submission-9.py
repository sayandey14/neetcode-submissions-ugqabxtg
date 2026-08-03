class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in strs:
            ret += str(len(i)) + "#" + i
        
        return ret

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        length = 0


        while(i<len(s)):
            temp = i

            while(s[temp]!="#"):
                temp+=1
            
            length = int(s[i:temp])
            decoded.append(s[temp+1:temp+1+length])

            i = temp + 1 + length
        
        return decoded

