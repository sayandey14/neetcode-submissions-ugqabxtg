class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        ret = []

        for i in strs:
            sorted_str = str(sorted(i))
            anagram_map[sorted_str].append(i)
        
        for i in anagram_map.values():
            ret.append(i)

        return ret