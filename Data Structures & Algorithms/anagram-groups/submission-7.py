class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            cnt = [0]*26
            for j in i:
                cnt[ord(j)-ord('a')] +=1
            hashmap[tuple(cnt)].append(i)
        return list(hashmap.values())


