class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in strs:
            temp = [0] * 26
            for j in i:
                temp[ord(j) - ord('a')] +=1
            if(tuple(temp) not in hashmap):
                hashmap[tuple(temp)] = []
            hashmap[tuple(temp)].append(i)
        
        return list(hashmap.values())
