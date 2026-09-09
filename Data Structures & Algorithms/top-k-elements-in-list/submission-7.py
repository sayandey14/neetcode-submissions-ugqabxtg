class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] +=1


        reverse = {}

        for key,value in freq.items():
            if(value not in reverse):
                reverse[value] = []
            reverse[value].append(key)
        
        ret = []
        for i in range(len(nums), 0, -1):
            if(i in reverse):
                for j in reverse[i]:
                    ret.append(j)
                    if(len(ret) == k):
                        return ret
        return []

