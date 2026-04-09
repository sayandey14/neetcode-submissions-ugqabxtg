class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        #dict
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = 1+hashmap.get(nums[i], 0)
        


        for i in range(k):
            max_temp = hashmap.get(0,0)
            idx = 0;
            for j,k in hashmap.items():
                if(k>max_temp):
                    max_temp = k
                    idx = j
            ret.append(idx)
            hashmap.pop(idx)
        
        return ret
                