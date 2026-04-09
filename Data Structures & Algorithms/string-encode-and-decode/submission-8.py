class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in strs:
            ret += str(len(i)) + "#" + i
        print(ret)
        return ret;

    def decode(self, s: str) -> List[str]:
        decoy = s
        ret = []
        i=0
        if(len(s) == 0):
            return []
        start = 0
        while i<len(s):
            if(s[i] == "#"):
                length = int(s[start:i])
                apd = s[i+1:i+1+length]
                ret.append(apd)
                start = i + length+1
                i = i+length+1
            i+=1
        return ret

