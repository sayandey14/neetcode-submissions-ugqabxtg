class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+= str(len(i)) + "#" + i
        return s
        
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0

        while i<len(s):
            start = i
            while s[start] != "#":
                start += 1
            length = int(s[i:start])
            i = start+1
            start = i + length
            ret.append(s[i:start])
            i=start
        return ret