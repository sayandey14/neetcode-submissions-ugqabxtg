class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            temp = [0]*26
            for j in i:
                temp[ord(j)-ord('a')]+=1
            hashmap[tuple(temp)].append(i)
        
        return list(hashmap.values())

