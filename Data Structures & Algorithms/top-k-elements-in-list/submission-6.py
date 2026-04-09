class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap = key:value -> number:freq
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        
        print(freq)

        #now = key:value -> freq:numbers
        reverse = {}
        for i in freq.values():
            reverse[i] = []
        
        for i in freq:
            reverse[freq[i]].append(i) #multiple numbers can have the same frequence
        

        ret = []

        for i in range(len(nums), -1, -1):
            if(i in reverse):
                for j in reverse[i]:
                    ret.append(j)
                    if(len(ret) == k):
                        return ret

        return ret

