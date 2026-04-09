class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        hashtemp = {}

        for i in s1:
            hashmap[i] = 1+hashmap.get(i,0)
        print(hashmap)

        tempstr = s2[0:len(s1)]

        for i in tempstr:
            hashtemp[i] = 1+hashtemp.get(i,0)
        print(hashtemp)


        for i in range(len(s2)-len(s1)):
            if(hashtemp==hashmap):
                return True
            if hashtemp[s2[i]] == 1:
                del hashtemp[s2[i]]
            else:
                hashtemp[s2[i]] -= 1
            right_char = s2[i + len(s1)]
            hashtemp[right_char] = 1 + hashtemp.get(right_char, 0)

        return hashtemp==hashmap
        