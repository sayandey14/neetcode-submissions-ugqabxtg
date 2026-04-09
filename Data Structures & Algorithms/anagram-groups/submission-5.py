class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for i in strs:
            temp = [0]*26 # list of chars
            for j in i:
                temp[ord(j)-ord('a')] +=1 #ascii values to list 
            hashmap[tuple(temp)].append(i)
        return list(hashmap.values())

