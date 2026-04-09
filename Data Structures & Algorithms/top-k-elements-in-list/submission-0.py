class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        ret = []
        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] = 0
        
        for i in range(k):
            max_key = max(hashmap, key = hashmap.get)
            ret.append(max_key)
            del hashmap[max_key]
        return ret
        
        