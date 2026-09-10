class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in strs:
            ret = ret+str(len(i)) + "#" + i
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        length = 0
        start = 0
        i=0
        while(i<len(s)):
            #find length
            if(s[i]=='#'):
                length = int(s[start:i])
                ret.append(s[i+1:i+length+1])
                start = i+length+1
                i=i+length+1
            i+=1
        return ret
            

