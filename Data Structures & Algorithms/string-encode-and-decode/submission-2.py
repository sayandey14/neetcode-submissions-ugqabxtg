class Solution:
    def encode(self, strs: List[str]) -> str:
        # Encode each string as "<len>#<string>"
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find the separator #
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # extract length
            word = s[j+1 : j+1+length]  # grab string of that length
            res.append(word)
            i = j + 1 + length  # move pointer
        return res
