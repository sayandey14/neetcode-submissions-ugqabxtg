class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        #dict
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = 1+hashmap.get(nums[i], 0)
        

        dict2 = {}

        for i in hashmap.values():
            dict2[i] = []
        
        for i,j in hashmap.items():
            dict2[j].append(i)

        

        print(dict2)

        for i in range(len(nums), 0,-1):
            if i in dict2:
                for value in dict2[i]:
                    ret.append(value)
                    if(len(ret)==k):
                        return ret
        


                