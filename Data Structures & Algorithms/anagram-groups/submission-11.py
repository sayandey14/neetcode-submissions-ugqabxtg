class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []

        hashmap = {}

        for string in strs:
            temp = [0]*26
            for i in string:
                temp[ord(i) - ord('a')] +=1
            tup = tuple(temp)
            if tup in hashmap:
                hashmap[tup].append(string)
            else:
                hashmap[tup] = [string]
        
        for k,v in hashmap.items():
            ret.append(v)
        

        return ret
